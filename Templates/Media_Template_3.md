<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Embedded external simulation (PhET, GeoGebra, H5P) with guided tasks, a measured value check and a conclusion.
-->

# Template `Media_Template_3`

- **Purpose:** Guide learners through an external interactive simulation with concrete tasks instead of free play.
- **Pairs with:** `Concept_Explanation_Template_1`, `Simulation_Template_1`, `Summary_Recap_Template_1`
- **Variants:** Any page that allows embedding works (PhET HTML5 sims, GeoGebra applets, H5P). Change the height in the iframe line (default 480 px). If a site blocks embedding, learners use the link below the frame.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 6 words | Experiment: Pressure Under Water |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | In this simulation you can measure pressure in a pool yourself. |
| `%%EMBED-URL%%` | URL of the simulation | URL | https://phet.colorado.edu/sims/html/under-pressure/latest/under-pressure_en.html |
| `%%EMBED-TITLE%%` | Name and source of the simulation | max 10 words | PhET Under Pressure, University of Colorado, CC BY 4.0 |
| `%%NARRATION-1%%` | Spoken task 1 | 1 sentence | First, get to know the controls. |
| `%%TASK-1%%` | Exploration task | 1–2 sentences | Fill the pool and drag the pressure gauge to the surface, then to the bottom. |
| `%%NARRATION-2%%` | Spoken task 2 | 1 sentence | Now measure one value exactly. |
| `%%TASK-2%%` | Measuring task with numeric answer | 1–2 sentences | Turn the atmosphere off and read the pressure at 3 m depth in kPa. |
| `%%MEASURE-ANSWER%%` | Expected value, dot as decimal sign | number | 29.4 |
| `%%MEASURE-HINT%%` | Hint | 1 sentence | Use the ruler to place the gauge exactly 3 m below the surface. |
| `%%MEASURE-FEEDBACK%%` | Feedback after solving | 1 sentence | 1000 · 9.8 · 3 Pa ≈ 29.4 kPa – the simulation agrees with the formula. |
| `%%NARRATION-3%%` | Spoken intro to the conclusion | 1 sentence | What do you conclude? |
| `%%CONCLUSION-QUESTION%%` | Conclusion question | 1 sentence | How does the pressure change with depth, and what changes when you switch the fluid to honey? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<iframe src="%%EMBED-URL%%" width="100%" height="480" style="border:0;" allowfullscreen title="%%EMBED-TITLE%%"></iframe>

*%%EMBED-TITLE%%* · [Open in a new tab](%%EMBED-URL%%)

    --{{1}}--
%%NARRATION-1%%

      {{1}}
**Task 1 · Explore:** %%TASK-1%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Task 2 · Measure:** %%TASK-2%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%MEASURE-ANSWER%%]]
[[?]] %%MEASURE-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%MEASURE-ANSWER%%")
// ADAPT: relative tolerance (0.05 = 5 %, reading values off a simulation is imprecise)
Math.abs(v - ref) <= 0.05 * Math.abs(ref)
</script>
***
%%MEASURE-FEEDBACK%%
***

****************************************

    --{{3}}--
%%NARRATION-3%%

      {{3}}
****************************************

**Conclude:** %%CONCLUSION-QUESTION%%

[[___ ___ ___]]

****************************************

<!-- TEMPLATE:END -->
