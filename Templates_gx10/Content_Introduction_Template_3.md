<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Starts a content block with a scenario, a cited fact, a key problem, then a Predict-Observe-Explain cycle.
-->

# Template `Content_Introduction_Template_3`

- **Purpose:** Open a content block with a concrete scenario and a cited fact, pose the problem, and let learners predict, observe and explain.
- **Pairs with:** `Content_Introduction_Template_1`, `Content_Introduction_Template_2`, `Concept_Explanation_Template_1`
- **Variants:** Replace the citation with a key message NOTE box. Merge both slides if the observation is already known to the class.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the scenario slide | max 6 words | Why Does the Lake Freeze |
| `%%NARRATION-0%%` | Spoken scenario opener | 2–3 sentences | Picture a winter morning in a small town on the northern edge of a lake. |
| `%%IMAGE-PATH%%` | Image of the scenario | landscape image | assets/images/frozen-lake.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Frozen lake beside a still-liquid river |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | Photo by J. Meyer, CC BY 4.0 |
| `%%CASE-TEXT%%` | The scenario in short | 2–3 sentences | The lake is covered in solid ice, yet the river running through the town flows freely. |
| `%%QUOTE%%` | Cited fact or statement | 1–2 sentences | Still water at the surface reaches 0 °C first, while moving water stays warmer. |
| `%%QUOTE-SOURCE%%` | Source of the quote | max 12 words | Lindqvist, Cold Fronts and Lakes, 2019 |
| `%%NARRATION-1%%` | Spoken intro to the problem | 1–2 sentences | That difference is exactly what we need to understand. |
| `%%KEY-PROBLEM%%` | The problem the block solves | 1–2 sentences | Why does still water freeze while moving water stays liquid at the same temperature? |
| `%%EX-TITLE%%` | Title of the POE slide | max 6 words | Predict, Observe, Explain |
| `%%NARRATION-EX-0%%` | Spoken intro to POE | 1 sentence | Let us work through this step by step. |
| `%%PREDICT-QUESTION%%` | Prediction question | 1 sentence | What do you think happens to the river this winter? |
| `%%PREDICT-CORRECT%%` | Correct prediction | max 10 words | It stays liquid all winter |
| `%%PREDICT-WRONG-1%%` | Plausible wrong prediction | max 10 words | It freezes from the banks inward |
| `%%PREDICT-WRONG-2%%` | Plausible wrong prediction | max 10 words | It freezes overnight like the lake |
| `%%PREDICT-HINT%%` | Hint | 1 sentence | Think about what moving water does to its own temperature. |
| `%%PREDICT-FEEDBACK%%` | Short feedback after answering | 1 sentence | Right – the flow keeps the river above freezing. |
| `%%NARRATION-EX-1%%` | Spoken reveal of observation | 1–2 sentences | Now let us check what was actually measured. |
| `%%OBSERVATION%%` | The real observation | 1–2 sentences | The river stayed liquid all winter while the lake froze solid by December. |
| `%%NARRATION-EX-2%%` | Spoken invite to explain | 1 sentence | Now it is your turn to explain what you saw. |
| `%%EXPLAIN-PROMPT%%` | Prompt for the explanation | 1 sentence | In three lines: why did the river stay liquid? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

%%CASE-TEXT%%

> %%QUOTE%%
>
> -- %%QUOTE-SOURCE%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!IMPORTANT] The problem
> %%KEY-PROBLEM%%

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

**Predict:** %%PREDICT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%PREDICT-CORRECT%%
- [( )] %%PREDICT-WRONG-1%%
- [( )] %%PREDICT-WRONG-2%%
[[?]] %%PREDICT-HINT%%
***
%%PREDICT-FEEDBACK%%
***

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
> [!NOTE] What we observed
> %%OBSERVATION%%

    --{{2}}--
%%NARRATION-EX-2%%

      {{2}}
**Explain:** %%EXPLAIN-PROMPT%%

[[___ ___ ___]]

<!-- TEMPLATE:END -->
