<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Opening slide that presents the course in four short bullets and ends with a one-word association survey.
-->

# Template `Introduction_Template_2`

- **Purpose:** Open a course by presenting it in four short bullets (Who, What, Why, How) revealed one per step and ending with a one-word association survey.
- **Pairs with:** `Introduction_Template_1`, `Introduction_Template_3`, `Overview_Course_Template_1`
- **Variants:** Reduce to three bullets (Who / What / When) and delete one reveal step. Add a NOTE key-message box after the How step.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the course | max 6 words | Introduction to Climate Models |
| `%%SUBTITLE%%` | One-line subtitle | max 15 words | How our climate works and what we can do about it |
| `%%NARRATION-0%%` | Spoken welcome | 1–2 sentences | Welcome to the course. Let me start with what this course is about and who it is for. |
| `%%WHO%%` | Who the course is for | max 12 words | Environmental science students in years one to three |
| `%%NARRATION-1%%` | Spoken intro to Who | 1 sentence | First, who this course is for. |
| `%%WHAT%%` | What learners will learn | max 12 words | The basics of climate systems and simple models |
| `%%NARRATION-2%%` | Spoken intro to What | 1 sentence | Next, what you will learn. |
| `%%WHY%%` | Why the topic matters | max 12 words | To understand the causes of climate change |
| `%%NARRATION-3%%` | Spoken intro to Why | 1 sentence | Then why it matters to you. |
| `%%HOW%%` | How the course runs | max 12 words | Interactive lessons, exercises, and a final project |
| `%%NARRATION-4%%` | Spoken intro to How | 1 sentence | And finally, how the course will run. |
| `%%NARRATION-5%%` | Spoken intro to the survey | 1 sentence | Let me end with a quick question for you. |
| `%%SURVEY-QUESTION%%` | One-word association prompt | max 15 words | one word you associate with climate models |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%SUBTITLE%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
**Who:** %%WHO%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
**What:** %%WHAT%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
**Why:** %%WHY%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
**How:** %%HOW%%

    --{{5}}--
%%NARRATION-5%%

      {{5}}
****************************************

**Associate:** %%SURVEY-QUESTION%%

[[___]]

****************************************

<!-- TEMPLATE:END -->
