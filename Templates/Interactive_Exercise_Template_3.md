<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Calculation task with given values, a numeric answer check with tolerance, tiered hints, a worked solution and a reflection.
-->

# Template `Interactive_Exercise_Template_3`

- **Purpose:** Practise a calculation. Rounding differences and a decimal comma are accepted, hints appear after a wrong try.
- **Pairs with:** `Concept_Explanation_Template_1`, `Simulation_Template_1`, `Application_Transfer_Template_2`
- **Variants:** Change the tolerance in the script line marked ADAPT (0.02 = 2 %). Add rows to the table of given values. Delete step 1 to skip the reflection.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the task | max 5 words | Pressure on a Dam |
| `%%NARRATION-0%%` | Spoken task context | 1–2 sentences | A dam holds back a lake that is forty metres deep. |
| `%%TASK-CONTEXT%%` | Situation | 1–2 sentences | A dam holds back a reservoir with a water depth of 40 m. |
| `%%GIVEN-1%%` … `%%GIVEN-3%%` | Name of a given quantity | max 4 words | Water depth h ; Density of water ρ ; Gravitational acceleration g |
| `%%VALUE-1%%` … `%%VALUE-3%%` | Value with unit | short | 40 m ; 1000 kg/m³ ; 9.81 m/s² |
| `%%TASK-QUESTION%%` | What to calculate | 1 sentence | Find the water pressure at the base of the dam. |
| `%%RESULT-VALUE%%` | Numeric result, dot as decimal sign | number | 392.4 |
| `%%UNIT%%` | Unit of the result | short | kPa |
| `%%HINT-1%%` | Small hint | 1 sentence | Which formula connects depth and pressure? |
| `%%HINT-2%%` | Bigger hint | 1 sentence | p = ρ · g · h, then convert Pa to kPa. |
| `%%SOLUTION%%` | Worked solution shown after solving | 1–4 lines | p = 1000 · 9.81 · 40 Pa = 392 400 Pa = 392.4 kPa |
| `%%NARRATION-1%%` | Spoken intro to the reflection | 1 sentence | Look back at how you solved it. |
| `%%REFLECTION-QUESTION%%` | Reflection question | 1 sentence | Where did you hesitate, and why? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%TASK-CONTEXT%%

<!-- data-type="none" -->
| Given | Value |
|-------|-------|
| %%GIVEN-1%% | %%VALUE-1%% |
| %%GIVEN-2%% | %%VALUE-2%% |
| %%GIVEN-3%% | %%VALUE-3%% |

**Calculate:** %%TASK-QUESTION%% Answer in %%UNIT%%.

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%RESULT-VALUE%%]]
[[?]] %%HINT-1%%
[[?]] %%HINT-2%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%RESULT-VALUE%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%SOLUTION%%
***

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Reflect:** %%REFLECTION-QUESTION%%

[[___ ___]]

****************************************

<!-- TEMPLATE:END -->
