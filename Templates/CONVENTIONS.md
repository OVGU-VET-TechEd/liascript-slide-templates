# Template conventions (binding, v2)

Every template in this folder follows these rules, so templates can be mixed freely and a lecturer only has to
supply content. Every pattern below was render-tested in the official LiaScript viewer 2.5.0 (headless Chrome):
it displays correctly, and quizzes, scripts, sliders, Python and JavaScript run.

## 1. Placeholders

- Content is written `%%UPPER-KEBAB-NAME%%`, e.g. `%%SLIDE-TITLE%%`, `%%Q1-HINT%%`, `%%IMAGE-ALT%%`.
- **Never use underscores** in placeholder names: LiaScript reads `_…_` as italics (`%%VALUE_1%%` displays as `%%VALUE1%%`).
- Never use `{{…}}`, `[[…]]`, `@…`, `<…>` as placeholders (LiaScript syntax).
- Placeholders may stand inside quiz syntax (`- [(X)] %%Q1-CORRECT%%`, `[[%%Q3-ANSWER%%]]`), script strings
  (`"%%RESULT-VALUE%%"`), script attributes (`min="%%PARAM-1-MIN%%"`), Mermaid labels (`A["%%STEP-1%%"]`) and code
  blocks (` ```python ` + `%%PY-CODE%%`). Values used inside scripts must not contain quotes, backticks or backslashes
  (`assemble.py build` refuses them).
- A placeholder that appears several times in one template gets the same value everywhere.
- Standard names: `%%SLIDE-TITLE%%`, `%%NARRATION-0%%` … `%%NARRATION-n%%`, `%%IMAGE-PATH%%`, `%%IMAGE-ALT%%`,
  `%%IMAGE-CAPTION%%`, `%%KEY-MESSAGE%%`. Further slides of a template use a prefix (`%%EX-TITLE%%`, `%%NARRATION-EX-0%%`).

## 2. File layout

`````markdown
<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  One sentence, no colon.

import:   only the imports this template needs (section 6)
-->

# Template `Family_Template_N`

- **Purpose:** when to use it (1 sentence)
- **Pairs with:** `Sibling_Template_1`, `Sibling_Template_2`
- **Variants:** 1–2 concrete ways to change the setup

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 6 words | The Bridge That Danced |
| `%%STEP-1%%` … `%%STEP-3%%` | Step name | max 3 words | Analyse ; Design ; Build |
| `%%PY-CODE%%` | Python program | 5–25 lines | see default program below |

**Default for `%%PY-CODE%%`:**

```python
print("a working default program")
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

…

<!-- TEMPLATE:END -->
`````

- The `# Template` slide is the **fill guide**: previewing a template in LiaScript shows purpose, combinations, variants
  and the field table. Only the part between `TEMPLATE:BEGIN` and `TEMPLATE:END` goes into a course (1–3 `##` slides).
- In the guide, every placeholder and every piece of LiaScript syntax stands in backticks; otherwise it renders live
  (a `[[ a | (b) ]]` becomes a real quiz, `!?[…](…)` a real video, `%%A_B%%` loses its underscores).
- Do **not** put the guide into an HTML comment: LiaScript ends a comment at the first blank line and prints the rest.
- A range row `%%X-1%%` … `%%X-4%%` documents every number in between.
- The example column holds real, consistent content: `assemble.py skeleton` copies it into new content files.
  Rows with several fields give one example per field, separated by ` ; `.
- Multi-line fields (programs) get their working default in a `**Default for `%%FIELD%%`:**` code block below the table.

## 3. Slides and animation

```
## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

Content visible from the start.

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

Several elements revealed together in step 1.

****************************************
```

- Every slide starts with narration `--{{0}}--` (4 spaces). Every reveal step `{{n}}` (6 spaces) has its own narration
  `--{{n}}--` placed directly before it. Steps count 1, 2, 3 … without gaps and restart at 0 on every `##` slide.
- One element per step: the `{{n}}` line stands directly above it. Several elements: wrap them in two lines of exactly
  40 `*`. Quizzes with solution blocks may sit inside such a group.
- At most 5 bullets or one short paragraph visible at once; 0–6 reveal steps per slide.
- Blank line before and after every block. Never indent normal text by 4 spaces.
- No free-standing HTML comments inside slides (a comment as the last block of a slide is printed as text).
  Only `<!-- TEMPLATE:BEGIN -->`, `<!-- TEMPLATE:END -->` and attribute comments such as `<!-- data-… -->` or `<!-- style="…" -->`.

## 4. Building blocks

| Element | Pattern |
|---|---|
| Image | `![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")`; size via `<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->` on the line above |
| Image beside text | `<div style="display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center;">` with two inner `<div style="flex:1 1 260px;">`, blank lines inside |
| Key message | `> [!NOTE] Key message` + `> %%KEY-MESSAGE%%` (also TIP, IMPORTANT, WARNING; one per slide unless the template is about phases) |
| Citation | `> %%QUOTE%%` / `>` / `> -- %%QUOTE-SOURCE%%` |
| Formula | `$$` on its own line, `%%FORMULA%%` (LaTeX), `$$` |
| Table that is not a chart | `<!-- data-type="none" -->` on the line above (otherwise LiaScript adds a chart button to numeric tables) |
| Instruction | bold verb + colon above every interaction: `**Try it:**`, `**Predict:**`, `**Decide:**`, `**Type:**`, `**Order:**`, `**Label:**` |
| Open-task hints | tiered `<details>` blocks with the summaries `💡 Hint 1`, `💡 Hint 2`, `✅ Solution`, blank lines inside |

## 5. Interaction patterns (all verified)

**Quiz attributes** (every quiz): `<!-- data-hint-button="1" data-solution-button="2" -->` – the hint bulb appears after one
wrong try, the "show solution" button after two.

**Single / multiple choice with feedback** – hints `[[?]]` after the options, then an optional solution block that is
shown once the quiz is solved or resolved:

```
<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%Q1-CORRECT%%
- [( )] %%Q1-WRONG-1%%
[[?]] %%Q1-HINT%%
***
%%Q1-FEEDBACK%%
***
```

**Text answer** (accepts any upper/lower case and surrounding spaces) – order: answer, hints, script, solution block.
A hint placed after the script is printed as raw text.

```
[[%%Q3-ANSWER%%]]
[[?]] %%Q3-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%Q3-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>
```

**Numeric answer with tolerance** (accepts a decimal comma):

```
[[%%RESULT-VALUE%%]]
[[?]] %%HINT-1%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%RESULT-VALUE%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
```

**Matrix quiz** (true/false series, classification A/B):

```
<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
[(true) (false)]
[  (X)    ( )  ] %%STATEMENT-1%%
[  ( )    (X)  ] %%STATEMENT-2%%
```

**Gap text** – selection `[[ a | (b) | c ]]`, typed `[[word]]` (exact spelling, prefer numbers), drag & drop
`[->[ (b) | c ]]`. All drag cards of one paragraph share a pool, so ordering and labelling tasks look like this
(do not start the line with `1.`, it becomes a list):

```
<!-- data-randomize data-show-partial-solution -->
Step 1: [->[ %%STEP-1%% ]] → Step 2: [->[ %%STEP-2%% ]] → Step 3: [->[ %%STEP-3%% ]]
```

**Surveys** (no right answer): vector `[(1)] Label`, multi-vector `[[a1]] Label`, matrix `[(none)(basic)(solid)]` +
rows `[                    ] %%ITEM%%`, text `[[___]]` (one line) or `[[___ ___ ___]]` (three lines).
**Task list** (ticks are saved in the learner's browser): `- [ ] %%CAN-DO-1%%`.

**Slider simulation** (no import) – model and ranges are content fields:

```
%%PARAM-1-LABEL%%: <script input="range" min="%%PARAM-1-MIN%%" max="%%PARAM-1-MAX%%" step="%%PARAM-1-STEP%%" value="%%PARAM-1-START%%" default="%%PARAM-1-START%%" output="p1" aria-label="%%PARAM-1-LABEL%%">@input</script>

<script>
const model = (p1, p2) => %%MODEL%%
const p1 = parseFloat(@input(`p1`))
"LIASCRIPT: **Result:** " + model(p1, 0).toFixed(1)
</script>
```

The `LIASCRIPT:` prefix renders the returned string as LiaScript (tables, bold, LaTeX, inline HTML such as a bar).

**Executable JavaScript** (no import) – the trailing `""` stops the viewer from printing `undefined`:

````
```js
%%JS-CODE%%
```
<script>
@input
""
</script>
````

**Executable Python**: import Pyodide 0.3.5, code block ` ```python ` followed directly by `@Pyodide.eval`.
The first run loads Python (a few seconds).

**Mermaid diagram**: import mermaid_template 0.1.4, code block ` ```mermaid @mermaid `. Labels in quotes, no quotes inside labels.

**Hotspot figure**: a `<div style="position:relative;display:inline-block;width:600px;max-width:100%;">` with the image
and numbered badges `<span style="position:absolute;left:X%;top:Y%;transform:translate(-50%,-50%);…">1</span>`.

**Video / external interactive**: `!?[%%VIDEO-ALT%%](%%VIDEO-URL%% "%%VIDEO-CAPTION%%")` (YouTube, Vimeo, files) or
`<iframe src="%%EMBED-URL%%" width="100%" height="480" style="border:0;" allowfullscreen title="%%EMBED-TITLE%%"></iframe>`
(PhET, GeoGebra, H5P) plus a link to open it in a new tab.

## 6. Imports (exact URLs, nothing else)

- Mermaid: `https://raw.githubusercontent.com/LiaTemplates/mermaid_template/0.1.4/README.md`
- Pyodide: `https://raw.githubusercontent.com/LiaTemplates/Pyodide/0.3.5/README.md`
  (versions 0.1.x load Python from the dead `pyodide-cdn2.iodide.io` – the whole course then hangs on "Loading").

`assemble.py build` puts only the imports of the templates actually used into the course header.

## 7. Checks

- `python3 validate.py` – structure, guide, placeholders ↔ guide, underscores, animation numbering and narration
  placement, text quizzes with answer script, hint order, imports ↔ macros.
- `node tools/render_check.mjs FILE.md …` – renders every slide in headless Chrome with the official viewer and reports
  rendered components, raw syntax visible on the slide, script errors and failed requests (setup: `cd tools && npm install`).
