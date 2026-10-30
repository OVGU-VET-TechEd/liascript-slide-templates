<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Case-analysis slides that let learners answer guiding questions and compare with a model answer.
-->

# Template `Application_Transfer_Template_1`

- **Purpose:** Analyze a real-world case with learners: present a scenario with its data, then work through guiding questions with a model answer.
- **Pairs with:** `Simulation_Template_2`, `Summary_Recap_Template_1`
- **Variants:** Replace the data table with a citation block. Turn each details model answer into a single-choice quiz with feedback.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the case | max 6 words | The Clinic That Went Paperless |
| `%%NARRATION-0%%` | Spoken introduction of the case | 2–3 sentences | Let us look at a real clinic that went fully paperless in 2024. |
| `%%IMAGE-PATH%%` | Image of the case | landscape image | assets/images/clinic-records.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Reception desk of a modern clinic |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | Public domain, Wikimedia Commons |
| `%%CASE-TEXT%%` | The case in short | 2–3 sentences | In March 2024, Northside Clinic digitized all patient records and stopped using paper files. |
| `%%NARRATION-1%%` | Spoken intro to the data table | 1–2 sentences | Here are the numbers three months after the change. |
| `%%TABLE-HEADER-1%%` … `%%TABLE-HEADER-3%%` | Column headers | max 3 words | Metric ; Before ; After |
| `%%TABLE-ROW-1%%` … `%%TABLE-ROW-3%%` | Table row | one value per column | Record lookup time ; 6 min ; 3.5 min |
| `%%CASE-QUESTION-TITLE%%` | Title of the question slide | max 6 words | Working Through the Case |
| `%%NARRATION-2%%` | Spoken intro to the questions | 1–2 sentences | Now let us work through the case together, question by question. |
| `%%QUESTION-1%%` … `%%QUESTION-3%%` | Guiding question | 1 sentence | What most likely caused the billing errors to rise? |
| `%%NARRATION-3%%` | Spoken intro to question 1 | 1 sentence | Start with the cause of the billing errors. |
| `%%NARRATION-4%%` | Spoken intro to question 2 | 1 sentence | Now think about what the team overlooked. |
| `%%NARRATION-5%%` | Spoken intro to question 3 | 1 sentence | Finally, decide what the clinic should do next. |
| `%%SURVEY-QUESTION-TEXT%%` | Instruction above each text survey | 1 sentence | Reflect in one or two sentences. |
| `%%MODEL-ANSWER-1%%` … `%%MODEL-ANSWER-3%%` | Model answer per question | 1–2 sentences | The new billing module was switched on before staff finished training. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<div style="display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center;">
<div style="flex:1 1 260px;">
<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")
</div>
<div style="flex:1 1 260px;">
%%CASE-TEXT%%
</div>
</div>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
<!-- data-type="none" -->
| %%TABLE-HEADER-1%% | %%TABLE-HEADER-2%% | %%TABLE-HEADER-3%% |
|---|---|---|
| %%TABLE-ROW-1%% |
| %%TABLE-ROW-2%% |
| %%TABLE-ROW-3%% |

## %%CASE-QUESTION-TITLE%%

    --{{0}}--
%%NARRATION-2%%

    --{{1}}--
%%NARRATION-3%%

      {{1}}
**Reflect:** %%QUESTION-1%%

[[___ ___ ___]]

<details>
<summary>✅ Model answer</summary>

%%MODEL-ANSWER-1%%

</details>

    --{{2}}--
%%NARRATION-4%%

      {{2}}
**Reflect:** %%QUESTION-2%%

[[___ ___ ___]]

<details>
<summary>✅ Model answer</summary>

%%MODEL-ANSWER-2%%

</details>

    --{{3}}--
%%NARRATION-5%%

      {{3}}
**Reflect:** %%QUESTION-3%%

[[___ ___ ___]]

<details>
<summary>✅ Model answer</summary>

%%MODEL-ANSWER-3%%

</details>

<!-- TEMPLATE:END -->
