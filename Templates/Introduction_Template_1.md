<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Opening slide with a large title image, welcome text, agenda and a prior-knowledge survey.
-->

# Template `Introduction_Template_1`

- **Purpose:** First slide of a course or session. Welcomes learners with an image and checks prior knowledge.
- **Pairs with:** `Overview_Course_Template_1`, `Overview_Course_Template_3`, `Content_Introduction_Template_1`
- **Variants:** Delete step 2 (survey) for a pure welcome slide. Delete the image line for a text-only opening.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Course or session title | max 6 words | Fluid Mechanics – Session 1 |
| `%%NARRATION-0%%` | Spoken welcome | 2–3 sentences | Welcome to fluid mechanics. Today we find out why water pushes back. |
| `%%IMAGE-PATH%%` | Path or URL of the title image | landscape image | assets/images/cover.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Water flowing around a bridge pillar |
| `%%IMAGE-CAPTION%%` | Caption or image credit | max 10 words | Photo: J. Doe, CC BY 4.0 |
| `%%WELCOME-TEXT%%` | Welcome paragraph | 2–3 sentences | Fluids are everywhere: in pipes, rivers and our blood. In this course you learn to describe and calculate them. |
| `%%SPEAKER-INFO%%` | Lecturer name, role, contact | max 12 words | Dr. A. Example · Institute of Mechanics |
| `%%NARRATION-1%%` | Spoken intro to the agenda | 1–2 sentences | Here is what you will do today. |
| `%%AGENDA-1%%` … `%%AGENDA-3%%` | Goal of today | max 10 words | name the key properties of fluids ; calculate hydrostatic pressure ; apply it to a dam wall |
| `%%NARRATION-2%%` | Spoken intro to the survey | 1–2 sentences | Before we start, tell me where you stand. |
| `%%TOPIC%%` | Topic named in the survey | max 5 words | fluid mechanics |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- style="max-width:100%;width:70%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

%%WELCOME-TEXT%%

*%%SPEAKER-INFO%%*

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Today you will:**

- %%AGENDA-1%%
- %%AGENDA-2%%
- %%AGENDA-3%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Rate yourself:** How familiar are you with %%TOPIC%%?

[(1)] New to me
[(2)] I have heard of it
[(3)] I have used it before
[(4)] I am confident with it

****************************************

<!-- TEMPLATE:END -->
