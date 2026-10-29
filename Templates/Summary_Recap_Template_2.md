<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Exit ticket with three mixed quiz items, one per session objective.
-->

# Template `Summary_Recap_Template_2`

- **Purpose:** Short exit ticket at the end of a session. One question per objective from the overview slide.
- **Pairs with:** `Overview_Course_Template_1`, `Overview_Course_Template_3`, `Interactive_Exercise_Template_2`
- **Variants:** Show all three questions at once by deleting the reveal lines and narrations of steps 1 and 2.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 5 words | Exit Ticket |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | Before you leave, answer three short questions. |
| `%%OBJECTIVE-1%%` … `%%OBJECTIVE-3%%` | Objective tested, short | max 5 words | Explain hydrostatic pressure ; Use pressure units ; Calculate pressure at depth |
| `%%Q1-QUESTION%%` | Single-choice question | 1 sentence | What does the pressure in a resting liquid depend on? |
| `%%Q1-CORRECT%%` | Correct option | max 10 words | The depth below the surface |
| `%%Q1-WRONG-1%%`, `%%Q1-WRONG-2%%` | Wrong options | max 10 words | The shape of the vessel ; The area of the surface |
| `%%Q1-HINT%%` | Hint | 1 sentence | Think of a diver going deeper. |
| `%%NARRATION-1%%` | Spoken intro to question 2 | 1 sentence | Second question – several answers can be right. |
| `%%Q2-QUESTION%%` | Multiple-choice question | 1 sentence | Which units can express a pressure? |
| `%%Q2-CORRECT-1%%`, `%%Q2-CORRECT-2%%` | Correct options | max 10 words | Pa ; N/m² |
| `%%Q2-WRONG-1%%` | Wrong option | max 10 words | J |
| `%%Q2-HINT%%` | Hint | 1 sentence | Pressure is force per area. |
| `%%NARRATION-2%%` | Spoken intro to question 3 | 1 sentence | And finally, calculate. |
| `%%Q3-QUESTION%%` | Numeric question with unit | 1 sentence | Water pressure at 10 m depth in kPa? |
| `%%Q3-ANSWER%%` | Numeric answer, dot as decimal sign | number | 98.1 |
| `%%Q3-HINT%%` | Hint | 1 sentence | p = ρ · g · h with ρ = 1000 kg/m³. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**🎟️ 1 · %%OBJECTIVE-1%%** – %%Q1-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%Q1-CORRECT%%
- [( )] %%Q1-WRONG-1%%
- [( )] %%Q1-WRONG-2%%
[[?]] %%Q1-HINT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**🎟️ 2 · %%OBJECTIVE-2%%** – %%Q2-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [[X]] %%Q2-CORRECT-1%%
- [[ ]] %%Q2-WRONG-1%%
- [[X]] %%Q2-CORRECT-2%%
[[?]] %%Q2-HINT%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**🎟️ 3 · %%OBJECTIVE-3%%** – %%Q3-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%Q3-ANSWER%%]]
[[?]] %%Q3-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%Q3-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>

****************************************

<!-- TEMPLATE:END -->
