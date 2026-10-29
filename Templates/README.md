# LiaScript Slide Templates

27 slide templates in 9 families with 3 variants each. They share one set of conventions, so they can be combined
freely: you choose templates, write the content into a plain-text file, and `assemble.py` builds a working LiaScript
session. No LiaScript syntax and no code editing needed – also not for quizzes, sliders or programs.

Sources: the skills of [LiaScript/teaching-agent](https://github.com/LiaScript/teaching-agent), the patterns of
[LiaPress/python-marsmission-schule](https://github.com/LiaPress/python-marsmission-schule), the
[LiaScript documentation](https://liascript.github.io) (v2.5.0). Every template was render-tested in the official viewer.

## Families (typical order in a session)

| # | Family | Job | Variant 1 | Variant 2 | Variant 3 |
|---|---|---|---|---|---|
| 1 | `Introduction_Template_#` | Opening slide | Title image, welcome, self-rating survey | Bullet points only, one-word survey | Real-life hook, prediction quiz, outcome |
| 2 | `Overview_Course_Template_#` | What to expect, objectives | Module table, Bloom objectives, interest survey | Mermaid roadmap, Know / Can / Value, order quiz | "You can …" objectives, workload, prior-knowledge matrix |
| 3 | `Content_Introduction_Template_#` | Start a content block | Picture beside text, activation question | Guiding question, bullets, survey | Real-life example, Predict–Observe–Explain |
| 4 | `Concept_Explanation_Template_#` | Explain a concept | Definition, formula, worked example, calculation | Comparison A vs B, misconception, classification matrix | Process diagram, drag & drop ordering |
| 5 | `Interactive_Exercise_Template_#` | Practise | Single / multiple choice / text quiz with feedback | Gap text (select, type, drag), true/false matrix | Calculation with tolerance check, hints, solution |
| 6 | `Simulation_Template_#` | Explore and compute | Two sliders, live result table and bar | Editable JavaScript, read-off quiz, Basis/Extra | Python in the browser, explore + find the error |
| 7 | `Media_Template_#` | Use media actively | Video with watch-for questions | Figure with hotspots, drag & drop labelling | Embedded simulation (PhET, GeoGebra) with tasks |
| 8 | `Application_Transfer_Template_#` | Apply knowledge | Case analysis with model answers | Find the mistake | Think-Pair-Share with votes before / after |
| 9 | `Summary_Recap_Template_#` | Close the session | Takeaways, recap quiz, outlook | Exit ticket (one item per objective) | Reflection, can-do checklist, feedback matrix, teaser |

Open any template in LiaScript: its first page is the fill guide (purpose, combinations, variants, every field with
meaning, length limit and example).

## Workflow

```bash
cd Templates

# 1 · choose templates (in slide order) and create a content file pre-filled with examples
python3 assemble.py skeleton ../MySession/session01.txt \
    Introduction_Template_3.md Overview_Course_Template_2.md Concept_Explanation_Template_1.md \
    Simulation_Template_1.md Interactive_Exercise_Template_2.md Summary_Recap_Template_2.md

# 2 · replace the example values in session01.txt with your content (plain text, Markdown and $LaTeX$ allowed)

# 3 · build the session
python3 assemble.py build ../MySession/session01.txt ../MySession/session01.md
```

The content file is simple:

```
[course]
AUTHOR = Dr. A. Example
COURSE-TITLE = Fluid Mechanics – Session 1

[Introduction_Template_3.md]
# Catchy title of the case · max 6 words
SLIDE-TITLE = The Bridge That Danced
CASE-TEXT = """
Several lines are possible
between triple quotes.
"""
```

`build` stops with a clear list if a field is missing or unknown, or if a value would break a script. It adds only
the imports (Mermaid, Pyodide) that the chosen templates need. A template may be used several times.
`python3 assemble.py raw OUT.md Template_A.md …` concatenates templates unfilled, for manual editing.

**Changing the setup** without touching code: every template lists its variants on the guide page (delete a step,
add a row, swap the image side, change a tolerance). Slider models, slider ranges and whole programs are content fields.

## Demo session

`../Demo_Session/` contains a complete 14-slide session on air pressure and Otto von Guericke's Magdeburg hemispheres,
built from 11 templates. `Demo_Session.content.txt` is the only file written by hand; `Demo_Session.md` was produced
by `assemble.py build`. Open it in the [LiaScript LiveEditor](https://liascript.github.io/LiveEditor/) or with the
VS Code LiaScript preview.

## Files

| File | Purpose |
|---|---|
| `*_Template_*.md` | the 27 slide templates |
| `_Header_Template.md` | course header used by `assemble.py build` |
| `CONVENTIONS.md` | binding rules and all verified LiaScript patterns – read before changing or adding a template |
| `assemble.py` | `skeleton` / `build` / `raw` |
| `validate.py` | static checks of all templates (`python3 validate.py`) |
| `tools/render_check.mjs` | renders files in headless Chrome with the official viewer and checks every slide (`cd tools && npm install` once) |

## Server-generated variants

`Templates_gx10/` (not part of this repository) receives the same 27 templates generated by the local model `qwen3.8:27b` on gx10-943e
(job `~/gx10-jobs/liascript-templates-v2`) from `CONVENTIONS.md`. They are not reviewed; check them with
`python3 validate.py ../Templates_gx10/*.md` and `node tools/render_check.mjs` before use.
