<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Closing slide with key takeaways revealed one by one, a remember box, a recap quiz and an outlook.
-->

# Template `Summary_Recap_Template_1`

- **Purpose:** Close a session: repeat the key points, anchor one core idea, check it once, point to the next session.
- **Pairs with:** `Overview_Course_Template_1`, `Interactive_Exercise_Template_1`, `Application_Transfer_Template_1`
- **Variants:** Use three takeaways by deleting step 3 and renumbering. Delete step 5 for a pure summary without quiz.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 5 words | Key Takeaways |
| `%%NARRATION-0%%` | Spoken intro | 1 sentence | Let us sum up what you learned today. |
| `%%NARRATION-1%%` … `%%NARRATION-4%%` | Spoken comment per takeaway | 1 sentence | First, pressure grows with depth. ; Second, only density, gravity and depth matter. ; Third, the vessel shape does not matter. ; And finally, here is the formula to remember. |
| `%%TAKEAWAY-1%%` … `%%TAKEAWAY-4%%` | Takeaway | max 12 words | Pressure in a resting fluid grows linearly with depth. ; It depends on density, gravity and depth only. ; The shape of the vessel does not matter. ; Pressure acts equally in all directions. |
| `%%REMEMBER%%` | One sentence or formula to remember | 1 sentence | $p = \rho \cdot g \cdot h$ |
| `%%NARRATION-5%%` | Spoken intro to the quiz | 1 sentence | One last question. |
| `%%RECAP-QUESTION%%` | Recap question | 1 sentence | Which change doubles the pressure at the bottom of a tank? |
| `%%RECAP-CORRECT%%` | Correct option | max 10 words | Doubling the water depth |
| `%%RECAP-WRONG-1%%`, `%%RECAP-WRONG-2%%` | Wrong options | max 10 words | Doubling the tank width ; Doubling the water surface |
| `%%RECAP-HINT%%` | Hint | 1 sentence | Look at the formula in the box. |
| `%%RECAP-FEEDBACK%%` | Feedback after solving | 1 sentence | Only depth, density and gravity count – not the width. |
| `%%NARRATION-6%%` | Spoken outlook | 1 sentence | Next time we look at fluids in motion. |
| `%%OUTLOOK%%` | Topic of the next session | 1 sentence | Next session: Bernoulli's equation. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
- %%TAKEAWAY-1%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
- %%TAKEAWAY-2%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
- %%TAKEAWAY-3%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
****************************************

- %%TAKEAWAY-4%%

> [!NOTE] Remember
> %%REMEMBER%%

****************************************

    --{{5}}--
%%NARRATION-5%%

      {{5}}
****************************************

**Recap:** %%RECAP-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] %%RECAP-WRONG-1%%
- [( )] %%RECAP-WRONG-2%%
- [(X)] %%RECAP-CORRECT%%
[[?]] %%RECAP-HINT%%
***
%%RECAP-FEEDBACK%%
***

****************************************

    --{{6}}--
%%NARRATION-6%%

      {{6}}
**➡️ Next:** %%OUTLOOK%%

<!-- TEMPLATE:END -->
