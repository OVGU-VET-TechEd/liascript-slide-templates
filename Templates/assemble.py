#!/usr/bin/env python3
"""Build LiaScript sessions from the slide templates and a plain-text content file.

  python3 assemble.py skeleton CONTENT.txt Template_A.md Template_B.md ...
      Write a content file for the chosen templates (in this order), pre-filled with the
      fill-guide examples and with meaning and limit of every field as comments.

  python3 assemble.py build CONTENT.txt OUT.md
      Fill the templates with the content and write a complete course file. Stops with a list
      of problems if a field is missing, unknown, or unsafe inside a script.

  python3 assemble.py raw OUT.md Template_A.md ...
      Concatenate the templates without filling them (placeholders stay in place).

Content file format:
  [course]                      course header fields (AUTHOR, EMAIL, COURSE-TITLE, ...)
  [Introduction_Template_3.md]  one section per slide template, in slide order; a template may repeat
  KEY = value                   one line
  KEY = \"\"\"                  several lines, closed by a line with \"\"\" only
  ...
  \"\"\"
  # comment                     lines starting with # are ignored
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BEGIN, END = "<!-- TEMPLATE:BEGIN -->", "<!-- TEMPLATE:END -->"
PLACEHOLDER = re.compile(r"%%([A-Z0-9-]+)%%")
COURSE_DEFAULTS = {"VERSION": "0.1.0", "LANGUAGE": "en", "NARRATOR": "US English Female", "COURSE-SUBTITLE": ""}
COURSE_GUIDE = [
    ("AUTHOR", "Name of the author", "Dr. A. Example"),
    ("EMAIL", "Contact address", "a.example@uni-example.de"),
    ("COURSE-TITLE", "Title shown on the first page", "Fluid Mechanics – Session 1"),
    ("COURSE-SUBTITLE", "One line under the title (may stay empty)", "Winter term 2026 · Faculty of Mechanical Engineering"),
    ("COURSE-DESCRIPTION", "One sentence for the course header, no colon", "Interactive session on hydrostatic pressure."),
    ("VERSION", "Version number of the material", "0.1.0"),
    ("LANGUAGE", "Language code (de for German)", "en"),
    ("NARRATOR", "Voice for the narration (Deutsch Female for German)", "US English Female"),
]


def template_path(name):
    path = HERE / name
    if not path.exists():
        sys.exit(f"unknown template: {name}")
    return path


def slides_of(text, name):
    if BEGIN not in text or END not in text:
        sys.exit(f"{name}: TEMPLATE:BEGIN/END markers missing")
    return text.split(BEGIN, 1)[1].split(END, 1)[0].strip()


def imports_of(text):
    return re.findall(r"https://\S+README\.md", text.split("-->", 1)[0])


def guide_rows(text):
    """(field, meaning, limit, example) for every placeholder documented in the fill guide."""
    rows = []
    guide = text.split(BEGIN, 1)[0]
    for line in guide.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) != 4 or not cells[0].startswith("`%%"):
            continue
        names = re.findall(r"%%([A-Z0-9-]+)%%", cells[0])
        rng = re.match(r"`%%([A-Z0-9-]*?)(\d+)([A-Z-]*)%%` … `%%\1(\d+)\3%%`", cells[0])
        if rng:
            pre, a, post, b = rng.group(1), int(rng.group(2)), rng.group(3), int(rng.group(4))
            names = [f"{pre}{n}{post}" for n in range(a, b + 1)]
        examples = [e.strip() for e in cells[3].split(" ; ")]
        if len(examples) != len(names):
            examples = [cells[3]] * len(names)
        for name, example in zip(names, examples):
            if re.fullmatch(r"`[^`]*`", example):
                example = example[1:-1]
            rows.append((name, cells[1], cells[2], example))
    # Multi-line defaults (programs) follow the table as "**Default for `%%FIELD%%`:**" plus a code block
    defaults = dict(re.findall(r"\*\*Default for `%%([A-Z0-9-]+)%%`:\*\*\s*\n\s*\n```[^\n]*\n(.*?)\n```", guide, re.S))
    return [(n, m, l, defaults.get(n, e)) for n, m, l, e in rows]


def ordered_fields(slides):
    seen = []
    for name in PLACEHOLDER.findall(slides):
        if name not in seen:
            seen.append(name)
    return seen


def script_fields(slides):
    """Placeholders that sit inside <script> blocks or script attributes: values must not break JavaScript."""
    parts = re.findall(r"<script.*?</script>", slides, re.S)
    return {n for part in parts for n in PLACEHOLDER.findall(part)}


def parse_content(path):
    sections, current, key, buf = [], None, None, None
    for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if buf is not None:
            if line.strip() == '"""':
                current[1][key] = "\n".join(buf)
                buf = None
            else:
                buf.append(line)
            continue
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\[(.+)\]\s*$", line)
        if m:
            current = (m.group(1).strip(), {}, number)
            sections.append(current)
            continue
        m = re.match(r"^([A-Z0-9-]+)\s*=\s?(.*)$", line)
        if not m or current is None:
            sys.exit(f"{path}:{number}: expected [section] or KEY = value, got: {line}")
        key, value = m.group(1), m.group(2)
        if value.strip() == '"""':
            buf = []
        else:
            current[1][key] = value.strip()
    if buf is not None:
        sys.exit(f'{path}: unclosed """ block for {key}')
    return sections


