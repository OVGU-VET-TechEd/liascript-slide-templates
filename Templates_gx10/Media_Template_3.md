<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Embeds an external simulation, lets learners explore it and then check their reading with a measuring quiz.
-->

# Template `Media_Template_3`

- **Purpose:** Let learners explore an external interactive simulation (PhET, GeoGebra, H5P) and verify their reading of it with a short measuring quiz.
- **Pairs with:** `Media_Template_1`, `Media_Template_2`, `Simulation_Template_1`
- **Variants:** Swap the PhET embed for a GeoGebra applet by changing `%%EMBED-URL%%`. Delete step 2 of slide 2 if only the quiz, not the survey, is wanted.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE-1%%` | Title of the embed slide | max 6 words | Watch a Projectile Fly |
| `%%NARRATION-1-0%%` | Spoken intro to the simulation | 2–3 sentences | Let us open the PhET projectile motion simulator and watch what it does. |
| `%%EMBED-URL%%` | URL of the external simulation | PhET or GeoGebra embed URL | https://phet.colorado.edu/en/simulations/projectile-motion |
| `%%EMBED-TITLE%%` | Accessible name of the embed | max 6 words | Projectile motion simulator |
| `%%NARRATION-1-1%%` | Spoken intro to the explore task | 1 sentence | Now it is your turn to play with the simulation. |
| `%%EXPLORE-TASK%%` | Open exploration task | 1–2 sentences | Launch the ball at 45 degrees and 20 m/s and watch how the path changes when you turn gravity down. |
| `%%SLIDE-TITLE-2%%` | Title of the quiz slide | max 6 words | Measure the Flight Time |
| `%%NARRATION-2-0%%` | Spoken bridge to the quiz | 1–2 sentences | You have explored the simulation, now let us check what you observed. |
| `%%RECAP-TIP%%` | Short recap of what to measure | 1 sentence | Keep the default launch settings and read the stopwatch when the ball lands. |
| `%%NARRATION-2-1%%` | Spoken intro to the measuring question | 1 sentence | Let us measure one thing together. |
| `%%MEASURE-QUESTION%%` | Measuring question with units | 1 sentence | In the default setup, how long does the ball stay in the air in seconds? |
| `%%MEASURE-VALUE%%` | Correct measured value | number without unit | 2.04 |
| `%%MEASURE-HINT%%` | Hint for the quiz | 1 sentence | Use the stopwatch in the simulator and pause the animation at landing. |
| `%%MEASURE-FEEDBACK%%` | Feedback after a correct answer | 1 sentence | Well measured – the flight time is set by the initial height and vertical velocity. |
| `%%NARRATION-2-2%%` | Spoken intro to the survey | 1 sentence | Before we move on, tell me in one sentence what this simulation taught you. |
| `%%SURVEY-QUESTION%%` | Conclusion question for the survey | 1 sentence | In one sentence, what did you learn about how gravity shapes the flight? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE-1%%

    --{{0}}--
%%NARRATION-1-0%%

<iframe src="%%EMBED-URL%%" width="100%" height="480" style="border:0;" allowfullscreen title="%%EMBED-TITLE%%"></iframe>

[Open %%EMBED-TITLE%% in a new tab](%%EMBED-URL%%)

    --{{1}}--
%%NARRATION-1-1%%

      {{1}}
**Explore:** %%EXPLORE-TASK%%

## %%SLIDE-TITLE-2%%

    --{{0}}--
%%NARRATION-2-0%%

> [!TIP] Before you measure
> %%RECAP-TIP%%

    --{{1}}--
%%NARRATION-2-1%%

      {{1}}
**Measure:** %%MEASURE-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%MEASURE-VALUE%%]]
[[?]] %%MEASURE-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%MEASURE-VALUE%%")
// ADAPT: relative tolerance (0.05 = 5 %)
Math.abs(v - ref) <= 0.05 * Math.abs(ref)
</script>
***
%%MEASURE-FEEDBACK%%
***

    --{{2}}--
%%NARRATION-2-2%%

      {{2}}
%%SURVEY-QUESTION%%

[[___]]

<!-- TEMPLATE:END -->
