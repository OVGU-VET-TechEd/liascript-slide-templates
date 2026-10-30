<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Gap text with selection, typed and drag gaps followed by a true false matrix quiz.
-->

# Template `Interactive_Exercise_Template_2`

- **Purpose:** Practise a topic in context by filling a short gap text and then judging related true/false statements.
- **Pairs with:** `Interactive_Exercise_Template_1`, `Interactive_Exercise_Template_3`
- **Variants:** Replace the drag gap with a second selection gap. Add a third true/false statement for longer sessions.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the exercise | max 6 words | Eiffel Tower Quick Check |
| `%%NARRATION-0%%` | Opening narration | 1–2 sentences | Let us test what you remember about the Eiffel Tower. |
| `%%GAP-TEXT%%` | Sentence with three gaps | 1–2 sentences | The Eiffel Tower was built in [[1889]] from [[ iron | (steel) | concrete ]] and stands in [->[ (Paris) | Lyon | Marseille ]]. |
| `%%SELECTION-CORRECT%%` | Correct selection option | max 8 words | iron |
| `%%SELECTION-WRONG-1%%` | Wrong selection option | max 8 words | steel |
| `%%SELECTION-WRONG-2%%` | Wrong selection option | max 8 words | concrete |
| `%%TYPED-ANSWER%%` | Typed gap answer, prefer a number | 1–4 words | 1889 |
| `%%DRAG-CORRECT%%` | Correct drag card | max 8 words | Paris |
| `%%DRAG-WRONG-1%%` | Wrong drag card | max 8 words | Lyon |
| `%%DRAG-WRONG-2%%` | Wrong drag card | max 8 words | Marseille |
| `%%GAP-HINT%%` | Hint for the gap text | 1 sentence | Think about what material the tower is made of. |
| `%%GAP-FEEDBACK%%` | Feedback after the gap text | 1 sentence | The tower is made of iron and was completed in 1889. |
| `%%NARRATION-EX-0%%` | Opening narration for the matrix | 1–2 sentences | Now decide whether each statement about the tower is true or false. |
| `%%STATEMENT-1%%` | True or false statement 1 | max 15 words | The Eiffel Tower is taller than 300 metres. |
| `%%STATEMENT-2%%` | True or false statement 2 | max 15 words | The tower is made of steel. |
| `%%STATEMENT-3%%` | True or false statement 3 | max 15 words | Gustave Eiffel designed the tower. |
| `%%STATEMENT-4%%` | True or false statement 4 | max 15 words | The tower was built as a permanent hotel. |
| `%%MATRIX-HINT%%` | Hint for the matrix | 1 sentence | Remember that the tower was built for a temporary exhibition. |
| `%%MATRIX-FEEDBACK%%` | Feedback after the matrix | 1 sentence | The tower is iron, not steel, and was built for the 1889 World Fair. |
| `%%NARRATION-EX-1%%` | Closing narration | 1 sentence | Check your answers and note which statements you got wrong. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Fill in the gaps:** %%GAP-TEXT%%

    --{{1}}--

      {{1}}
[[?]] %%GAP-HINT%%

    --{{2}}--

      {{2}}
***
%%GAP-FEEDBACK%%
***

## True or False

    --{{0}}--
%%NARRATION-EX-0%%

**Decide:** Mark each statement as true or false.

    --{{1}}--

      {{1}}
<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
[(true) (false)]
[  (X)    ( )  ] %%STATEMENT-1%%
[  ( )    (X)  ] %%STATEMENT-2%%
[  (X)    ( )  ] %%STATEMENT-3%%
[  ( )    (X)  ] %%STATEMENT-4%%
[[?]] %%MATRIX-HINT%%
***
%%MATRIX-FEEDBACK%%
***

    --{{2}}--
%%NARRATION-EX-1%%

> [!NOTE] Key message
> Review any statement you marked incorrectly before moving on.

<!-- TEMPLATE:END -->
