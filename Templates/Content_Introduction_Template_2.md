<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Start of a content block with a guiding question, four bullets revealed step by step and a prior-knowledge survey.
-->

# Template `Content_Introduction_Template_2`

- **Purpose:** Text-only opener for a new topic. A guiding question frames four aspects the block will cover.
- **Pairs with:** `Overview_Course_Template_2`, `Concept_Explanation_Template_2`, `Interactive_Exercise_Template_1`
- **Variants:** Show all bullets at once by deleting the reveal lines of steps 2–4 and their narrations. Replace the TIP alert with an image.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Topic of the new block | max 6 words | Risk Management |
| `%%NARRATION-0%%` | Spoken intro with the question | 1–2 sentences | Projects fail for many reasons. Can we see them coming? |
| `%%GUIDING-QUESTION%%` | Guiding question | 1 sentence | How can we spot project risks early? |
| `%%NARRATION-1%%` … `%%NARRATION-4%%` | Spoken comment per aspect | 1 sentence | First, we identify risks systematically. ; Then we rate how likely and how severe they are. ; Next, we plan countermeasures. ; Finally, we keep watching them during the project. |
| `%%ASPECT-1%%` … `%%ASPECT-4%%` | Aspect the block covers | max 10 words | Identify risks with a checklist ; Rate probability and impact ; Plan countermeasures ; Monitor risks during the project |
| `%%NARRATION-5%%` | Spoken reason why this matters | 1 sentence | Why should you care? |
| `%%WHY-IT-MATTERS%%` | Relevance for learners | 1–2 sentences | Most failed projects had warning signs that nobody acted on. |
| `%%NARRATION-6%%` | Spoken intro to the survey | 1 sentence | Tell me what you already know. |

**Note:** the survey reuses `%%ASPECT-1%%` … `%%ASPECT-4%%`.

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**%%GUIDING-QUESTION%%**

    --{{1}}--
%%NARRATION-1%%

      {{1}}
- %%ASPECT-1%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
- %%ASPECT-2%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
- %%ASPECT-3%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
- %%ASPECT-4%%

    --{{5}}--
%%NARRATION-5%%

      {{5}}
> [!TIP] Why this matters
> %%WHY-IT-MATTERS%%

    --{{6}}--
%%NARRATION-6%%

      {{6}}
****************************************

**Mark:** Which of these do you already know? (several possible)

[[a1]] %%ASPECT-1%%
[[a2]] %%ASPECT-2%%
[[a3]] %%ASPECT-3%%
[[a4]] %%ASPECT-4%%

****************************************

<!-- TEMPLATE:END -->
