<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Video slide that tells learners what to watch for, then checks understanding with a choice and a text quiz.
-->

# Template `Media_Template_1`

- **Purpose:** Present a video with a "Watch for" preview and a text summary, then check understanding with two short quizzes.
- **Pairs with:** `Concept_Explanation_Template_1`, `Interactive_Exercise_Template_1`, `Summary_Recap_Template_1`
- **Variants:** Replace the two watch-for points with a task list `- [ ]` to turn the viewing into a checklist. Add a second quiz step with a true/false matrix for longer videos.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the video slide | max 6 words | The Bridge That Danced |
| `%%NARRATION-0%%` | Spoken intro to the video | 1–2 sentences | We are going to watch a short clip of the Tacoma Narrows Bridge in 1940. |
| `%%VIDEO-URL%%` | Video address (YouTube, Vimeo, file) | 1 line | https://www.youtube.com/watch?v=9UQ9wVwQqYk |
| `%%VIDEO-ALT%%` | Description of the video | max 12 words | Tacoma Narrows Bridge twisting in the wind |
| `%%VIDEO-CAPTION%%` | Source of the video | max 10 words | Public domain, University of Washington |
| `%%WATCH-FOR-1%%` | First thing to watch for | 1 sentence | How the twisting grows from small waves to full rotations. |
| `%%WATCH-FOR-2%%` | Second thing to watch for | 1 sentence | When the deck finally tears apart. |
| `%%SUMMARY-TEXT%%` | Text summary of the video | 2–3 sentences | The deck started to sway in a moderate wind and the motion grew until the bridge collapsed. Engineers later traced it to self-excited oscillation. |
| `%%QUIZ-TITLE%%` | Title of the quiz slide | max 6 words | Check Your Understanding |
| `%%NARRATION-EX-0%%` | Spoken intro to the quiz | 1–2 sentences | Let us check what you saw in the video. |
| `%%SC-QUESTION%%` | Single choice question | 1 sentence | What was the direct cause of the collapse? |
| `%%SC-CORRECT%%` | Correct choice | max 10 words | Growing self-excited oscillation of the deck |
| `%%SC-WRONG-1%%` | Plausible wrong choice | max 10 words | A storm with extreme gusts |
| `%%SC-WRONG-2%%` | Plausible wrong choice | max 10 words | A design error in the cables |
| `%%SC-HINT%%` | Hint for the choice quiz | 1 sentence | Think of a swing that is pushed at just the right moment. |
| `%%SC-FEEDBACK%%` | Feedback after the choice quiz | 1 sentence | Right – the wind fed the motion instead of damping it. |
| `%%NARRATION-EX-1%%` | Spoken intro to the text quiz | 1 sentence | Now name the phenomenon in one word. |
| `%%TA-QUESTION%%` | Text answer question | 1 sentence | What is the name of the phenomenon? |
| `%%TA-ANSWER%%` | Accepted answer | 1–3 words | resonance |
| `%%TA-HINT%%` | Hint for the text quiz | 1 sentence | It is the same effect as a child on a swing. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!TIP] Watch for
> - %%WATCH-FOR-1%%
> - %%WATCH-FOR-2%%

!?[%%VIDEO-ALT%%](%%VIDEO-URL%% "%%VIDEO-CAPTION%%")

<details>
<summary>📝 Text summary</summary>

%%SUMMARY-TEXT%%

</details>

## %%QUIZ-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

**Decide:** %%SC-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%SC-CORRECT%%
- [( )] %%SC-WRONG-1%%
- [( )] %%SC-WRONG-2%%
[[?]] %%SC-HINT%%
***
%%SC-FEEDBACK%%
***

    --{{1}}--
%%NARRATION-EX-1%%

**Type:** %%TA-QUESTION%%

[[%%TA-ANSWER%%]]
[[?]] %%TA-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%TA-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>

<!-- TEMPLATE:END -->
