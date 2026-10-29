<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Video slide with watch-for questions before viewing and two check questions afterwards.
-->

# Template `Media_Template_1`

- **Purpose:** Use a video actively: learners know what to look for, watch, and then answer two questions about it.
- **Pairs with:** `Content_Introduction_Template_2`, `Concept_Explanation_Template_2`, `Interactive_Exercise_Template_1`
- **Variants:** Works with YouTube, Vimeo or a video file (assets/video/clip.mp4). Add a start time to YouTube links with ?start=SECONDS.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 6 words | Watch: The Tacoma Narrows Collapse |
| `%%NARRATION-0%%` | Spoken intro to the video | 1–2 sentences | Watch the original film from 1940. Pay attention to two things. |
| `%%WATCH-FOR-1%%`, `%%WATCH-FOR-2%%` | What to look for | 1 sentence | How does the movement of the deck change over time? ; What happens just before the deck breaks? |
| `%%VIDEO-URL%%` | Link to the video | URL | https://www.youtube.com/watch?v=j-zczJXSxnw |
| `%%VIDEO-ALT%%` | Short description of the video | max 12 words | Archive film of a suspension bridge twisting and collapsing |
| `%%VIDEO-CAPTION%%` | Source and length | max 12 words | Archive footage, 1940 · 4 min |
| `%%VIDEO-SUMMARY%%` | Text summary for learners without sound or video | 2–3 sentences | The deck first swings up and down, then begins to twist until it breaks. |
| `%%NARRATION-1%%` | Spoken intro to question 1 | 1 sentence | What did you notice? |
| `%%Q1-QUESTION%%` | Single-choice question on the video | 1 sentence | Which movement finally destroyed the bridge? |
| `%%Q1-CORRECT%%` | Correct option | max 10 words | A twisting (torsional) movement |
| `%%Q1-WRONG-1%%`, `%%Q1-WRONG-2%%` | Wrong options | max 10 words | A slow sideways drift ; A sinking of the towers |
| `%%Q1-HINT%%` | Hint | 1 sentence | Watch the yellow centre line in the last minute. |
| `%%Q1-FEEDBACK%%` | Feedback after solving | 1 sentence | The deck twisted around its long axis until hangers failed. |
| `%%NARRATION-2%%` | Spoken intro to question 2 | 1 sentence | And one term to remember. |
| `%%Q2-QUESTION%%` | Text question on the video | 1 sentence | Which phenomenon makes small regular pushes grow into large oscillations? |
| `%%Q2-ANSWER%%` | Expected answer, case does not matter | 1–2 words | resonance |
| `%%Q2-HINT%%` | Hint | 1 sentence | Think of pushing a swing at the right moment. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!TIP] Watch for
> 1. %%WATCH-FOR-1%%
> 2. %%WATCH-FOR-2%%

!?[%%VIDEO-ALT%%](%%VIDEO-URL%% "%%VIDEO-CAPTION%%")

<details>

<summary>Text summary of the video</summary>

%%VIDEO-SUMMARY%%

</details>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Decide:** %%Q1-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] %%Q1-WRONG-1%%
- [(X)] %%Q1-CORRECT%%
- [( )] %%Q1-WRONG-2%%
[[?]] %%Q1-HINT%%
***
%%Q1-FEEDBACK%%
***

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Type:** %%Q2-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%Q2-ANSWER%%]]
[[?]] %%Q2-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%Q2-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>

****************************************

<!-- TEMPLATE:END -->
