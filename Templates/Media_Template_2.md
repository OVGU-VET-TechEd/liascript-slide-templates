<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Annotated figure with numbered hotspots explained step by step and a drag and drop labelling task.
-->

# Template `Media_Template_2`

- **Purpose:** Explain the parts of a figure (device, diagram, photo, map) with numbered markers, then let learners label it.
- **Pairs with:** `Content_Introduction_Template_1`, `Concept_Explanation_Template_3`, `Interactive_Exercise_Template_2`
- **Variants:** Marker positions are percentages of the image width (X) and height (Y), measured from the top left corner. Add a distractor card by writing `( %%PART-3%% ) | Distractor` inside the last gap. The image is shown 600 px wide.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the explanation slide | max 5 words | Anatomy of a Barometer |
| `%%NARRATION-0%%` | Spoken intro to the figure | 1–2 sentences | This mercury barometer measures air pressure. Let us look at its three main parts. |
| `%%IMAGE-PATH%%` | Figure | landscape or square | assets/images/barometer.svg |
| `%%IMAGE-ALT%%` | Description of the figure | max 15 words | Glass tube filled with mercury standing upside down in a mercury dish |
| `%%SPOT-1-X%%` … `%%SPOT-3-X%%` | Horizontal marker position | percent | 50% ; 42% ; 50% |
| `%%SPOT-1-Y%%` … `%%SPOT-3-Y%%` | Vertical marker position | percent | 12% ; 55% ; 88% |
| `%%NARRATION-1%%` … `%%NARRATION-3%%` | Spoken explanation per part | 1–2 sentences | At the top of the tube is a vacuum. ; Below it stands a column of mercury. ; The open dish connects the mercury to the outside air. |
| `%%PART-1%%` … `%%PART-3%%` | Name of the part | max 3 words | Vacuum ; Mercury column ; Mercury dish |
| `%%PART-TEXT-1%%` … `%%PART-TEXT-3%%` | Function of the part | max 15 words | Empty space – nothing presses down on the mercury from above. ; Its height (about 760 mm) shows the air pressure. ; Here the air presses on the open mercury surface. |
| `%%LABEL-TITLE%%` | Title of the labelling slide | max 5 words | Label the Barometer |
| `%%NARRATION-LABEL-0%%` | Spoken intro to the labelling task | 1 sentence | Now drag the names onto the right markers. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<div style="position:relative;display:inline-block;width:600px;max-width:100%;">

![%%IMAGE-ALT%%](%%IMAGE-PATH%%)

<span style="position:absolute;left:%%SPOT-1-X%%;top:%%SPOT-1-Y%%;transform:translate(-50%,-50%);background:#c92a2a;color:#fff;border-radius:50%;width:1.8em;height:1.8em;line-height:1.8em;text-align:center;font-weight:bold;">1</span>
<span style="position:absolute;left:%%SPOT-2-X%%;top:%%SPOT-2-Y%%;transform:translate(-50%,-50%);background:#c92a2a;color:#fff;border-radius:50%;width:1.8em;height:1.8em;line-height:1.8em;text-align:center;font-weight:bold;">2</span>
<span style="position:absolute;left:%%SPOT-3-X%%;top:%%SPOT-3-Y%%;transform:translate(-50%,-50%);background:#c92a2a;color:#fff;border-radius:50%;width:1.8em;height:1.8em;line-height:1.8em;text-align:center;font-weight:bold;">3</span>

</div>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
**① %%PART-1%%:** %%PART-TEXT-1%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
**② %%PART-2%%:** %%PART-TEXT-2%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
**③ %%PART-3%%:** %%PART-TEXT-3%%

## %%LABEL-TITLE%%

    --{{0}}--
%%NARRATION-LABEL-0%%

<div style="position:relative;display:inline-block;width:600px;max-width:100%;">

![%%IMAGE-ALT%%](%%IMAGE-PATH%%)

<span style="position:absolute;left:%%SPOT-1-X%%;top:%%SPOT-1-Y%%;transform:translate(-50%,-50%);background:#c92a2a;color:#fff;border-radius:50%;width:1.8em;height:1.8em;line-height:1.8em;text-align:center;font-weight:bold;">1</span>
<span style="position:absolute;left:%%SPOT-2-X%%;top:%%SPOT-2-Y%%;transform:translate(-50%,-50%);background:#c92a2a;color:#fff;border-radius:50%;width:1.8em;height:1.8em;line-height:1.8em;text-align:center;font-weight:bold;">2</span>
<span style="position:absolute;left:%%SPOT-3-X%%;top:%%SPOT-3-Y%%;transform:translate(-50%,-50%);background:#c92a2a;color:#fff;border-radius:50%;width:1.8em;height:1.8em;line-height:1.8em;text-align:center;font-weight:bold;">3</span>

</div>

**Label:** Drag each name to its number.

<!-- data-randomize data-show-partial-solution data-solution-button="2" -->
① [->[ %%PART-1%% ]] ② [->[ %%PART-2%% ]] ③ [->[ %%PART-3%% ]]

<!-- TEMPLATE:END -->
