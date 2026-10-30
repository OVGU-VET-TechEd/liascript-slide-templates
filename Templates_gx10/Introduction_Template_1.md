<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Opening slide with a title image, a short welcome, the session goals and a familiarity survey.
-->

# Template `Introduction_Template_1`

- **Purpose:** Open a session with a title image, a short welcome, the session goals and a quick familiarity check.
- **Pairs with:** `Overview_Course_Template_1`, `Content_Introduction_Template_1`
- **Variants:** Replace the image with a video line `!?[alt](url)`. Swap the survey for a one-line text survey `[[___]]` if the group is very small.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the session | max 6 words | Tidal Energy Basics |
| `%%NARRATION-0%%` | Spoken welcome | 2–3 sentences | Welcome to the first session of the course. |
| `%%IMAGE-PATH%%` | Large title image | landscape image | assets/images/tidal-turbines.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Tidal turbine array in a shallow bay at low tide |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | Public domain, Wikimedia Commons |
| `%%WELCOME-TEXT%%` | Welcome text on the slide | 2–3 sentences | Welcome to Tidal Energy Basics. Over the next four sessions we will turn the ocean's daily rhythm into usable power. This first session sets up the vocabulary and the goals. |
| `%%SPEAKER-LINE%%` | Speaker and affiliation | max 12 words | Dr. Lena Hart, Coastal Engineering Lab |
| `%%NARRATION-1%%` | Spoken intro to the goals | 1 sentence | Here is what we will build up together today. |
| `%%GOAL-1%%` | First session goal | max 12 words | Explain how tides and tidal currents arise |
| `%%GOAL-2%%` | Second session goal | max 12 words | Compare tidal and wave energy systems |
| `%%GOAL-3%%` | Third session goal | max 12 words | Evaluate a real tidal project by its site data |
| `%%NARRATION-2%%` | Spoken intro to the survey | 1 sentence | Before we start, I would like to know where you are coming from. |
| `%%TOPIC%%` | Topic of the session | max 6 words | tidal energy |
| `%%LEVEL-1%%` | Survey label for level 1 | max 12 words | New to the topic |
| `%%LEVEL-2%%` | Survey label for level 2 | max 12 words | I know some of the terms |
| `%%LEVEL-3%%` | Survey label for level 3 | max 12 words | I can explain the basic ideas |
| `%%LEVEL-4%%` | Survey label for level 4 | max 12 words | I have studied it before |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

%%WELCOME-TEXT%%

**Speaker:** %%SPEAKER-LINE%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Today you will**

- %%GOAL-1%%
- %%GOAL-2%%
- %%GOAL-3%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Decide:** How familiar are you with %%TOPIC%%?

- [(1)] %%LEVEL-1%%
- [(2)] %%LEVEL-2%%
- [(3)] %%LEVEL-3%%
- [(4)] %%LEVEL-4%%

****************************************

<!-- TEMPLATE:END -->
