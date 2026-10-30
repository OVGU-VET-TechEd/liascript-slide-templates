<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Calculation task with a data table, a tolerance-checked numeric answer and a reflection survey.
-->

# Template `Interactive_Exercise_Template_3`

- **Purpose:** Let learners apply a formula to concrete given values and check a numeric result with a tolerance.
- **Pairs with:** `Interactive_Exercise_Template_1`, `Interactive_Exercise_Template_2`, `Concept_Explanation_Template_1`
- **Variants:** Replace the data table with an image of the setup. Use a three-line survey `[[___ ___ ___]]` for a longer reflection.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the calculation task | max 6 words | Energy in a Charging Capacitor |
| `%%NARRATION-0%%` | Spoken intro to the task | 1–2 sentences | Now let us apply the formula to a real flash capacitor. |
| `%%TASK-CONTEXT%%` | Situation the task lives in | 2–3 sentences | A camera flash charges a capacitor to 12 V before it fires. |
| `%%KEY-MESSAGE%%` | Unit or method reminder | 1 sentence | Convert all units to the base system before you calculate. |
| `%%NARRATION-1%%` | Spoken intro to the data table | 1 sentence | Here are the values you may use. |
| `%%GIVEN-1-NAME%%` | Name of a given quantity | max 6 words | Capacitance C |
| `%%GIVEN-1-VALUE%%` | Value with unit | max 6 words | 200 µF |
| `%%GIVEN-2-NAME%%` | Name of a given quantity | max 6 words | Voltage U |
| `%%GIVEN-2-VALUE%%` | Value with unit | max 6 words | 12 V |
| `%%GIVEN-3-NAME%%` | Name of the unknown quantity | max 6 words | Energy E |
| `%%GIVEN-3-VALUE%%` | Mark for the unknown | max 6 words | to be calculated |
| `%%NARRATION-2%%` | Spoken intro to the question | 1 sentence | Compute the stored energy in millijoules. |
| `%%QUESTION%%` | The calculation question | 1 sentence | How much energy is stored in the capacitor, in millijoules? |
| `%%ANSWER-VALUE%%` | Correct number, no unit | number | 14.4 |
| `%%HINT-1%%` | First hint | 1 sentence | Use E = ½ · C · U² and convert microfarads to farads first. |
| `%%HINT-2%%` | Second hint | 1 sentence | 200 µF is 0.0002 F, so E = 0.5 × 0.0002 × 144. |
| `%%SOLUTION-TEXT%%` | Full worked solution | 1–2 sentences | E = ½ · 0.0002 F · (12 V)² = 0.0144 J = 14.4 mJ. |
| `%%REFLECT-TITLE%%` | Title of the reflection slide | max 6 words | Reflect on Your Approach |
| `%%NARRATION-REFLECT-0%%` | Spoken intro to the reflection | 1 sentence | Before we move on, take a moment to look back. |
| `%%REFLECT-TEXT%%` | Written context for the reflection | 1–2 sentences | Trusting your result matters as much as computing it. |
| `%%NARRATION-REFLECT-1%%` | Spoken intro to the survey | 1 sentence | Answer in a single honest sentence. |
| `%%REFLECT-QUESTION%%` | Reflection question | 1 sentence | Which step of your calculation felt least certain, and why? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%TASK-CONTEXT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

<!-- data-type="none" -->
| Quantity | Value |
|---|---|
| %%GIVEN-1-NAME%% | %%GIVEN-1-VALUE%% |
| %%GIVEN-2-NAME%% | %%GIVEN-2-VALUE%% |
| %%GIVEN-3-NAME%% | %%GIVEN-3-VALUE%% |

> [!NOTE] Key message
> %%KEY-MESSAGE%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Calculate:** %%QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%ANSWER-VALUE%%]]
[[?]] %%HINT-1%%
[[?]] %%HINT-2%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%ANSWER-VALUE%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%SOLUTION-TEXT%%
***

****************************************

## %%REFLECT-TITLE%%

    --{{0}}--
%%NARRATION-REFLECT-0%%

%%REFLECT-TEXT%%

    --{{1}}--
%%NARRATION-REFLECT-1%%

      {{1}}
****************************************

**Type:** %%REFLECT-QUESTION%%

[[___]]

****************************************

<!-- TEMPLATE:END -->