def skeleton(out, names):
    lines = ["# Content file – fill in the values, then run:",
             f"#   python3 assemble.py build {Path(out).name} MySession.md",
             "# Each value replaces one %%FIELD%% in the template. Values may contain Markdown and $LaTeX$.",
             "# Several lines:  KEY = \"\"\"  …  \"\"\"", "", "[course]"]
    for key, meaning, example in COURSE_GUIDE:
        lines += [f"# {meaning}", f"{key} = {example}"]
    for name in names:
        text = template_path(name).read_text(encoding="utf-8")
        slides = slides_of(text, name)
        rows = {r[0]: r for r in guide_rows(text)}
        purpose = re.search(r"\*\*Purpose:\*\* (.*)", text)
        lines += ["", "", f"[{name}]", f"# {purpose.group(1) if purpose else ''}"]
        for field in ordered_fields(slides):
            _, meaning, limit, example = rows.get(field, (field, "?", "?", ""))
            lines.append(f"# {meaning} · {limit}")
            lines += [f'{field} = """', example, '"""'] if "\n" in example else [f"{field} = {example}"]
    Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(names)} templates)")


def build(content, out):
    sections = parse_content(content)
    problems, parts, imports = [], [], []
    course = dict(COURSE_DEFAULTS)
    for name, values, line in sections:
        if name == "course":
            course.update(values)
            continue
        text = template_path(name).read_text(encoding="utf-8")
        slides = slides_of(text, name)
        fields = set(ordered_fields(slides))
        for missing in sorted(fields - set(values)):
            problems.append(f"[{name}] (line {line}): missing {missing}")
        for unknown in sorted(set(values) - fields):
            problems.append(f"[{name}] (line {line}): unknown field {unknown}")
        for field in sorted(script_fields(slides) & set(values)):
            if re.search(r'["`\\\n]', values[field]):
                problems.append(f"[{name}] (line {line}): {field} is used inside a script – no quotes, backticks, backslashes or line breaks")
        slides = PLACEHOLDER.sub(lambda m: values.get(m.group(1), m.group(0)), slides)
        parts.append(slides)
        imports += [url for url in imports_of(text) if url not in imports]
    for key in ("AUTHOR", "EMAIL", "COURSE-TITLE", "COURSE-DESCRIPTION"):
        if key not in course:
            problems.append(f"[course]: missing {key}")
    if problems:
        sys.exit("cannot build:\n  " + "\n  ".join(problems))

    header = (HERE / "_Header_Template.md").read_text(encoding="utf-8")
    header = header.split("<!-- TEMPLATE:BEGIN -->", 1)[1].split(END, 1)[0].strip() if BEGIN in header else header
    course["IMPORTS"] = "\n          ".join(imports)
    if not imports:
        header = re.sub(r"\n\nimport:\s+%%IMPORTS%%", "", header)
    header = PLACEHOLDER.sub(lambda m: course.get(m.group(1), m.group(0)), header)
    result = header.rstrip() + "\n\n" + "\n\n".join(parts) + "\n"
    left = sorted(set(PLACEHOLDER.findall(result)))
    if left:
        sys.exit("unfilled fields left: " + ", ".join(left))
    Path(out).write_text(result, encoding="utf-8")
    slide_count = len(re.findall(r"^## ", result, re.M))
    print(f"wrote {out}: {len(parts)} templates, {slide_count} slides, imports: {len(imports)}")


def raw(out, names):
    parts = [slides_of(template_path(n).read_text(encoding="utf-8"), n) for n in names]
    Path(out).write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(names)} templates, unfilled)")


def main():
    args = sys.argv[1:]
    if len(args) >= 3 and args[0] == "skeleton":
        skeleton(args[1], args[2:])
    elif len(args) == 3 and args[0] == "build":
        build(args[1], args[2])
    elif len(args) >= 3 and args[0] == "raw":
        raw(args[1], args[2:])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
