<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Explore a two-parameter model with sliders after a prediction and end with a key message
-->

# Template `Simulation_Template_1`

- **Purpose:** Let learners predict, then explore how two parameters of a small model shape its result with live sliders.
- **Pairs with:** `Concept_Explanation_Template_1`, `Interactive_Exercise_Template_3`, `Summary_Recap_Template_1`
- **Variants:** Make the prediction a text answer instead of single choice. Swap the bar for a plain table if the result can be negative.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the model to explore | max 6 words | How a Line Makes a Prediction |
| `%%NARRATION-0%%` | Spoken intro to the model | 2–3 sentences | Our model is a straight line. The slope says how much the result grows per step, the intercept is the starting value. |
| `%%MODEL-CONTEXT%%` | What the model describes | 2 sentences | A shop sells 100 coffees on a mild day. For every degree above 15 degrees, it sells a few more. |
| `%%NARRATION-1%%` | Spoken intro to the prediction | 1 sentence | Before you touch the sliders, make a prediction. |
| `%%PREDICT-QUESTION%%` | Prediction question before exploring | 1 sentence | If the slope doubles, what happens to the result? |
| `%%PREDICT-CORRECT%%` | Correct prediction | max 12 words | It grows by roughly double the slope part |
| `%%PREDICT-WRONG-1%%` | Plausible wrong prediction | max 12 words | It stays the same, only the start changes |
| `%%PREDICT-WRONG-2%%` | Plausible wrong prediction | max 12 words | It gets exactly twice as big |
| `%%PREDICT-HINT%%` | Hint for the prediction | 1 sentence | The intercept does not depend on the slope. |
| `%%PREDICT-FEEDBACK%%` | Short feedback after answering | 1 sentence | Right – only the part that scales with the input changes. |
| `%%NARRATION-2%%` | Spoken intro to the sliders | 1–2 sentences | Now you control the model yourself. Move the slope and watch the bar. |
| `%%PARAM-1-LABEL%%` | Label of slider 1 | max 6 words | Slope (extra coffees per degree) |
| `%%PARAM-1-MIN%%` | Minimum of slider 1 | number | 0 |
| `%%PARAM-1-MAX%%` | Maximum of slider 1 | number | 10 |
| `%%PARAM-1-STEP%%` | Step of slider 1 | number | 1 |
| `%%PARAM-1-START%%` | Start value of slider 1 | number | 5 |
| `%%PARAM-2-LABEL%%` | Label of slider 2 | max 6 words | Intercept (base coffees) |
| `%%PARAM-2-MIN%%` | Minimum of slider 2 | number | 0 |
| `%%PARAM-2-MAX%%` | Maximum of slider 2 | number | 200 |
| `%%PARAM-2-STEP%%` | Step of slider 2 | number | 10 |
| `%%PARAM-2-START%%` | Start value of slider 2 | number | 100 |
| `%%MODEL%%` | Model function of two parameters | 1 line, no quotes | (a, b) => a * 10 + b |
| `%%NARRATION-3%%` | Spoken explore question 1 | 1 sentence | Now test your prediction by doubling the slope. |
| `%%EXPLORE-1%%` | Open explore question 1 | 1 sentence | What happens to the result when you double the slope? |
| `%%EXPLORE-1-HINT-1%%` | First hint for explore 1 | 1 sentence | Compare the result before and after the change. |
| `%%EXPLORE-1-HINT-2%%` | Second hint for explore 1 | 1 sentence | The bar width is proportional to the result. |
| `%%EXPLORE-1-SOLUTION%%` | Solution for explore 1 | 1 sentence | Doubling the slope adds another slope-times-input to the result. |
| `%%NARRATION-4%%` | Spoken explore question 2 | 1 sentence | And what does the intercept control? |
| `%%EXPLORE-2%%` | Open explore question 2 | 1 sentence | Set the slope to zero. What is left? |
| `%%EXPLORE-2-HINT-1%%` | First hint for explore 2 | 1 sentence | Look at the bar when the slope is zero. |
| `%%EXPLORE-2-HINT-2%%` | Second hint for explore 2 | 1 sentence | The result then equals the intercept alone. |
| `%%EXPLORE-2-SOLUTION%%` | Solution for explore 2 | 1 sentence | With slope zero, the result is exactly the intercept. |
| `%%NARRATION-5%%` | Spoken wrap-up | 1 sentence | Let us collect what the sliders taught us. |
| `%%KEY-MESSAGE%%` | Key message of the model | 1–2 sentences | The slope sets how strongly the input matters, the intercept sets the starting value. |

**Default for `%%MODEL%%`:**

```js
(a, b) => a * 10 + b
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%MODEL-CONTEXT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Predict:** %%PREDICT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%PREDICT-CORRECT%%
- [( )] %%PREDICT-WRONG-1%%
- [( )] %%PREDICT-WRONG-2%%
[[?]] %%PREDICT-HINT%%
***
%%PREDICT-FEEDBACK%%
***

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
%%PARAM-1-LABEL%%: <script input="range" min="%%PARAM-1-MIN%%" max="%%PARAM-1-MAX%%" step="%%PARAM-1-STEP%%" value="%%PARAM-1-START%%" default="%%PARAM-1-START%%" output="p1" aria-label="%%PARAM-1-LABEL%%">@input</script>

%%PARAM-2-LABEL%%: <script input="range" min="%%PARAM-2-MIN%%" max="%%PARAM-2-MAX%%" step="%%PARAM-2-STEP%%" value="%%PARAM-2-START%%" default="%%PARAM-2-START%%" output="p2" aria-label="%%PARAM-2-LABEL%%">@input</script>

<script>
const model = (p1, p2) => %%MODEL%%
const p1 = parseFloat(@input(`p1`))
const p2 = parseFloat(@input(`p2`))
const result = model(p1, p2)
const bar = Math.min(100, Math.max(0, result / (10 * 200) * 100))
"LIASCRIPT: **Result:** " + result.toFixed(1) + "\n\n" +
"| Parameter | Value |\n|---|---|\n| " + p1 + " | " + p2 + " |\n\n" +
"<div style='background:#e0e0e0;'><div style='background:#4a90d9;width:" + bar.toFixed(1) + "%;height:18px;'></div></div>"
</script>

    --{{3}}--
%%NARRATION-3%%

      {{3}}
**Try it:** %%EXPLORE-1%%

<details>
<summary>💡 Hint 1</summary>

%%EXPLORE-1-HINT-1%%

</details>

<details>
<summary>💡 Hint 2</summary>

%%EXPLORE-1-HINT-2%%

</details>

<details>
<summary>✅ Solution</summary>

%%EXPLORE-1-SOLUTION%%

</details>

    --{{4}}--
%%NARRATION-4%%

      {{4}}
**Try it:** %%EXPLORE-2%%

<details>
<summary>💡 Hint 1</summary>

%%EXPLORE-2-HINT-1%%

</details>

<details>
<summary>💡 Hint 2</summary>

%%EXPLORE-2-HINT-2%%

</details>

<details>
<summary>✅ Solution</summary>

%%EXPLORE-2-SOLUTION%%

</details>

    --{{5}}--
%%NARRATION-5%%

      {{5}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

<!-- TEMPLATE:END -->
