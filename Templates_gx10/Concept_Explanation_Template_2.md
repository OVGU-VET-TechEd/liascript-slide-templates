<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Explains a concept by contrasting two related notions with a table, examples and a classification quiz.

import:   none
-->

# Template `Concept_Explanation_Template_2`

- **Purpose:** Explain a concept by contrasting it with a related one, so learners see the difference instead of memorising a definition.
- **Pairs with:** `Content_Introduction_Template_1`, `Interactive_Exercise_Template_1`, `Summary_Recap_Template_1`
- **Variants:** Swap the four criteria for your own. Replace the examples with domain-specific cases or convert the A/B quiz into a true/false quiz.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title naming both concepts | max 6 words | Static array vs. linked list |
| `%%NARRATION-0%%` | Spoken intro of the contrast | 1–2 sentences | We meet two similar data structures that behave very differently. |
| `%%CONCEPT-A%%` | First concept | max 3 words | Static array |
| `%%CONCEPT-B%%` | Second concept | max 3 words | Linked list |
| `%%CRITERION-1%%` … `%%CRITERION-4%%` | Comparison criteria | max 3 words each | Size ; Access ; Insertion ; Typical use |
| `%%VALUE-A-1%%` … `%%VALUE-A-4%%` | Property of A per criterion | max 8 words each | Fixed at creation ; Direct by index ; Expensive shifts ; Fixed-size tables |
| `%%VALUE-B-1%%` … `%%VALUE-B-4%%` | Property of B per criterion | max 8 words each | Grows and shrinks ; Walk from head ; Cheap at the end ; Ordered queues |
| `%%KEY-MESSAGE%%` | One-sentence contrast takeaway | max 15 words | A is fixed and directly accessible, B grows and is walked element by element. |
| `%%NARRATION-1%%` | Spoken intro to the examples | 1 sentence | Let us make this concrete with two everyday cases. |
| `%%EXAMPLE-A%%` | Example case for A | 1–2 sentences | The grade sheet holds exactly 30 students, so a static array fits perfectly. |
| `%%EXAMPLE-B%%` | Example case for B | 1–2 sentences | Your to-do list changes all day, so a linked list fits perfectly. |
| `%%NARRATION-2%%` | Spoken warning | 1 sentence | One mistake happens in almost every exam. |
| `%%MISCONCEPTION%%` | Common false belief | 1–2 sentences | A linked list is not an array that resizes itself. It stores no indices at all. |
| `%%NARRATION-3%%` | Spoken quiz intro | 1 sentence | Now you classify four statements yourself. |
| `%%STATEMENT-1%%` … `%%STATEMENT-4%%` | Statements to classify | max 12 words each | You pick element 10 directly ; It grows when you add items ; Its size is fixed at creation ; Indexing is instant |
| `%%HINT-1%%` | Quiz hint | 1 sentence | Ask yourself one question for each row: is the size fixed or variable? |
| `%%FEEDBACK-1%%` | Feedback after solving | 1–2 sentences | A is fixed and directly accessible. B grows and is walked element by element. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- data-type="none" -->
| Criterion | %%CONCEPT-A%% | %%CONCEPT-B%% |
|---|---|---|
| %%CRITERION-1%% | %%VALUE-A-1%% | %%VALUE-B-1%% |
| %%CRITERION-2%% | %%VALUE-A-2%% | %%VALUE-B-2%% |
| %%CRITERION-3%% | %%VALUE-A-3%% | %%VALUE-B-3%% |
| %%CRITERION-4%% | %%VALUE-A-4%% | %%VALUE-B-4%% |

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

> [!NOTE] Key message
> %%KEY-MESSAGE%%

**%%CONCEPT-A%%:** %%EXAMPLE-A%%
**%%CONCEPT-B%%:** %%EXAMPLE-B%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!WARNING] Common misconception
> %%MISCONCEPTION%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
****************************************

**Try it:** Classify each statement as %%CONCEPT-A%% or %%CONCEPT-B%%.

<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
[(A) (B)]
[  (X)    ( )  ] %%STATEMENT-1%%
[  ( )    (X)  ] %%STATEMENT-2%%
[  (X)    ( )  ] %%STATEMENT-3%%
[  (X)    ( )  ] %%STATEMENT-4%%
[[?]] %%HINT-1%%
***
%%FEEDBACK-1%%
***

****************************************

<!-- TEMPLATE:END -->
