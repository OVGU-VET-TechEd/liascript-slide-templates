#!/usr/bin/env python3
"""Generate index.html (GitHub Pages) with LiaScript links to every template and the demo session.

Usage: python3 Templates/tools/build_index.py   (from the repository root)
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = "OVGU-VET-TechEd/liascript-slide-templates"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
LIA = "https://liascript.github.io/course/?"
GITHUB = f"https://github.com/{REPO}/blob/main/"
FAMILIES = [
    ("Introduction", "Opening slide of a course or session"),
    ("Overview_Course", "What to expect and the learning objectives"),
    ("Content_Introduction", "Start of a new content block"),
    ("Concept_Explanation", "Explain a concept, a contrast or a process"),
    ("Interactive_Exercise", "Practise with quizzes and calculations"),
    ("Simulation", "Explore with sliders, JavaScript and Python"),
    ("Media", "Use video, figures and external simulations actively"),
    ("Application_Transfer", "Apply knowledge: cases, mistakes, discussion"),
    ("Summary_Recap", "Close the session: recap, exit ticket, reflection"),
]


def card(path):
    text = path.read_text(encoding="utf-8")
    purpose = re.search(r"\*\*Purpose:\*\* (.*)", text).group(1)
    comment = re.search(r"^comment:\s+(.*)$", text, re.M).group(1)
    rel = path.relative_to(ROOT).as_posix()
    n = path.stem.rsplit("_", 1)[1]
    return f"""      <article class="card">
        <h3>Variant {n}</h3>
        <p class="what">{html.escape(comment)}</p>
        <p class="use">{html.escape(purpose)}</p>
        <div class="links">
          <a class="btn" href="{LIA}{RAW}{rel}" target="_blank" rel="noopener">Open in LiaScript</a>
          <a class="src" href="{GITHUB}{rel}" target="_blank" rel="noopener">Source</a>
        </div>
      </article>"""


sections = []
for family, job in FAMILIES:
    cards = "\n".join(card(p) for p in sorted((ROOT / "Templates").glob(f"{family}_Template_*.md")))
    title = family.replace("_", " ")
    sections.append(f"""    <section id="{family.lower()}">
      <h2>{title} <span>{job}</span></h2>
      <div class="grid">
{cards}
      </div>
    </section>""")

demo = f"{LIA}{RAW}Demo_Session/Demo_Session.md"
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LiaScript Slide Templates</title>
<style>
  :root {{ --bg:#f6f8fa; --card:#ffffff; --text:#1f2933; --muted:#5f6b7a; --accent:#0b7285; --border:#d9e0e7; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg:#11161c; --card:#1a222b; --text:#e6edf3; --muted:#9aa7b4; --accent:#3bc9db; --border:#2c3742; }}
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text); font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif; }}
  header, main, footer {{ max-width:1100px; margin:0 auto; padding:0 16px; }}
  header {{ padding-top:48px; padding-bottom:16px; }}
  h1 {{ font-size:2rem; margin:0 0 .5rem; }}
  header p {{ color:var(--muted); max-width:760px; margin:.25rem 0; }}
  .hero {{ display:flex; flex-wrap:wrap; gap:12px; margin:20px 0 8px; }}
  nav {{ display:flex; flex-wrap:wrap; gap:8px; margin:20px 0 0; }}
  nav a {{ font-size:.9rem; color:var(--accent); text-decoration:none; border:1px solid var(--border); border-radius:999px; padding:3px 12px; background:var(--card); }}
  section {{ margin:40px 0; }}
  h2 {{ font-size:1.35rem; margin:0 0 14px; }}
  h2 span {{ display:block; font-size:.95rem; font-weight:400; color:var(--muted); }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:14px; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:10px; padding:16px; display:flex; flex-direction:column; }}
  .card h3 {{ margin:0 0 6px; font-size:1rem; }}
  .what {{ margin:0 0 8px; }}
  .use {{ margin:0 0 14px; color:var(--muted); font-size:.92rem; flex:1; }}
  .links {{ display:flex; align-items:center; gap:14px; }}
  .btn {{ background:var(--accent); color:#fff; text-decoration:none; padding:7px 14px; border-radius:6px; font-weight:600; font-size:.92rem; }}
  .btn.big {{ padding:10px 18px; font-size:1rem; }}
  .btn.ghost {{ background:transparent; color:var(--accent); border:1px solid var(--accent); }}
  @media (prefers-color-scheme: dark) {{ .btn {{ color:#0b1a1f; }} .btn.ghost {{ color:var(--accent); }} }}
  .src {{ color:var(--accent); font-size:.92rem; }}
  .demo {{ background:var(--card); border:1px solid var(--border); border-left:4px solid var(--accent); border-radius:10px; padding:18px; }}
  .demo h2 {{ margin-bottom:6px; }}
  code {{ background:var(--border); padding:1px 5px; border-radius:4px; font-size:.9em; }}
  footer {{ color:var(--muted); font-size:.85rem; padding-bottom:40px; }}
  footer a {{ color:var(--accent); }}
</style>
</head>
<body>
<header>
  <h1>LiaScript Slide Templates</h1>
  <p>27 render-tested slide templates in 9 families for interactive teaching with <a href="https://liascript.github.io" style="color:var(--accent)">LiaScript</a>.
     Each link opens the template directly in LiaScript: the first page is its fill guide, the following pages show the slides.</p>
  <p>Build a whole session from a plain-text content file with <code>assemble.py</code> – no LiaScript or code editing needed.</p>
  <div class="hero">
    <a class="btn big" href="{demo}" target="_blank" rel="noopener">Open the demo session</a>
    <a class="btn big ghost" href="https://github.com/{REPO}" target="_blank" rel="noopener">Repository on GitHub</a>
  </div>
  <nav>
{chr(10).join(f'    <a href="#{f.lower()}">{f.replace("_", " ")}</a>' for f, _ in FAMILIES)}
  </nav>
</header>
<main>
  <section class="demo">
    <h2>Demo: Air Pressure – Otto von Guericke's Hemispheres <span>14 slides built from 11 templates and one content file</span></h2>
    <div class="links">
      <a class="btn" href="{demo}" target="_blank" rel="noopener">Open in LiaScript</a>
      <a class="src" href="{GITHUB}Demo_Session/Demo_Session.content.txt" target="_blank" rel="noopener">Content file</a>
      <a class="src" href="{GITHUB}Demo_Session/Demo_Session.md" target="_blank" rel="noopener">Built session</a>
    </div>
  </section>
{chr(10).join(sections)}
</main>
<footer>
  <p>Otto-von-Guericke-Universität Magdeburg · Templates and content under CC BY 4.0, scripts under MIT ·
     Based on ideas from <a href="https://github.com/LiaScript/teaching-agent">LiaScript/teaching-agent</a> and
     <a href="https://github.com/LiaPress/python-marsmission-schule">LiaPress/python-marsmission-schule</a>.</p>
</footer>
</body>
</html>
"""
(ROOT / "index.html").write_text(page, encoding="utf-8")
print("wrote index.html with", page.count("Open in LiaScript") - 1, "template links")
