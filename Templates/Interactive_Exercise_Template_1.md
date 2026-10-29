<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Self-check slide with a single-choice, a multiple-choice and a text quiz, each with hint and feedback.
-->

# Template `Interactive_Exercise_Template_1`

- **Purpose:** Quick knowledge check after an explanation. Three quiz types, one question each, revealed one by one.
- **Pairs with:** `Concept_Explanation_Template_1`, `Concept_Explanation_Template_2`, `Summary_Recap_Template_1`
- **Variants:** Copy a quiz block to add questions (keep one quiz per step). Delete a feedback block (`***` … `***`) if no feedback is needed.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 5 words | Check Yourself |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | Three short questions. You can try as often as you like. |
| `%%Q1-QUESTION%%` | Single-choice question | 1 sentence | Which unit measures pressure? |
| `%%Q1-CORRECT%%` | Correct option | max 10 words | Pascal |
| `%%Q1-WRONG-1%%`, `%%Q1-WRONG-2%%` | Wrong options | max 10 words | Newton ; Joule |
| `%%Q1-HINT%%` | Hint | 1 sentence | Pressure is force per area. |
| `%%Q1-FEEDBACK%%` | Feedback after solving | 1 sentence | 1 Pa = 1 N/m². |
| `%%NARRATION-1%%` | Spoken intro to question 2 | 1 sentence | Now more than one answer can be right. |
| `%%Q2-QUESTION%%` | Multiple-choice question | 1 sentence | On which quantities does hydrostatic pressure depend? |
| `%%Q2-CORRECT-1%%`, `%%Q2-CORRECT-2%%` | Correct options | max 10 words | Depth ; Density of the fluid |
| `%%Q2-WRONG-1%%`, `%%Q2-WRONG-2%%` | Wrong options | max 10 words | Shape of the vessel ; Area of the water surface |
| `%%Q2-HINT%%` | Hint | 1 sentence | Look at the formula p = ρ · g · h. |
| `%%Q2-FEEDBACK%%` | Feedback after solving | 1 sentence | Only density, gravity and depth appear in the formula. |
| `%%NARRATION-2%%` | Spoken intro to question 3 | 1 sentence | Finally, type the answer. |
| `%%Q3-QUESTION%%` | Text question | 1 sentence | Which Greek letter stands for density? |
| `%%Q3-ANSWER%%` | Expected answer, case does not matter | 1–2 words | rho |
| `%%Q3-HINT%%` | Hint | 1 sentence | It looks like a p. |
| `%%Q3-FEEDBACK%%` | Feedback after solving | 1 sentence | ρ (rho) is the usual symbol for density. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**1 · Choose one:** %%Q1-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] %%Q1-WRONG-1%%
- [(X)] %%Q1-CORRECT%%
- [( )] %%Q1-WRONG-2%%
[[?]] %%Q1-HINT%%
***
%%Q1-FEEDBACK%%
***

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**2 · Choose all that apply:** %%Q2-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [[X]] %%Q2-CORRECT-1%%
- [[ ]] %%Q2-WRONG-1%%
- [[X]] %%Q2-CORRECT-2%%
- [[ ]] %%Q2-WRONG-2%%
[[?]] %%Q2-HINT%%
***
%%Q2-FEEDBACK%%
***

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**3 · Type:** %%Q3-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%Q3-ANSWER%%]]
[[?]] %%Q3-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%Q3-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>
***
%%Q3-FEEDBACK%%
***

****************************************

<!-- TEMPLATE:END -->
