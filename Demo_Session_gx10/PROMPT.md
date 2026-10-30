<!-- gx10 out=demo/Demo_Session_gx10.md dest=Demo_Session_gx10/Demo_Session_gx10.md -->
# AUTOPILOT – demo session from the gx10 templates

Read `inputs/rahmen.md` first. Then look at the templates in `gx10_templates/` (start with `list_dir`).

## Task

Create ONE complete LiaScript demo session in `demo/Demo_Session_gx10.md` with `write_file`.

- Topic: "Air Pressure – Otto von Guericke's Hemispheres" (Magdeburg hemispheres experiment, air pressure, p = F/A,
  force on the hemispheres, measuring air pressure). Audience: first-year university students. Language: English.
- Use 8 to 11 different templates from `gx10_templates/`, in a sensible teaching order (introduction, overview,
  content, explanation, practice, simulation or media, application, summary).
- For each template copy ONLY the part between `<!-- TEMPLATE:BEGIN -->` and `<!-- TEMPLATE:END -->` and replace
  EVERY `%%PLACEHOLDER%%` with concrete content on the topic. Keep the structure, quiz syntax and scripts unchanged.
- Start the file with one course header (rahmen.md section 2, with author "gx10 demo", mode Presentation) and one
  `# ` title line. Add to `import:` only the imports needed by the templates you used.
- Facts and numbers must be correct and consistent (quiz answers must match calculations). If unsure, choose simpler content.
- Do not use images that you cannot be sure exist; prefer text, tables, formulas and diagrams.

## Finish

Re-read the file: no `%%` left, every slide has narration, quiz answers match. Fix with `edit_file`.
Then write `agent_report.md` (max 10 lines): templates used, open doubts.
