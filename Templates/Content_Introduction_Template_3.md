<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Start of a content block from a real-life example using Predict, Observe, Explain.
-->

# Template `Content_Introduction_Template_3`

- **Purpose:** Introduce a concept through a real scenario. Learners predict, see the observation, then explain it in their words.
- **Pairs with:** `Introduction_Template_3`, `Concept_Explanation_Template_1`, `Simulation_Template_1`
- **Variants:** Replace the citation with a small data table. Use slide 1 alone as a short real-life opener.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the scenario | max 6 words | Why Do Steel Ships Float? |
| `%%NARRATION-0%%` | Spoken scenario | 2–3 sentences | A container ship weighs 200,000 tonnes and still floats. |
| `%%IMAGE-PATH%%` | Picture of the scenario | landscape | assets/images/ship.jpg |
| `%%IMAGE-ALT%%` | Description | max 12 words | Large container ship in a harbour |
| `%%IMAGE-CAPTION%%` | Caption or credit | max 10 words | Photo: J. Doe, CC BY 4.0 |
| `%%SCENARIO-TEXT%%` | Scenario description | 2 sentences | The ship is made of steel. A steel bolt sinks at once. |
| `%%NARRATION-1%%` | Spoken intro to the quote or data | 1 sentence | Here is a number that surprises most people. |
| `%%QUOTE%%` | Quote or data point | 1–2 sentences | Steel is almost eight times as dense as water. |
| `%%QUOTE-SOURCE%%` | Source | max 10 words | Material data sheet, EN 10025 |
| `%%NARRATION-2%%` | Spoken problem statement | 1 sentence | So here is our problem. |
| `%%PROBLEM%%` | Problem leading to the concept | 1 sentence | How can something denser than water float? |
| `%%POE-TITLE%%` | Title of the POE slide | max 5 words | Predict, Observe, Explain |
| `%%NARRATION-POE-0%%` | Spoken intro to predict | 1 sentence | First, make a prediction. |
| `%%PREDICT-QUESTION%%` | Prediction question | 1 sentence | A steel bowl is placed on water. What happens? |
| `%%PREDICT-CORRECT%%` | Correct prediction | max 10 words | It floats |
| `%%PREDICT-WRONG-1%%`, `%%PREDICT-WRONG-2%%` | Plausible wrong predictions | max 10 words | It sinks slowly ; It sinks at once |
| `%%PREDICT-HINT%%` | Hint | 1 sentence | Think of the water the bowl pushes aside. |
| `%%NARRATION-POE-1%%` | Spoken observation | 1–2 sentences | Look at what happens. |
| `%%OBSERVATION%%` | What is observed | 1–2 sentences | The bowl floats until water runs over its rim. |
| `%%NARRATION-POE-2%%` | Spoken intro to explain | 1 sentence | Now explain it in your own words. |
| `%%EXPLAIN-PROMPT%%` | Explain question | 1 sentence | Why does the bowl float while the bolt sinks? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

%%SCENARIO-TEXT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> %%QUOTE%%
>
> -- %%QUOTE-SOURCE%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!IMPORTANT] Problem
> %%PROBLEM%%

## %%POE-TITLE%%

    --{{0}}--
%%NARRATION-POE-0%%

**Predict:** %%PREDICT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%PREDICT-CORRECT%%
- [( )] %%PREDICT-WRONG-1%%
- [( )] %%PREDICT-WRONG-2%%
[[?]] %%PREDICT-HINT%%

    --{{1}}--
%%NARRATION-POE-1%%

      {{1}}
> [!NOTE] Observe
> %%OBSERVATION%%

    --{{2}}--
%%NARRATION-POE-2%%

      {{2}}
****************************************

**Explain:** %%EXPLAIN-PROMPT%%

[[___ ___ ___]]

****************************************

<!-- TEMPLATE:END -->
