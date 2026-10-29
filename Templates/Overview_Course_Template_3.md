<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Learner-centred overview with objectives, workload box and a prior-knowledge matrix survey.
-->

# Template `Overview_Course_Template_3`

- **Purpose:** Present the objectives from the learner's view and collect prior knowledge and expectations per objective.
- **Pairs with:** `Introduction_Template_1`, `Introduction_Template_3`, `Summary_Recap_Template_3`
- **Variants:** Use slide 1 alone as a compact overview. Repeat the matrix in `Summary_Recap_Template_3` to make progress visible.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the objectives slide | max 5 words | What's in It for You |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | Let me show you what you will be able to do at the end. |
| `%%OBJECTIVE-1%%` … `%%OBJECTIVE-3%%` | Objective in "you can" form | max 12 words | read a technical drawing without help ; size a simple component ; present a design decision |
| `%%NARRATION-1%%` | Spoken comment on the workload | 1–2 sentences | And here is what it takes. |
| `%%WORKLOAD%%` | Time per week | 1 sentence | About 4 hours per week: 2 in class, 2 for self-study. |
| `%%ASSESSMENT%%` | Assessment format | 1 sentence | A 20-minute oral exam on a case you choose. |
| `%%CHECK-TITLE%%` | Title of the survey slide | max 5 words | Where Do You Start? |
| `%%NARRATION-CHECK-0%%` | Spoken intro to the matrix | 1–2 sentences | Rate your prior knowledge for each objective. There are no wrong answers. |
| `%%NARRATION-CHECK-1%%` | Spoken intro to the expectations | 1 sentence | And what do you expect from this course? |

**Note:** the matrix survey reuses `%%OBJECTIVE-1%%` … `%%OBJECTIVE-3%%`.

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**By the end you can …**

- ✅ %%OBJECTIVE-1%%
- ✅ %%OBJECTIVE-2%%
- ✅ %%OBJECTIVE-3%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!TIP] What it takes
> **Workload:** %%WORKLOAD%%
>
> **Assessment:** %%ASSESSMENT%%

## %%CHECK-TITLE%%

    --{{0}}--
%%NARRATION-CHECK-0%%

**Rate yourself:** How much do you already know?

[(none)(basic)(solid)]
[                    ] %%OBJECTIVE-1%%
[                    ] %%OBJECTIVE-2%%
[                    ] %%OBJECTIVE-3%%

    --{{1}}--
%%NARRATION-CHECK-1%%

      {{1}}
****************************************

**Share:** What do you expect from this course?

[[___ ___ ___]]

****************************************

<!-- TEMPLATE:END -->
