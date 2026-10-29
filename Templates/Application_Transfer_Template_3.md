<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Think-Pair-Share discussion of a dilemma with an opinion vote before and after and an argument collection.
-->

# Template `Application_Transfer_Template_3`

- **Purpose:** Discuss an open question or dilemma in class. The two votes show whether the discussion changed opinions.
- **Pairs with:** `Introduction_Template_3`, `Concept_Explanation_Template_2`, `Summary_Recap_Template_3`
- **Variants:** Change the phase durations in the alert titles. For self-study delete the Pair phase (step 2) and renumber.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the discussion | max 6 words | Repair or Replace the Bridge? |
| `%%NARRATION-0%%` | Spoken dilemma | 2–3 sentences | The old bridge is a listed monument but too weak for modern trucks. |
| `%%DILEMMA%%` | Dilemma or open question | 2–3 sentences | The town must decide: reinforce the historic bridge or build a new one next to it. |
| `%%OPTION-A%%`, `%%OPTION-B%%` | The two positions | max 6 words | Reinforce the old bridge ; Build a new bridge |
| `%%NARRATION-1%%` … `%%NARRATION-3%%` | Spoken instruction per phase | 1 sentence | First, think alone for one minute. ; Now compare with your neighbour. ; Finally, we collect your arguments. |
| `%%THINK-TASK%%` | Task for thinking alone | 1 sentence | Note two arguments for your position. |
| `%%PAIR-TASK%%` | Task for pair work | 1 sentence | Compare your arguments with your neighbour and pick the strongest. |
| `%%SHARE-TASK%%` | Task for the plenary | 1 sentence | Each pair presents its strongest argument in one sentence. |
| `%%AFTER-TITLE%%` | Title of the second slide | max 5 words | What Do You Think Now? |
| `%%NARRATION-AFTER-0%%` | Spoken intro to the second vote | 1 sentence | Vote again – did the discussion change your mind? |
| `%%NARRATION-AFTER-1%%` | Spoken intro to the arguments | 1 sentence | Which argument convinced you most? |

**Note:** both votes reuse `%%OPTION-A%%` and `%%OPTION-B%%`.

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%DILEMMA%%

**Vote (before):** What is your position?

[(a)] %%OPTION-A%%
[(b)] %%OPTION-B%%
[(undecided)] Undecided

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!TIP] 🧠 Think · 1 min
> %%THINK-TASK%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!TIP] 👥 Pair · 3 min
> %%PAIR-TASK%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
> [!TIP] 📣 Share · 5 min
> %%SHARE-TASK%%

## %%AFTER-TITLE%%

    --{{0}}--
%%NARRATION-AFTER-0%%

**Vote (after):** What is your position now?

[(a)] %%OPTION-A%%
[(b)] %%OPTION-B%%
[(undecided)] Undecided

    --{{1}}--
%%NARRATION-AFTER-1%%

      {{1}}
****************************************

**Share:** Which argument convinced you most?

[[___ ___]]

****************************************

<!-- TEMPLATE:END -->
