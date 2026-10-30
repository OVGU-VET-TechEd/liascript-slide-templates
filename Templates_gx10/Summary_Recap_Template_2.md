<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Exit ticket with one quiz per session objective, each question naming its objective.
-->

# Template `Summary_Recap_Template_2`

- **Purpose:** Close a session as an exit ticket: one short quiz per session objective, with the objective named inside each question.
- **Pairs with:** `Summary_Recap_Template_1`, `Summary_Recap_Template_3`
- **Variants:** Swap the quiz type of any objective (e.g. text answer instead of numeric). Add a fourth objective by copying the question pattern with `%%OBJ-4%%` and `%%Q4-…%%` fields.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of both slides | max 6 words | Exit Ticket – Heat Transfer Basics |
| `%%NARRATION-0%%` | Spoken intro to the ticket | 2–3 sentences | Before we finish, let us check the three objectives of today. |
| `%%NARRATION-1%%` | Spoken intro to slide 2 | 1–2 sentences | One last question for objective three. |
| `%%OBJ-1%%` | Session objective 1 | 1 sentence | Explain how heat moves between two bodies |
| `%%OBJ-2%%` | Session objective 2 | 1 sentence | Compare the factors that control heat loss |
| `%%OBJ-3%%` | Session objective 3 | 1 sentence | Calculate the total heat loss of a wall |
| `%%Q1-QUESTION%%` | Question for objective 1 | 1–2 sentences | Two objects at different temperatures are placed in contact. What happens next? |
| `%%Q1-CORRECT%%` | Correct option | max 10 words | Heat flows from hot to cold until both reach the same temperature |
| `%%Q1-WRONG-1%%` | Plausible wrong option | max 10 words | Heat flows from cold to hot until both cool down |
| `%%Q1-WRONG-2%%` | Plausible wrong option | max 10 words | The temperatures stay constant and no energy moves |
| `%%Q1-HINT%%` | Hint | 1 sentence | Energy never flows on its own from the colder side to the hotter one. |
| `%%Q1-FEEDBACK%%` | Feedback after answering | 1 sentence | Correct – objective 1 is to name this spontaneous flow and the final equilibrium. |
| `%%Q2-QUESTION%%` | Question for objective 2 | 1–2 sentences | Which factors make a wall lose heat faster? |
| `%%Q2-CORRECT-1%%` … `%%Q2-CORRECT-2%%` | Correct options | max 10 words each | A larger surface area ; A thinner insulation layer |
| `%%Q2-WRONG-1%%` | Plausible wrong option | max 10 words | The colour of the paint |
| `%%Q2-WRONG-2%%` | Plausible wrong option | max 10 words | The day of the week |
| `%%Q2-HINT%%` | Hint | 1 sentence | Think of a window: what lets more energy cross the boundary? |
| `%%Q2-FEEDBACK%%` | Feedback after answering | 1 sentence | Correct – objective 2 is to compare area, thickness and material of the insulation. |
| `%%Q3-QUESTION%%` | Question for objective 3 | 1–2 sentences | A wall loses 2.5 kW over 6 hours. How many kWh does it lose in total? |
| `%%Q3-ANSWER%%` | Numeric answer | no quotes, backticks or backslashes | 15.0 |
| `%%Q3-HINT%%` | Hint | 1 sentence | Multiply the power in kilowatts by the time in hours. |
| `%%Q3-FEEDBACK%%` | Feedback after answering | 1 sentence | Correct – objective 3 is to convert power and time into energy in kWh. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!NOTE] Exit ticket
> Three objectives, three quick questions. You may use the hint bulb and the solution button.

**Objective 1:** %%OBJ-1%%

**Decide:** %%Q1-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%Q1-CORRECT%%
- [( )] %%Q1-WRONG-1%%
- [( )] %%Q1-WRONG-2%%
[[?]] %%Q1-HINT%%
***
%%Q1-FEEDBACK%%
***

**Objective 2:** %%OBJ-2%%

**Decide:** %%Q2-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%Q2-CORRECT-1%%
- [(X)] %%Q2-CORRECT-2%%
- [( )] %%Q2-WRONG-1%%
- [( )] %%Q2-WRONG-2%%
[[?]] %%Q2-HINT%%
***
%%Q2-FEEDBACK%%
***

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-1%%

**Objective 3:** %%OBJ-3%%

**Type:** %%Q3-QUESTION%%

[[%%Q3-ANSWER%%]]
[[?]] %%Q3-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%Q3-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%Q3-FEEDBACK%%
***

<!-- TEMPLATE:END -->
