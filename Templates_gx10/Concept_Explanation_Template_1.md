<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Defines a concept with formula and symbol table, then walks through a worked example with a numeric check.

import:   none
-->

# Template `Concept_Explanation_Template_1`

- **Purpose:** Explain one core concept of a session – definition, formula, symbol table – and immediately anchor it with a fully worked example.
- **Pairs with:** `Content_Introduction_Template_1`, `Interactive_Exercise_Template_3`, `Simulation_Template_1`
- **Variants:** Replace the formula with a plain-text definition if the concept has no equation. Add a fourth reveal step on slide 2 for a unit conversion check.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Name of the concept | max 6 words | The Ideal Gas Law |
| `%%NARRATION-0%%` | Spoken intro to the definition | 1–2 sentences | Let us start with the definition you will use all week. |
| `%%DEFINITION%%` | Formal definition of the concept | 1–2 sentences | The ideal gas law links pressure, volume, temperature and amount of substance for an ideal gas. |
| `%%NARRATION-1%%` | Spoken intro to the formula | 1 sentence | The law is one short equation. |
| `%%FORMULA%%` | The formula in LaTeX | 1 equation | pV = nRT |
| `%%NARRATION-2%%` | Spoken intro to the symbol table | 1 sentence | Here is what every symbol means. |
| `%%SYM-1-NAME%%` … `%%SYM-5-NAME%%` | Symbol names | 1 word each | p ; V ; n ; R ; T |
| `%%SYM-1-UNIT%%` … `%%SYM-5-UNIT%%` | Units | 1 unit each | kPa ; L ; mol ; kPa·L/(mol·K) ; K |
| `%%SYM-1-MEANING%%` … `%%SYM-5-MEANING%%` | Meanings | max 5 words each | pressure ; volume ; amount of substance ; gas constant 8.314 ; temperature |
| `%%EX-TITLE%%` | Title of the worked example | max 6 words | Worked Example |
| `%%NARRATION-EX-0%%` | Spoken intro to the example | 1–2 sentences | Let us apply the law to a concrete case. |
| `%%EX-GIVEN%%` | Given values of the example | 3–4 values | n = 2 mol, V = 10 L, T = 300 K, R = 8.314 kPa·L/(mol·K) |
| `%%NARRATION-EX-1%%` | Spoken step 1 | 1 sentence | First we write the formula with the values inserted. |
| `%%EX-STEP-1%%` | Step 1, substitution | 1 line | p = (nRT) / V = (2 · 8.314 · 300) / 10 |
| `%%NARRATION-EX-2%%` | Spoken step 2 | 1 sentence | Then we multiply the numerator. |
| `%%EX-STEP-2%%` | Step 2, intermediate result | 1 line | p = 4988.4 / 10 |
| `%%NARRATION-EX-3%%` | Spoken step 3 | 1 sentence | Finally we divide and read off the result. |
| `%%EX-STEP-3%%` | Step 3, final result | 1 line | p = 498.84 kPa, about 500 kPa |
| `%%NARRATION-EX-4%%` | Spoken intro to the check | 1 sentence | Now check it yourself. |
| `%%EX-QUESTION%%` | Numeric question for the check | 1 sentence | What is the pressure in kPa, rounded to the nearest whole number? |
| `%%EX-ANSWER%%` | Expected numeric answer | number without unit | 500 |
| `%%EX-HINT-1%%` | First hint | 1 sentence | Solve the formula for p before you insert the numbers. |
| `%%EX-HINT-2%%` | Second hint | 1 sentence | Multiply 2, 8.314 and 300 first, then divide by 10. |
| `%%EX-SOLUTION%%` | Full solution text | 1–2 lines | p = (2 · 8.314 · 300) / 10 = 4988.4 / 10 = 498.84 kPa, rounded to 500 kPa. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!IMPORTANT] Definition
> %%DEFINITION%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
$$
%%FORMULA%%
$$

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

<!-- data-type="none" -->
| Symbol | Unit | Meaning |
|---|---|---|
| %%SYM-1-NAME%% | %%SYM-1-UNIT%% | %%SYM-1-MEANING%% |
| %%SYM-2-NAME%% | %%SYM-2-UNIT%% | %%SYM-2-MEANING%% |
| %%SYM-3-NAME%% | %%SYM-3-UNIT%% | %%SYM-3-MEANING%% |
| %%SYM-4-NAME%% | %%SYM-4-UNIT%% | %%SYM-4-MEANING%% |
| %%SYM-5-NAME%% | %%SYM-5-UNIT%% | %%SYM-5-MEANING%% |

****************************************

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

**Given:** %%EX-GIVEN%%

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
**Step 1 – Substitute:** %%EX-STEP-1%%

    --{{2}}--
%%NARRATION-EX-2%%

      {{2}}
**Step 2 – Multiply:** %%EX-STEP-2%%

    --{{3}}--
%%NARRATION-EX-3%%

      {{3}}
**Step 3 – Divide:** %%EX-STEP-3%%

    --{{4}}--
%%NARRATION-EX-4%%

      {{4}}
****************************************

**Type:** %%EX-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%EX-ANSWER%%]]
[[?]] %%EX-HINT-1%%
[[?]] %%EX-HINT-2%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%EX-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%EX-SOLUTION%%
***

****************************************

<!-- TEMPLATE:END -->
