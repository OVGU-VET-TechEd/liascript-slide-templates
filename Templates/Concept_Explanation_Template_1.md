<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Concept explained by definition, formula with symbol table, worked example and a numeric practice task.
-->

# Template `Concept_Explanation_Template_1`

- **Purpose:** Explain a quantitative concept: definition, formula, symbols, worked example, then one calculation by the learners.
- **Pairs with:** `Content_Introduction_Template_1`, `Content_Introduction_Template_3`, `Simulation_Template_1`
- **Variants:** Use slide 1 alone for a pure explanation. Add symbol rows as needed. The answer check accepts 2 % deviation and a decimal comma.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Name of the concept | max 5 words | Hydrostatic Pressure |
| `%%NARRATION-0%%` | Spoken definition | 1–2 sentences | Hydrostatic pressure is the pressure inside a fluid at rest. |
| `%%DEFINITION%%` | Definition | 1–2 sentences | The pressure a resting fluid exerts at depth h because of the weight of the fluid above. |
| `%%NARRATION-1%%` | Spoken explanation of the formula | 1–2 sentences | It depends on density, gravity and depth – nothing else. |
| `%%FORMULA%%` | LaTeX formula without dollar signs | 1 line | `p = \rho \cdot g \cdot h` |
| `%%SYMBOL-1%%` … `%%SYMBOL-3%%` | Symbol in LaTeX | 1 symbol | `p` ; `\rho` ; `h` |
| `%%MEANING-1%%` … `%%MEANING-3%%` | Meaning of the symbol | max 6 words | hydrostatic pressure ; density of the fluid ; depth below the surface |
| `%%UNIT-1%%` … `%%UNIT-3%%` | Unit | short | Pa ; kg/m³ ; m |
| `%%EX-TITLE%%` | Title of the worked example slide | max 5 words | Worked Example: Pool |
| `%%NARRATION-EX-0%%` | Spoken problem statement | 1–2 sentences | How large is the pressure at the bottom of a three-metre pool? |
| `%%EX-PROBLEM%%` | Problem text | 1–2 sentences | Find the water pressure at a depth of 3 m (ρ = 1000 kg/m³, g = 9.81 m/s²). |
| `%%NARRATION-EX-1%%` … `%%NARRATION-EX-3%%` | Spoken comment per step | 1 sentence | First, we write down the formula. ; Then we insert the values. ; Finally, we calculate and convert the unit. |
| `%%EX-STEP-1%%` … `%%EX-STEP-3%%` | Solution step (text or $LaTeX$) | 1 line | $p = \rho \cdot g \cdot h$ ; $p = 1000 \cdot 9.81 \cdot 3\ \text{Pa}$ ; $p = 29\,430\ \text{Pa} \approx 29.4\ \text{kPa}$ |
| `%%NARRATION-EX-4%%` | Spoken intro to the task | 1 sentence | Now it is your turn. |
| `%%TASK%%` | Calculation task with unit | 1–2 sentences | Find the water pressure at a depth of 5 m in kPa. |
| `%%RESULT-VALUE%%` | Numeric result, dot as decimal sign | number | 49.05 |
| `%%HINT-1%%`, `%%HINT-2%%` | Small and bigger hint | 1 sentence | Use the same formula with h = 5 m. ; p = 1000 · 9.81 · 5 Pa, then divide by 1000. |
| `%%SOLUTION%%` | Worked solution shown after solving | 1–3 lines | p = 1000 · 9.81 · 5 Pa = 49 050 Pa = 49.05 kPa |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!IMPORTANT] Definition
> %%DEFINITION%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

$$
%%FORMULA%%
$$

<!-- data-type="none" -->
| Symbol | Meaning | Unit |
|--------|---------|------|
| $%%SYMBOL-1%%$ | %%MEANING-1%% | %%UNIT-1%% |
| $%%SYMBOL-2%%$ | %%MEANING-2%% | %%UNIT-2%% |
| $%%SYMBOL-3%%$ | %%MEANING-3%% | %%UNIT-3%% |

****************************************

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

**Problem:** %%EX-PROBLEM%%

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
1. %%EX-STEP-1%%

    --{{2}}--
%%NARRATION-EX-2%%

      {{2}}
2. %%EX-STEP-2%%

    --{{3}}--
%%NARRATION-EX-3%%

      {{3}}
3. %%EX-STEP-3%%

    --{{4}}--
%%NARRATION-EX-4%%

      {{4}}
****************************************

**Calculate:** %%TASK%%

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

****************************************

<!-- TEMPLATE:END -->
