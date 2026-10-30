<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Course overview with a module table, an assessment note and four learning objectives.
-->

# Template `Overview_Course_Template_1`

- **Purpose:** Give learners a one-page map of the whole course: modules, formats, assessment and the four things they will be able to do.
- **Pairs with:** `Introduction_Template_3`, `Overview_Course_Template_2`
- **Variants:** Replace the module table with one bullet line per module if the table feels too dense. Move the survey to slide 1 if the objectives should close the session.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the module overview slide | max 6 words | The Road To Your Data Story |
| `%%NARRATION-0%%` | Spoken intro to the module table | 2–3 sentences | Over the next eight weeks we build one data story from raw tables to a five-minute presentation. |
| `%%MODULE-1%%` … `%%MODULE-4%%` | Module names | max 4 words | Data Cleaning ; Story Design ; Chart Making ; Presentation |
| `%%FORMAT-1%%` … `%%FORMAT-4%%` | Teaching format of the module | max 2 words | Lecture ; Workshop ; Lab ; Studio |
| `%%DURATION-1%%` … `%%DURATION-4%%` | Duration of the module | max 3 words | 2 sessions ; 3 sessions ; 4 sessions ; 2 sessions |
| `%%NARRATION-1%%` | Spoken intro to the assessment note | 1–2 sentences | Here is how your work will be counted. |
| `%%ASSESSMENT-TEXT%%` | How the course is assessed | 1–2 sentences | The final data story counts 40 % written analysis and 60 % five-minute presentation. |
| `%%OBJ-TITLE%%` | Title of the objectives slide | max 6 words | What You Will Be Able To Do |
| `%%NARRATION-OBJ-0%%` | Spoken intro to the objectives | 1–2 sentences | Let me make the goal concrete: four things you will be able to do. |
| `%%OBJ-1%%` … `%%OBJ-4%%` | Objective with a bold Bloom verb | 1 sentence | **Analyse** a raw dataset and pick the strongest story ; **Design** a story arc with one message per chart ; **Build** four chart types in Python ; **Present** the story to a non-technical audience |
| `%%NARRATION-OBJ-1%%` … `%%NARRATION-OBJ-4%%` | Spoken line for one objective | 1 sentence | First, you will learn to choose the variables that carry the story. ; Second, you will shape a story arc before touching any chart. ; Third, you will build the charts in Python. ; And finally, you will tell the story out loud. |
| `%%NARRATION-OBJ-5%%` | Spoken intro to the survey | 1 sentence | Tell me where your curiosity points. |
| `%%SURVEY-QUESTION%%` | Survey question | 1 sentence | Which modules interest you? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- data-type="none" -->
| No | Module | Format | Duration |
|---|---|---|---|
| 1 | %%MODULE-1%% | %%FORMAT-1%% | %%DURATION-1%% |
| 2 | %%MODULE-2%% | %%FORMAT-2%% | %%DURATION-2%% |
| 3 | %%MODULE-3%% | %%FORMAT-3%% | %%DURATION-3%% |
| 4 | %%MODULE-4%% | %%FORMAT-4%% | %%DURATION-4%% |

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!NOTE] How you are assessed
> %%ASSESSMENT-TEXT%%

## %%OBJ-TITLE%%

    --{{0}}--
%%NARRATION-OBJ-0%%

By the end of the course you will be able to:

    --{{1}}--
%%NARRATION-OBJ-1%%

      {{1}}
- %%OBJ-1%%

    --{{2}}--
%%NARRATION-OBJ-2%%

      {{2}}
- %%OBJ-2%%

    --{{3}}--
%%NARRATION-OBJ-3%%

      {{3}}
- %%OBJ-3%%

    --{{4}}--
%%NARRATION-OBJ-4%%

      {{4}}
- %%OBJ-4%%

    --{{5}}--
%%NARRATION-OBJ-5%%

      {{5}}
****************************************

**Decide:** %%SURVEY-QUESTION%%

[[m1]] %%MODULE-1%%
[[m2]] %%MODULE-2%%
[[m3]] %%MODULE-3%%
[[m4]] %%MODULE-4%%

****************************************

<!-- TEMPLATE:END -->
