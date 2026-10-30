<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Course overview with three objectives and a workload tip, then a self-assessment survey.
-->

# Template `Overview_Course_Template_3`

- **Purpose:** Open a course by naming three concrete "by the end you can" objectives and let learners rate their starting level.
- **Pairs with:** `Overview_Course_Template_1`, `Overview_Course_Template_2`, `Introduction_Template_1`
- **Variants:** Replace the self-assessment matrix with a task list `- [ ]` of can-do statements. Add a fourth objective as another matrix row.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the overview slide | max 6 words | Where This Course Takes You |
| `%%NARRATION-0%%` | Spoken welcome and course name | 2–3 sentences | Welcome to Data Storytelling with Python. In the next twelve weeks we turn raw numbers into clear pictures and confident presenters. |
| `%%OBJ-1%%` … `%%OBJ-3%%` | Learning objective, starts with a verb | max 12 words | build a bar chart from raw data ; choose the right chart type for a question ; present a data story to a non-technical audience |
| `%%NARRATION-1%%` | Spoken pointer to the workload tip | 1 sentence | And here is what the workload and the assessment look like. |
| `%%TIP-TEXT%%` | Workload and assessment in one line | 2 sentences | Plan for 6 hours per week. Assessment is one project and two short quizzes. |
| `%%EX-TITLE%%` | Title of the self-assessment slide | max 6 words | Rate Yourself Before We Start |
| `%%EX-NARRATION-0%%` | Spoken intro to the self-assessment | 1–2 sentences | Before we start, I would like to know where you stand. |
| `%%EX-NARRATION-1%%` | Spoken intro to the rating matrix and the expectations question | 1–2 sentences | Let us start with a quick self-check on the three objectives, and tell me what you hope to take away. |
| `%%EX-NARRATION-2%%` | Spoken pointer to the note | 1 sentence | Your ratings help us adjust the pace – there are no wrong answers here. |
| `%%EXPECTATIONS-QUESTION%%` | Question above the text survey | 1 sentence | What do you hope to learn in this course? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**By the end of this course, you can:**

- **%%OBJ-1%%**
- **%%OBJ-2%%**
- **%%OBJ-3%%**

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!TIP] Workload and assessment
> %%TIP-TEXT%%

## %%EX-TITLE%%

    --{{0}}--
%%EX-NARRATION-0%%

    --{{1}}--
%%EX-NARRATION-1%%

      {{1}}
****************************************

**Rate yourself:** How confident do you feel about each objective right now?

[(none)(basic)(solid)]
[                    ] %%OBJ-1%%
[                    ] %%OBJ-2%%
[                    ] %%OBJ-3%%

**Tell us:** %%EXPECTATIONS-QUESTION%%

[[___]]

****************************************

    --{{2}}--
%%EX-NARRATION-2%%

      {{2}}
> [!NOTE] Why we ask
> Your ratings help us adjust the pace. There are no wrong answers here.

<!-- TEMPLATE:END -->
