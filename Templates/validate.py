#!/usr/bin/env python3
"""Check slide templates against CONVENTIONS.md (structure, placeholders, animations, quizzes, imports).

Usage: python3 validate.py [FILE.md ...]   (default: all *_Template_*.md in this folder)
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MERMAID = "https://raw.githubusercontent.com/LiaTemplates/mermaid_template/0.1.4/README.md"
PYODIDE = "https://raw.githubusercontent.com/LiaTemplates/Pyodide/0.3.5/README.md"
PLACEHOLDER = re.compile(r"%%[A-Z0-9_-]+%%")
BEGIN, END = "<!-- TEMPLATE:BEGIN -->", "<!-- TEMPLATE:END -->"


def documented_fields(guide):
    """Placeholders named in the fill guide; a row '%%X-1%% … %%X-4%%' documents X-1 to X-4."""
    fields = set(PLACEHOLDER.findall(guide))
    for pre, a, post, b in re.findall(r"%%([A-Z0-9-]*?)(\d+)([A-Z-]*)%%`? … `?%%\1(\d+)\3%%", guide):
        fields |= {f"%%{pre}{n}{post}%%" for n in range(int(a), int(b) + 1)}
    return fields


def check(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors = []

    # Code fences and the lines outside of code blocks
    if sum(1 for line in lines if re.match(r"\s*```", line)) % 2:
        errors.append("odd number of code fences")
    body, in_code = [], False
    for line in lines:
        if re.match(r"\s*```", line):
            in_code = not in_code
        elif not in_code:
            body.append(line)

    # File layout
    if sum(1 for line in body if line.startswith("# ")) != 1:
        errors.append("need exactly one '#' heading")
    if BEGIN not in text or END not in text:
        return errors + ["TEMPLATE:BEGIN/END markers missing"]
    # The fill guide is rendered on the title slide: everything between '# Template' and TEMPLATE:BEGIN
    guide = re.search(r"^# Template[^\n]*\n(.*?)" + re.escape(BEGIN), text, re.S | re.M)
    if not guide or "| Placeholder | Meaning | Limit | Example |" not in guide.group(1):
        return errors + ["fill guide table missing between '# Template' and TEMPLATE:BEGIN"]
    for key in ("**Purpose:**", "**Pairs with:**", "**Variants:**"):
        if key not in guide.group(1):
            errors.append(f"fill guide line {key} missing")
    visible = re.sub(r"`[^`\n]*`", "", guide.group(1)).replace('<!-- data-type="none" -->', "")
    if "%%" in visible:
        errors.append("placeholder in the fill guide outside backticks (would render with italics)")
    for token in ("[[", "[(", "{{", "***", "<!--", "-->", "![", "!?[", "??["):
        if token in visible:
            errors.append(f"LiaScript syntax {token} in the fill guide outside backticks (would render live)")
    slides = text.split(BEGIN, 1)[1].split(END, 1)[0]

    # Placeholders
    for field in sorted(set(PLACEHOLDER.findall(text))):
        if "_" in field:
            errors.append(f"underscore in placeholder (renders as italics): {field}")
    documented = documented_fields(guide.group(1))
    used = set(PLACEHOLDER.findall(slides))
    for field in sorted(used - documented):
        errors.append(f"placeholder not in fill guide: {field}")
    for field in sorted(documented - used):
        errors.append(f"fill guide lists unused placeholder: {field}")

    # Animation: per slide, narration 0, consecutive steps, narration directly before each step
    slide_lines = body
    starts = [i for i, line in enumerate(slide_lines) if line.startswith("## ")]
    for k, start in enumerate(starts):
        block = slide_lines[start:starts[k + 1] if k + 1 < len(starts) else len(slide_lines)]
        title = block[0][3:]
        shown = {}
        for i, line in enumerate(block):
            m = re.match(r"^\s{6}\{\{(\d+)(?:-\d+)?\}\}\s*$", line)
            if m:
                shown[int(m.group(1))] = i
        spoken = {int(n) for n in re.findall(r"--\{\{(\d+)[^}]*\}\}--", "\n".join(block))}
        if 0 not in spoken:
            errors.append(f"slide '{title}': no --{{{{0}}}}-- narration")
        if shown and sorted(shown) != list(range(1, max(shown) + 1)):
            errors.append(f"slide '{title}': reveal steps not consecutive {sorted(shown)}")
        for n, i in shown.items():
            before = [line for line in block[:i] if line.strip()][-2:]
            if len(before) < 2 or not re.match(rf"^\s{{4}}--\{{\{{{n}\}}\}}--\s*$", before[0]):
                errors.append(f"slide '{title}': narration --{{{{{n}}}}}-- must stand directly before step {{{{{n}}}}}")

    # Containers, details, quizzes
    depth = 0
    for i, line in enumerate(body):
        depth += len(re.findall(r"<(div|section)\b", line)) - len(re.findall(r"</(div|section)>", line))
        if depth == 0 and line.startswith("####"):
            errors.append(f"'####' outside a container: {line.strip()}")
        nxt = next((l for l in body[i + 1:] if l.strip()), "")
        if line.strip() == "</script>" and nxt.startswith("[[?]]"):
            errors.append("hint [[?]] after </script> is printed as raw text – put hints before the script")
        if re.match(r"^\[\[(?!\?\]\]|_)[^\]|]+\]\]\s*$", line):  # text quiz alone on a line
            rest = [l for l in body[i + 1:] if l.strip() and not l.startswith("[[?]]")]
            if not rest or rest[0].strip() != "<script>":
                errors.append(f"text quiz without answer script (case-sensitive): {line.strip()}")
    if re.search(r"<details>\n(?!\n)|(?<!\n)\n</details>", text):
        errors.append("<details> needs blank lines inside")

    # Imports must match the macros that are used
    header = text.split("-->", 1)[0]
    imports = set(re.findall(r"https://\S+README\.md", header))
    for url in imports - {MERMAID, PYODIDE}:
        errors.append(f"import not allowed: {url}")
    for macro, url in (("@mermaid", MERMAID), ("@Pyodide.eval", PYODIDE)):
        if (macro in slides) != (url in imports):
            errors.append(f"{macro} used without its import, or import without use")
    return errors


def main():
    files = [Path(f) for f in sys.argv[1:]] or sorted(HERE.glob("*_Template_*.md"))
    bad = 0
    for path in files:
        errors = check(path)
        bad += bool(errors)
        print(f"{'OK ' if not errors else 'ERR'} {path.name}")
        for error in errors:
            print("     -", error)
    print(f"{len(files) - bad}/{len(files)} templates pass")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
