<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Parameter simulation with two sliders, a live result table and bar, framed by a prediction and guiding questions.
-->

# Template `Simulation_Template_1`

- **Purpose:** Learners explore a formula or model by moving two sliders. No import needed, runs in every LiaScript viewer.
- **Pairs with:** `Concept_Explanation_Template_1`, `Content_Introduction_Template_3`, `Interactive_Exercise_Template_3`
- **Variants:** The model is one JavaScript expression in `p1` and `p2` (e.g. `0.5 * p1 * p2 ** 2`, `Math.sqrt(p1) * p2`). Fields that go into the script must not contain quotes, backticks or vertical bars.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the simulation | max 5 words | Explore Kinetic Energy |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | Before you play with the model, make a prediction. |
| `%%PREDICT-QUESTION%%` | Prediction question | 1 sentence | You double the speed. What happens to the energy? |
| `%%PREDICT-CORRECT%%` | Correct prediction | max 10 words | It becomes four times as large |
| `%%PREDICT-WRONG-1%%` | Wrong prediction | max 10 words | It doubles |
| `%%PREDICT-WRONG-2%%` | Wrong prediction | max 10 words | It stays the same |
| `%%PREDICT-HINT%%` | Hint | 1 sentence | Look at the exponent of v. |
| `%%NARRATION-1%%` | Spoken instruction for the sliders | 1–2 sentences | Now move the sliders and watch the result. |
| `%%PARAM-1-LABEL%%` | Name and unit of slider 1 (p1) | max 4 words | Mass m in kg |
| `%%PARAM-1-MIN%%` | Smallest value of slider 1 | number | 1 |
| `%%PARAM-1-MAX%%` | Largest value of slider 1 | number | 100 |
| `%%PARAM-1-STEP%%` | Step of slider 1 | number | 1 |
| `%%PARAM-1-START%%` | Start value of slider 1 | number | 10 |
| `%%PARAM-2-LABEL%%` | Name and unit of slider 2 (p2) | max 4 words | Speed v in m/s |
| `%%PARAM-2-MIN%%` | Smallest value of slider 2 | number | 0 |
| `%%PARAM-2-MAX%%` | Largest value of slider 2 | number | 40 |
| `%%PARAM-2-STEP%%` | Step of slider 2 | number | 1 |
| `%%PARAM-2-START%%` | Start value of slider 2 | number | 10 |
| `%%MODEL%%` | JavaScript expression in p1 and p2 | 1 line | `0.5 * p1 * p2 ** 2` |
| `%%RESULT-LABEL%%` | Name of the result | max 3 words | Energy E |
| `%%RESULT-UNIT%%` | Unit of the result | short | J |
| `%%RESULT-DIGITS%%` | Decimal places of the result | 0–4 | 1 |
| `%%NARRATION-2%%`, `%%NARRATION-3%%` | Spoken guiding question | 1 sentence | Keep the mass fixed and double the speed. ; Now keep the speed fixed and change the mass. |
| `%%EXPLORE-1%%`, `%%EXPLORE-2%%` | Guiding question | 1 sentence | Set v to 10 and then to 20. By what factor does E grow? ; Double the mass at v = 10. By what factor does E grow now? |
| `%%KEY-MESSAGE%%` | What the simulation shows | 1 sentence | Energy grows with the square of the speed. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Predict:** %%PREDICT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] %%PREDICT-WRONG-1%%
- [(X)] %%PREDICT-CORRECT%%
- [( )] %%PREDICT-WRONG-2%%
[[?]] %%PREDICT-HINT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Try it:** Move the sliders.

%%PARAM-1-LABEL%%: <script input="range" min="%%PARAM-1-MIN%%" max="%%PARAM-1-MAX%%" step="%%PARAM-1-STEP%%" value="%%PARAM-1-START%%" default="%%PARAM-1-START%%" output="p1" aria-label="%%PARAM-1-LABEL%%">@input</script>

%%PARAM-2-LABEL%%: <script input="range" min="%%PARAM-2-MIN%%" max="%%PARAM-2-MAX%%" step="%%PARAM-2-STEP%%" value="%%PARAM-2-START%%" default="%%PARAM-2-START%%" output="p2" aria-label="%%PARAM-2-LABEL%%">@input</script>

<script>
const model = (p1, p2) => %%MODEL%%
const corners = [model(%%PARAM-1-MIN%%, %%PARAM-2-MIN%%), model(%%PARAM-1-MIN%%, %%PARAM-2-MAX%%),
                 model(%%PARAM-1-MAX%%, %%PARAM-2-MIN%%), model(%%PARAM-1-MAX%%, %%PARAM-2-MAX%%)]
const maxResult = Math.max(...corners.map(Math.abs)) || 1
const p1 = parseFloat(@input(`p1`))
const p2 = parseFloat(@input(`p2`))
const result = model(p1, p2)
const pct = Math.min(100, 100 * Math.abs(result) / maxResult).toFixed(1)
"LIASCRIPT: <!-- data-type=\"none\" -->\n" +
"| %%PARAM-1-LABEL%% | %%PARAM-2-LABEL%% | %%RESULT-LABEL%% |\n|---|---|---|\n" +
"| " + p1 + " | " + p2 + " | **" + result.toFixed(%%RESULT-DIGITS%%) + " %%RESULT-UNIT%%** |\n\n" +
"<div style=\"background:#dee2e6;border-radius:4px;max-width:420px;\"><div style=\"background:#0b7285;height:12px;border-radius:4px;width:" + pct + "%;\"></div></div>"
</script>

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
**Explore 1:** %%EXPLORE-1%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
****************************************

**Explore 2:** %%EXPLORE-2%%

> [!NOTE] Key message
> %%KEY-MESSAGE%%

****************************************

<!-- TEMPLATE:END -->
