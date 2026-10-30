<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Closing slide that walks through four takeaways, adds a remember box and an outlook, then checks the main idea with one quiz.
-->

# Template `Summary_Recap_Template_1`

- **Purpose:** Close a session by revealing the four key takeaways one by one, pinning one thing to remember, and checking the main idea with a quick quiz.
- **Pairs with:** `Application_Transfer_Template_3`, `Summary_Recap_Template_2`, `Summary_Recap_Template_3`
- **Variants:** Merge the NOTE box and the outlook into one step if time is short. Replace the recap quiz with a task list `- [ ]` to end on a self-check.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the recap slide | max 6 words | What You Take Home Today |
| `%%NARRATION-0%%` | Spoken opening of the recap | 1–2 sentences | Let us collect what we have built today before we finish. |
| `%%TAKEAWAY-1%%` | First key takeaway | 1 sentence | A moderate wind can excite a bridge that is built to carry heavy loads. |
| `%%TAKEAWAY-2%%` | Second key takeaway | 1 sentence | Resonance grows when the push repeats at the natural frequency. |
| `%%TAKEAWAY-3%%` | Third key takeaway | 1 sentence | Damping limits the amplitude of the oscillation. |
| `%%TAKEAWAY-4%%` | Fourth key takeaway | 1 sentence | Engineers check wind loads against oscillation, not just static weight. |
| `%%NARRATION-1%%` | Spoken reveal of takeaway 1 | 1 sentence | First, the wind that seemed harmless was the real load case. |
| `%%NARRATION-2%%` | Spoken reveal of takeaway 2 | 1 sentence | Second, this happened because the push matched the natural frequency. |
| `%%NARRATION-3%%` | Spoken reveal of takeaway 3 | 1 sentence | Third, damping is what keeps the motion in check. |
| `%%NARRATION-4%%` | Spoken reveal of takeaway 4 | 1 sentence | Fourth, we now check wind against oscillation in our design. |
| `%%NARRATION-5%%` | Spoken close: remember box and outlook | 1–2 sentences | Here is the one thing to remember, and here is where we go next. |
| `%%REMEMBER%%` | The one thing to remember | 1–2 sentences | Resonance is not about strength but about frequency. If the push matches the natural frequency, even a small force grows the motion. |
| `%%OUTLOOK%%` | Outlook to the next session | 1 sentence | Next time we design a damper and test it in the simulation. |
| `%%RECAP-TITLE%%` | Title of the recap quiz slide | max 4 words | Last Check |
| `%%NARRATION-6%%` | Spoken intro to the recap quiz | 1 sentence | One last check to make sure the main idea is clear. |
| `%%RECAP-QUESTION%%` | Recap question | 1 sentence | Which sentence captures the main idea of today's session? |
| `%%RECAP-CORRECT%%` | Correct recap sentence | max 15 words | A small repeated push at the natural frequency can grow a large oscillation. |
| `%%RECAP-WRONG-1%%` | Plausible wrong sentence | max 15 words | A bridge fails only when the total load exceeds its strength. |
| `%%RECAP-WRONG-2%%` | Plausible wrong sentence | max 15 words | Wind loads matter only for very tall buildings. |
| `%%RECAP-HINT%%` | Hint | 1 sentence | Think of a swing that is pushed at just the right moment. |
| `%%RECAP-FEEDBACK%%` | Short feedback after answering | 1 sentence | Right – frequency matching, not raw strength, was the core of today. |

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
- %%TAKEAWAY-4%%

    --{{5}}--
%%NARRATION-5%%

      {{5}}
****************************************

> [!NOTE] Remember
> %%REMEMBER%%

**Outlook:** %%OUTLOOK%%

****************************************

## %%RECAP-TITLE%%

    --{{0}}--
%%NARRATION-6%%

      {{1}}
**Decide:** %%RECAP-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%RECAP-CORRECT%%
- [( )] %%RECAP-WRONG-1%%
- [( )] %%RECAP-WRONG-2%%
[[?]] %%RECAP-HINT%%
***
%%RECAP-FEEDBACK%%
***

<!-- TEMPLATE:END -->
