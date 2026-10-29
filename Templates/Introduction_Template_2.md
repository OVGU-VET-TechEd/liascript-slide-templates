<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Opening slide with bullet points only (who, what, why, how) and a one-word association survey.
-->

# Template `Introduction_Template_2`

- **Purpose:** Lean opening without images. Four bullets appear one after another, then every learner names one association.
- **Pairs with:** `Overview_Course_Template_1`, `Overview_Course_Template_2`, `Content_Introduction_Template_2`
- **Variants:** Show all bullets at once by deleting the reveal lines of steps 2–4 and their narrations. Delete step 5 to skip the survey.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Course or session title | max 6 words | Project Management Basics |
| `%%SUBTITLE%%` | One-line subtitle | max 10 words | Session 1 · Winter term 2026 |
| `%%NARRATION-0%%` | Spoken welcome | 1–2 sentences | Welcome. Let me tell you in four points what this course is about. |
| `%%NARRATION-1%%` | Spoken text on "who" | 1–2 sentences | First, who we are. |
| `%%WHO%%` | Who teaches, who learns | max 12 words | Dr. A. Example with 2nd-year engineering students |
| `%%NARRATION-2%%` | Spoken text on "what" | 1–2 sentences | Second, what we cover. |
| `%%WHAT%%` | Topic of the course | max 12 words | Planning, steering and closing technical projects |
| `%%NARRATION-3%%` | Spoken text on "why" | 1–2 sentences | Third, why it matters to you. |
| `%%WHY%%` | Relevance for learners | max 12 words | Most engineering work is organised in projects |
| `%%NARRATION-4%%` | Spoken text on "how" | 1–2 sentences | And fourth, how we work together. |
| `%%HOW%%` | Format and method | max 12 words | Short inputs, case work, weekly self-checks |
| `%%NARRATION-5%%` | Spoken intro to the survey | 1 sentence | Now it is your turn. |
| `%%TOPIC%%` | Topic named in the survey | max 5 words | project management |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

*%%SUBTITLE%%*

    --{{1}}--
%%NARRATION-1%%

      {{1}}
- **Who:** %%WHO%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
- **What:** %%WHAT%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
- **Why:** %%WHY%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
- **How:** %%HOW%%

    --{{5}}--
%%NARRATION-5%%

      {{5}}
****************************************

**Share:** Which single word comes to mind when you hear "%%TOPIC%%"?

[[___]]

****************************************

<!-- TEMPLATE:END -->
