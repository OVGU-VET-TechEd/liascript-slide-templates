<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Start content block that poses a bold guiding question, reveals four aspects one per step and asks a self-assessment survey.

import:   none
-->

# Template `Content_Introduction_Template_2`

- **Purpose:** Start a content block with a bold guiding question, walk through the four aspects of the topic one by one and let learners self-assess their prior knowledge.
- **Pairs with:** `Overview_Course_Template_2`, `Content_DeepDive_Template_1`, `Application_Transfer_Template_1`
- **Variants:** Replace the four aspects with a numbered list of 3 or 5 items and adjust the survey options accordingly. Swap the TIP callout for an IMPORTANT callout when the topic carries a compliance or safety angle.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the content block | max 6 words | Making Online Meetings Accessible |
| `%%NARRATION-0%%` | Spoken welcome and framing | 1–2 sentences | Let us look at how online meetings can work for every participant. |
| `%%GUIDING-QUESTION%%` | Bold guiding question of the block | 1 sentence | What does it take to make an online meeting truly accessible? |
| `%%NARRATION-1%%` | Spoken intro to aspect 1 | 1 sentence | First, let us look at how people follow the spoken content. |
| `%%ASPECT-1%%` | First aspect of the topic | max 10 words | Live captions and a written transcript |
| `%%NARRATION-2%%` | Spoken intro to aspect 2 | 1 sentence | Second, think about participants who rely on a screen reader. |
| `%%ASPECT-2%%` | Second aspect of the topic | max 10 words | Screen-reader-friendly slides and controls |
| `%%NARRATION-3%%` | Spoken intro to aspect 3 | 1 sentence | Third, check whether everything can be driven without a mouse. |
| `%%ASPECT-3%%` | Third aspect of the topic | max 10 words | Keyboard shortcuts for chat and polls |
| `%%NARRATION-4%%` | Spoken intro to aspect 4 | 1 sentence | Finally, make sure the visuals work for low-vision users. |
| `%%ASPECT-4%%` | Fourth aspect of the topic | max 10 words | Sufficient color contrast and clear icons |
| `%%NARRATION-5%%` | Spoken transition to the tip | 1 sentence | Here is why this matters beyond our course. |
| `%%TIP-WHY-IT-MATTERS%%` | Why the topic matters | 1–2 sentences | Accessible meetings include colleagues with visual, hearing or motor impairments. They are also a legal requirement in many institutions. |
| `%%NARRATION-6%%` | Spoken intro to the survey | 1 sentence | Now, be honest about where you stand. |
| `%%SURVEY-LABEL%%` | Survey question shown above the options | 1 sentence | Which of these do you already know? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Guiding question:** %%GUIDING-QUESTION%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
- %%ASPECT-1%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
- %%ASPECT-2%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
- %%ASPECT-3%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
- %%ASPECT-4%%

    --{{5}}--
%%NARRATION-5%%

      {{5}}
> [!TIP] Why it matters
> %%TIP-WHY-IT-MATTERS%%

    --{{6}}--
%%NARRATION-6%%

      {{6}}
****************************************

**Decide:** %%SURVEY-LABEL%%

[[a1]] %%ASPECT-1%%
[[a2]] %%ASPECT-2%%
[[a3]] %%ASPECT-3%%
[[a4]] %%ASPECT-4%%

****************************************

<!-- TEMPLATE:END -->
