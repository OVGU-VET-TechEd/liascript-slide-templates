<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Start of a content block with a picture next to an intro text, a key message and an activation question.
-->

# Template `Content_Introduction_Template_1`

- **Purpose:** Open a new topic with a picture and a short text, then activate prior knowledge with one typed answer.
- **Pairs with:** `Overview_Course_Template_1`, `Concept_Explanation_Template_1`, `Concept_Explanation_Template_3`
- **Variants:** Swap the two inner div blocks to put the picture on the right. Delete step 2 if no activation question is needed. Accepted spellings of the answer can be added in the script line marked ADAPT.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Topic of the new block | max 6 words | Hydrostatic Pressure |
| `%%NARRATION-0%%` | Spoken intro | 2–3 sentences | Dive three metres deep and your ears start to hurt. Why is that? |
| `%%IMAGE-PATH%%` | Picture for the topic | portrait or square | assets/images/diver.jpg |
| `%%IMAGE-ALT%%` | Description of the picture | max 12 words | Diver holding her nose at three metres depth |
| `%%IMAGE-CAPTION%%` | Caption or credit | max 10 words | Photo: J. Doe, CC BY 4.0 |
| `%%INTRO-TEXT%%` | Intro text beside the picture | 3–4 sentences | Water presses on everything inside it. The deeper you go, the more water lies above you. |
| `%%NARRATION-1%%` | Spoken key message | 1 sentence | Keep one idea in mind. |
| `%%KEY-MESSAGE%%` | Core idea of the block | 1 sentence | Pressure in a fluid grows with depth. |
| `%%NARRATION-2%%` | Spoken intro to the question | 1 sentence | A quick check before we start. |
| `%%ACTIVATION-QUESTION%%` | Question with a one-word answer | 1 sentence | What is the SI unit of pressure? |
| `%%ACTIVATION-ANSWER%%` | Expected answer | 1–2 words | Pascal |
| `%%ACTIVATION-HINT%%` | Hint | 1 sentence | It is named after a French scientist. |
| `%%ACTIVATION-FEEDBACK%%` | Feedback after answering | 1 sentence | Yes: 1 Pa = 1 N/m². |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<div style="display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center;">
<div style="flex:1 1 260px;">

![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

</div>
<div style="flex:2 1 320px;">

%%INTRO-TEXT%%

</div>
</div>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Type:** %%ACTIVATION-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%ACTIVATION-ANSWER%%]]
[[?]] %%ACTIVATION-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%ACTIVATION-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>
***
%%ACTIVATION-FEEDBACK%%
***

****************************************

<!-- TEMPLATE:END -->
