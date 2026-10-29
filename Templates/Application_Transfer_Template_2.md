<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Find-the-mistake task with a four-step solution, a quiz to locate the error and a check of the corrected value.
-->

# Template `Application_Transfer_Template_2`

- **Purpose:** Train critical reading. A solution with exactly one wrong step is shown; learners locate it and give the correct result.
- **Pairs with:** `Concept_Explanation_Template_1`, `Interactive_Exercise_Template_3`, `Simulation_Template_3`
- **Variants:** Use code lines, a drawing or an argument instead of calculation steps. Move (X) in the locate quiz to the step that holds YOUR error (default: step 3).

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 5 words | Spot the Mistake |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | A student solved this task. One of the four steps is wrong. |
| `%%PROBLEM%%` | The original task | 1–2 sentences | Find the pressure at 2 m depth in sea water (ρ = 1025 kg/m³) in kPa. |
| `%%STEP-1%%` … `%%STEP-4%%` | Solution step (text or $LaTeX$) | 1 line | $p = \rho \cdot g \cdot h$ ; $h = 2\ \text{m} = 200\ \text{cm}$ ; $p = 1025 \cdot 9.81 \cdot 200\ \text{Pa}$ ; $p = 2\,011\,050\ \text{Pa} \approx 2011\ \text{kPa}$ |
| `%%NARRATION-1%%` | Spoken intro to the locate quiz | 1 sentence | Which step is wrong? |
| `%%LOCATE-HINT%%` | Hint | 1 sentence | Check the units in every step. |
| `%%LOCATE-FEEDBACK%%` | Why this step is wrong | 1–2 sentences | Step 3 uses 200 cm instead of 2 m for the depth. |
| `%%NARRATION-2%%` | Spoken intro to the correction | 1 sentence | Now give the correct result. |
| `%%CORRECT-QUESTION%%` | Question for the corrected value | 1 sentence | What is the correct pressure in kPa? |
| `%%CORRECT-ANSWER%%` | Correct value, dot as decimal sign | number | 20.11 |
| `%%CORRECT-HINT%%` | Hint | 1 sentence | Repeat step 3 with h = 2 m. |
| `%%SOLUTION%%` | Worked correct solution | 1–3 lines | p = 1025 · 9.81 · 2 Pa = 20 110 Pa ≈ 20.11 kPa |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Task:** %%PROBLEM%%

<!-- data-type="none" -->
| Step | Student solution |
|------|------------------|
| 1 | %%STEP-1%% |
| 2 | %%STEP-2%% |
| 3 | %%STEP-3%% |
| 4 | %%STEP-4%% |

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Locate:** Which step contains the mistake?

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] Step 1
- [( )] Step 2
- [(X)] Step 3
- [( )] Step 4
[[?]] %%LOCATE-HINT%%
***
%%LOCATE-FEEDBACK%%
***

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Correct:** %%CORRECT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%CORRECT-ANSWER%%]]
[[?]] %%CORRECT-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%CORRECT-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%SOLUTION%%
***

****************************************

<!-- TEMPLATE:END -->
