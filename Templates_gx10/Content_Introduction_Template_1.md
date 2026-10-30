<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Starts a content block with a picture beside short text and checks the central term.
-->

# Template `Content_Introduction_Template_1`

- **Purpose:** Open a content block by showing the topic as image and short text side by side and checking the key term.
- **Pairs with:** `Introduction_Template_3`, `Concept_Explanation_Template_1`, `Interactive_Exercise_Template_1`
- **Variants:** Replace the flex div with a full-width image line plus text below. Swap the text answer quiz for a single choice with hint and feedback.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the content block | max 6 words | Why Current Needs a Brake |
| `%%NARRATION-0%%` | Spoken intro to the topic | 2–3 sentences | We start with the first building block of every circuit. Watch how a simple loop already contains a limit. |
| `%%IMAGE-PATH%%` | Image of the topic | landscape image | assets/images/circuit-loop.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Simple battery and bulb circuit on a breadboard |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | CC BY 4.0, OpenStax |
| `%%INTRO-TEXT%%` | Short text beside the image | 2–3 sentences | A battery pushes charge around a closed loop. The bulb turns on, but only a limited amount of charge flows per second. Something in the loop slows the charge down. |
| `%%NARRATION-1%%` | Spoken intro to the key message | 1 sentence | Here is the idea to keep in mind for the whole block. |
| `%%KEY-MESSAGE%%` | Central statement of the block | 1–2 sentences | Every circuit limits the current. This limit is called resistance, and it is measured in ohms. |
| `%%NARRATION-2%%` | Spoken intro to the check | 1 sentence | Let me check whether this term already means something to you. |
| `%%Q1-QUESTION%%` | Check question | 1 sentence | What is the name for the opposition to the flow of charge? |
| `%%Q1-ANSWER%%` | Accepted answer, one word | 1–2 words, no quotes | resistance |
| `%%Q1-HINT%%` | Hint after a wrong try | 1 sentence | The symbol for it is the Greek letter omega. |
| `%%Q1-FEEDBACK%%` | Feedback after a correct answer | 1 sentence | Exactly – resistance, measured in ohms, is what limits the current. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<div style="display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center;">
<div style="flex:1 1 260px;">

![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

</div>
<div style="flex:1 1 260px;">

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

**Type:** %%Q1-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%Q1-ANSWER%%]]
[[?]] %%Q1-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%Q1-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>
***
%%Q1-FEEDBACK%%
***

****************************************

<!-- TEMPLATE:END -->
