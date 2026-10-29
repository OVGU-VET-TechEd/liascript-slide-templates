<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Concept explained by contrast with a comparison table, a typical misconception and a classification quiz.
-->

# Template `Concept_Explanation_Template_2`

- **Purpose:** Explain two related concepts by comparing them on four criteria and clearing up a common misconception.
- **Pairs with:** `Content_Introduction_Template_2`, `Interactive_Exercise_Template_1`, `Application_Transfer_Template_2`
- **Variants:** Add a third column (and a third matrix column) for a concept C. Delete step 2 if there is no typical misconception. In the matrix quiz move (X) to the correct column for each of your statements (default: A, B, A, B).

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | "A vs B" title | max 6 words | Laminar vs Turbulent Flow |
| `%%NARRATION-0%%` | Spoken intro to the comparison | 1–2 sentences | Both are ways a fluid can move, but they behave very differently. |
| `%%CONCEPT-A%%`, `%%CONCEPT-B%%` | Names of the concepts | max 3 words | Laminar ; Turbulent |
| `%%CRITERION-1%%` … `%%CRITERION-4%%` | Comparison criterion | max 4 words | Particle paths ; Mixing ; Typical speed ; Reynolds number |
| `%%A-1%%` … `%%A-4%%` | Value for concept A | max 8 words | parallel layers ; very little ; low ; below about 2300 |
| `%%B-1%%` … `%%B-4%%` | Value for concept B | max 8 words | chaotic eddies ; strong ; high ; above about 4000 |
| `%%NARRATION-1%%` | Spoken intro to the examples | 1 sentence | Here is one everyday example of each. |
| `%%EXAMPLE-A%%`, `%%EXAMPLE-B%%` | Everyday example | max 10 words | Honey poured from a spoon ; Smoke rising from a candle after a few cm |
| `%%NARRATION-2%%` | Spoken warning | 1 sentence | Watch out for a common mistake. |
| `%%MISCONCEPTION%%` | Typical wrong idea and its correction | 1–2 sentences | Fast does not automatically mean turbulent – the Reynolds number decides. |
| `%%NARRATION-3%%` | Spoken intro to the quiz | 1 sentence | Now sort the statements. |
| `%%STATEMENT-1%%` … `%%STATEMENT-4%%` | Statement to classify | max 12 words | Dye injected into the flow stays a thin line. ; Milk mixes quickly into stirred coffee. ; Oil flows slowly through a thin tube. ; Water rushes out of a fire hose. |
| `%%CLASSIFY-HINT%%` | Hint | 1 sentence | Look at the table again. |
| `%%CLASSIFY-FEEDBACK%%` | Feedback after solving | 1 sentence | Orderly behaviour points to laminar, mixing points to turbulent flow. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- data-type="none" -->
| Criterion | %%CONCEPT-A%% | %%CONCEPT-B%% |
|-----------|---------------|---------------|
| %%CRITERION-1%% | %%A-1%% | %%B-1%% |
| %%CRITERION-2%% | %%A-2%% | %%B-2%% |
| %%CRITERION-3%% | %%A-3%% | %%B-3%% |
| %%CRITERION-4%% | %%A-4%% | %%B-4%% |

    --{{1}}--
%%NARRATION-1%%

      {{1}}
- **%%CONCEPT-A%%:** %%EXAMPLE-A%%
- **%%CONCEPT-B%%:** %%EXAMPLE-B%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!WARNING] Common misconception
> %%MISCONCEPTION%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
****************************************

**Decide:** Which concept does each statement describe?

<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
[(%%CONCEPT-A%%) (%%CONCEPT-B%%)]
[       (X)             ( )      ] %%STATEMENT-1%%
[       ( )             (X)      ] %%STATEMENT-2%%
[       (X)             ( )      ] %%STATEMENT-3%%
[       ( )             (X)      ] %%STATEMENT-4%%
[[?]] %%CLASSIFY-HINT%%
***
%%CLASSIFY-FEEDBACK%%
***

****************************************

<!-- TEMPLATE:END -->
