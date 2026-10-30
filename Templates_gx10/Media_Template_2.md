<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Annotated figure with numbered hotspots and a drag-and-drop labelling task.
-->

# Template `Media_Template_2`

- **Purpose:** Annotate a figure with numbered hotspots, explain each part one per step, then let learners label the same figure.
- **Pairs with:** `Media_Template_1`, `Media_Template_3`, `Concept_Explanation_Template_3`
- **Variants:** Use a diagram or a photo instead of the technical figure. Add a fourth badge if a fourth part matters.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the annotated figure slide | max 6 words | Reading a Suspension Bridge |
| `%%NARRATION-0%%` | Spoken intro to the figure | 1–2 sentences | Here is a cross-section of a suspension bridge with three numbered points. |
| `%%NARRATION-1%%` … `%%NARRATION-3%%` | Spoken text for each part | 1–2 sentences | Point one marks the tower. ; Point two marks the main cable. ; Point three marks the deck. |
| `%%NARRATION-4%%` | Spoken line for the key message | 1 sentence | Together the parts form one load path. |
| `%%IMAGE-PATH%%` | Image of the figure | landscape image | assets/images/bridge-section.png |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Cross-section of a suspension bridge |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | Public domain, Wikimedia Commons |
| `%%HOTSPOT-1-X%%`, `%%HOTSPOT-1-Y%%` | Percent position of badge 1 | 0–100 | 20 ; 35 |
| `%%HOTSPOT-2-X%%`, `%%HOTSPOT-2-Y%%` | Percent position of badge 2 | 0–100 | 50 ; 20 |
| `%%HOTSPOT-3-X%%`, `%%HOTSPOT-3-Y%%` | Percent position of badge 3 | 0–100 | 80 ; 70 |
| `%%PART-1-NAME%%` … `%%PART-3-NAME%%` | Name of a part | max 3 words | Tower ; Main cable ; Deck |
| `%%PART-1-TEXT%%` … `%%PART-3-TEXT%%` | One-sentence explanation of a part | 1 sentence | The tower carries the cable. ; The cable holds the deck. ; The deck carries traffic. |
| `%%KEY-MESSAGE%%` | Key message | 1 sentence | Load path: deck to cable to tower to foundation. |
| `%%EX-TITLE%%` | Title of the labelling slide | max 6 words | Label the Parts |
| `%%NARRATION-EX-0%%` | Spoken intro to the labelling task | 1 sentence | Now label the three parts yourself. |
| `%%NARRATION-EX-1%%` | Spoken instruction for the drag task | 1 sentence | Drag each name onto its number. |

The labelling task on slide 2 uses one shared drag-and-drop pool: each number on the figure is a drop target and the three part names are the cards.

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<div style="position:relative;display:inline-block;width:600px;max-width:100%;">
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")
<span style="position:absolute;left:%%HOTSPOT-1-X%%%;top:%%HOTSPOT-1-Y%%%;transform:translate(-50%,-50%);background:#1f4e79;color:#fff;border-radius:50%;width:28px;height:28px;line-height:28px;text-align:center;font-weight:bold;">1</span>
<span style="position:absolute;left:%%HOTSPOT-2-X%%%;top:%%HOTSPOT-2-Y%%%;transform:translate(-50%,-50%);background:#1f4e79;color:#fff;border-radius:50%;width:28px;height:28px;line-height:28px;text-align:center;font-weight:bold;">2</span>
<span style="position:absolute;left:%%HOTSPOT-3-X%%%;top:%%HOTSPOT-3-Y%%%;transform:translate(-50%,-50%);background:#1f4e79;color:#fff;border-radius:50%;width:28px;height:28px;line-height:28px;text-align:center;font-weight:bold;">3</span>
</div>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
**%%PART-1-NAME%%:** %%PART-1-TEXT%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
**%%PART-2-NAME%%:** %%PART-2-TEXT%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
**%%PART-3-NAME%%:** %%PART-3-TEXT%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

<div style="position:relative;display:inline-block;width:600px;max-width:100%;">
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")
<span style="position:absolute;left:%%HOTSPOT-1-X%%%;top:%%HOTSPOT-1-Y%%%;transform:translate(-50%,-50%);background:#1f4e79;color:#fff;border-radius:50%;width:28px;height:28px;line-height:28px;text-align:center;font-weight:bold;">1</span>
<span style="position:absolute;left:%%HOTSPOT-2-X%%%;top:%%HOTSPOT-2-Y%%%;transform:translate(-50%,-50%);background:#1f4e79;color:#fff;border-radius:50%;width:28px;height:28px;line-height:28px;text-align:center;font-weight:bold;">2</span>
<span style="position:absolute;left:%%HOTSPOT-3-X%%%;top:%%HOTSPOT-3-Y%%%;transform:translate(-50%,-50%);background:#1f4e79;color:#fff;border-radius:50%;width:28px;height:28px;line-height:28px;text-align:center;font-weight:bold;">3</span>
</div>

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
****************************************

**Label:** Drag each name onto the matching number.

<!-- data-randomize data-show-partial-solution -->
1: [->[ %%PART-1-NAME%% ]]   2: [->[ %%PART-2-NAME%% ]]   3: [->[ %%PART-3-NAME%% ]]

****************************************

<!-- TEMPLATE:END -->
