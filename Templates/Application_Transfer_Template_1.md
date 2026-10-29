<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Case analysis with a real case, a data table and three guiding questions with open answers and model answers.
-->

# Template `Application_Transfer_Template_1`

- **Purpose:** Apply the content to a real case. Learners answer three guiding questions in writing, then compare with model answers.
- **Pairs with:** `Introduction_Template_3`, `Concept_Explanation_Template_2`, `Summary_Recap_Template_1`
- **Variants:** Use slide 1 alone as a case presentation in class. Order the questions from describe to analyse to evaluate.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Name of the case | max 6 words | Case: The Leaking Water Tower |
| `%%NARRATION-0%%` | Spoken case summary | 2–3 sentences | A town's water tower started leaking only five years after it was built. |
| `%%IMAGE-PATH%%` | Picture of the case | landscape | assets/images/water-tower.jpg |
| `%%IMAGE-ALT%%` | Description | max 12 words | Concrete water tower with wet stains at its base |
| `%%IMAGE-CAPTION%%` | Caption or credit | max 10 words | Photo: J. Doe, CC BY 4.0 |
| `%%CASE-TEXT%%` | Case description | 3–4 sentences | The tank sits 30 m above ground. Cracks appeared near the bottom of the tank wall. |
| `%%DATA-LABEL-1%%` … `%%DATA-LABEL-3%%` | Name of a case figure | max 4 words | Height of the tank floor ; Water depth in the tank ; Age of the tower |
| `%%DATA-VALUE-1%%` … `%%DATA-VALUE-3%%` | Value with unit | short | 30 m ; 12 m ; 5 years |
| `%%QUESTIONS-TITLE%%` | Title of the question slide | max 5 words | Analyse the Case |
| `%%NARRATION-Q-0%%` … `%%NARRATION-Q-2%%` | Spoken intro per question | 1 sentence | First, describe where the problem occurs. ; Next, explain the cause. ; Finally, judge the repair options. |
| `%%QUESTION-1%%` … `%%QUESTION-3%%` | Guiding question | 1 sentence | Where is the water pressure on the tank wall highest? ; How large is the pressure at the tank floor? ; Would a thicker wall at the top help? Why or why not? |
| `%%MODEL-ANSWER-1%%` … `%%MODEL-ANSWER-3%%` | Model answer | 1–3 sentences | At the bottom of the tank, because pressure grows with depth. ; p = 1000 · 9.81 · 12 Pa ≈ 118 kPa. ; No – the load is largest at the bottom, so the bottom part must be reinforced. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<div style="display:flex;gap:1.5rem;flex-wrap:wrap;align-items:flex-start;">
<div style="flex:1 1 260px;">

![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

</div>
<div style="flex:2 1 320px;">

%%CASE-TEXT%%

<!-- data-type="none" -->
| Figure | Value |
|--------|-------|
| %%DATA-LABEL-1%% | %%DATA-VALUE-1%% |
| %%DATA-LABEL-2%% | %%DATA-VALUE-2%% |
| %%DATA-LABEL-3%% | %%DATA-VALUE-3%% |

</div>
</div>

## %%QUESTIONS-TITLE%%

    --{{0}}--
%%NARRATION-Q-0%%

**1 · Answer:** %%QUESTION-1%%

[[___ ___]]

<details>

<summary>✅ Model answer</summary>

%%MODEL-ANSWER-1%%

</details>

    --{{1}}--
%%NARRATION-Q-1%%

      {{1}}
****************************************

**2 · Answer:** %%QUESTION-2%%

[[___ ___]]

<details>

<summary>✅ Model answer</summary>

%%MODEL-ANSWER-2%%

</details>

****************************************

    --{{2}}--
%%NARRATION-Q-2%%

      {{2}}
****************************************

**3 · Answer:** %%QUESTION-3%%

[[___ ___]]

<details>

<summary>✅ Model answer</summary>

%%MODEL-ANSWER-3%%

</details>

****************************************

<!-- TEMPLATE:END -->
