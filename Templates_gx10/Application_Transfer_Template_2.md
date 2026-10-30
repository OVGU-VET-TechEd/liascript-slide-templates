<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Learners audit a four-step worked solution, spot the one wrong step and compute the correct value.
-->

# Template `Application_Transfer_Template_2`

- **Purpose:** Let learners audit a worked solution, find the single wrong step and then compute the correct value themselves.
- **Pairs with:** `Application_Transfer_Template_1`, `Application_Transfer_Template_3`
- **Variants:** Swap the table for a drag-and-drop ordering of the steps. Replace the numeric question with a text answer if the result is a word.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the case | max 6 words | The Van That Overspent |
| `%%NARRATION-0%%` | Spoken intro to the case | 2–3 sentences | A delivery company checks the fuel cost of a 240 km route before quoting a customer. |
| `%%CASE-TEXT%%` | The task in short | 2–3 sentences | A van drives 90 km/h for 2 hours 40 minutes, consumes 6.5 L per 100 km, and fuel costs 1.75 € per litre. |
| `%%STEP-1-TEXT%%` … `%%STEP-4-TEXT%%` | What the clerk does in each step | max 8 words | Convert 2 h 40 min to hours |
| `%%STEP-1-RESULT%%` … `%%STEP-4-RESULT%%` | Result of each step, one is wrong | number + unit | 2.67 h ; 240 km ; 1560 L ; 2730 € |
| `%%NARRATION-1%%` | Spoken intro to the quiz | 1 sentence | One of these four steps is wrong – can you find it? |
| `%%FIND-QUESTION%%` | Which-step question | 1 sentence | Which step of the clerk's calculation contains the mistake? |
| `%%FIND-CORRECT%%` | The wrong step, the correct choice | max 8 words | Step 3 – the fuel amount |
| `%%FIND-WRONG-1%%` … `%%FIND-WRONG-3%%` | The other three steps | max 8 words | Step 1 – the time conversion ; Step 2 – the distance ; Step 4 – the cost |
| `%%FIND-HINT%%` | Hint | 1 sentence | Check which result makes no sense for a 240 km trip. |
| `%%FIND-FEEDBACK%%` | Feedback after answering | 1–2 sentences | Step 3 forgot to divide by 100, so the fuel amount is 100 times too large. |
| `%%EX-TITLE%%` | Title of the repair slide | max 6 words | The Correct Fuel Amount |
| `%%NARRATION-EX-0%%` | Spoken intro to the numeric task | 1 sentence | Now let us repair the calculation and enter the correct fuel amount. |
| `%%CORRECT-QUESTION%%` | Numeric question | 1 sentence | How many litres does the van really need? |
| `%%CORRECT-VALUE%%` | Correct value, used in answer and script | number | 15.6 |
| `%%CORRECT-HINT%%` | Hint for the calculation | 1 sentence | Divide the distance by 100 first, then multiply by 6.5. |
| `%%SOLUTION-TEXT%%` | Full correct calculation | 1–2 sentences | 240 ÷ 100 × 6.5 = 15.6 L, so the cost is 15.6 × 1.75 ≈ 27.30 €. |
| `%%NARRATION-EX-1%%` | Spoken intro to the key message | 1 sentence | Here is the habit that catches mistakes like this one. |
| `%%KEY-MESSAGE%%` | Transferable habit | 1–2 sentences | After every step, check whether the result is realistic – a sanity check catches unit errors early. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%CASE-TEXT%%

<!-- data-type="none" -->
| Step | Calculation | Result |
|---|---|---|
| 1 | %%STEP-1-TEXT%% | %%STEP-1-RESULT%% |
| 2 | %%STEP-2-TEXT%% | %%STEP-2-RESULT%% |
| 3 | %%STEP-3-TEXT%% | %%STEP-3-RESULT%% |
| 4 | %%STEP-4-TEXT%% | %%STEP-4-RESULT%% |

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Decide:** %%FIND-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%FIND-CORRECT%%
- [( )] %%FIND-WRONG-1%%
- [( )] %%FIND-WRONG-2%%
- [( )] %%FIND-WRONG-3%%
[[?]] %%FIND-HINT%%
***
%%FIND-FEEDBACK%%
***

****************************************

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

**Type:** %%CORRECT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%CORRECT-VALUE%%]]
[[?]] %%CORRECT-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%CORRECT-VALUE%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%SOLUTION-TEXT%%
***

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

<!-- TEMPLATE:END -->
