<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Practice slide with a gap text (selection, typed and drag and drop gaps) and a true or false matrix.
-->

# Template `Interactive_Exercise_Template_2`

- **Purpose:** Practise terms and facts in context. A gap text first, then four true/false statements in one matrix.
- **Pairs with:** `Concept_Explanation_Template_3`, `Interactive_Exercise_Template_1`, `Summary_Recap_Template_2`
- **Variants:** Gap types can be swapped freely: selection `[[ a | (b) | c ]]`, typed `[[word]]`, drag `[->[ (b) | c ]]`. In the matrix move (X) to the right column for each of your statements (default: true, false, true, false).

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 5 words | Fill the Gaps |
| `%%NARRATION-0%%` | Spoken intro to the gap text | 1–2 sentences | Complete the text. Choose, type or drag the missing words. |
| `%%GAP-TEXT-1%%` | Text before gap 1 | sentence part | In a resting fluid the pressure |
| `%%GAP-1-CORRECT%%` | Correct option of the selection gap | 1–2 words | increases |
| `%%GAP-1-WRONG-1%%`, `%%GAP-1-WRONG-2%%` | Wrong options of the selection gap | 1–2 words | decreases ; stays constant |
| `%%GAP-TEXT-2%%` | Text between gap 1 and 2 | sentence part | with depth. Its SI unit is the |
| `%%GAP-2-ANSWER%%` | Typed answer (exact spelling) | 1 word | pascal |
| `%%GAP-TEXT-3%%` | Text between gap 2 and 3 | sentence part | , and the pressure at the bottom of a vessel does not depend on its |
| `%%GAP-3-CORRECT%%` | Correct drag card | 1–2 words | shape |
| `%%GAP-3-DISTRACTOR%%` | Wrong drag card | 1–2 words | depth |
| `%%GAP-TEXT-4%%` | Text after gap 3 | sentence part | . |
| `%%GAP-HINT%%` | Hint for the gap text | 1 sentence | Think of a diver going deeper. |
| `%%NARRATION-1%%` | Spoken intro to true or false | 1 sentence | Now decide: true or false? |
| `%%STATEMENT-1%%` … `%%STATEMENT-4%%` | Statement | max 15 words | Doubling the depth doubles the hydrostatic pressure. ; A wide tank has a higher floor pressure than a narrow one of the same depth. ; Sea water causes a slightly higher pressure than fresh water. ; Hydrostatic pressure acts only downwards. |
| `%%TF-HINT%%` | Hint for the matrix | 1 sentence | Check each statement against p = ρ · g · h. |
| `%%TF-FEEDBACK%%` | Feedback after solving | 1–2 sentences | Pressure grows linearly with depth and does not depend on the vessel shape. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Complete:**

<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
%%GAP-TEXT-1%% [[ (%%GAP-1-CORRECT%%) | %%GAP-1-WRONG-1%% | %%GAP-1-WRONG-2%% ]] %%GAP-TEXT-2%% [[%%GAP-2-ANSWER%%]]%%GAP-TEXT-3%% [->[ (%%GAP-3-CORRECT%%) | %%GAP-3-DISTRACTOR%% ]]%%GAP-TEXT-4%%
[[?]] %%GAP-HINT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Decide:** True or false?

<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
[(true) (false)]
[  (X)    ( )  ] %%STATEMENT-1%%
[  ( )    (X)  ] %%STATEMENT-2%%
[  (X)    ( )  ] %%STATEMENT-3%%
[  ( )    (X)  ] %%STATEMENT-4%%
[[?]] %%TF-HINT%%
***
%%TF-FEEDBACK%%
***

****************************************

<!-- TEMPLATE:END -->
