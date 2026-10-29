<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Opening slide that starts from a real-life case, lets learners predict the outcome and then reveals it.
-->

# Template `Introduction_Template_3`

- **Purpose:** Hook the audience with a real event (history, news, accident, product, everyday situation) before naming the topic.
- **Pairs with:** `Overview_Course_Template_2`, `Content_Introduction_Template_3`, `Application_Transfer_Template_1`
- **Variants:** Replace the image with a video line `!?[alt](url)`. Delete step 3 if the outcome should stay open until later.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Catchy title of the case | max 6 words | The Bridge That Danced |
| `%%NARRATION-0%%` | Spoken story opener | 2–3 sentences | In 1940 a brand-new bridge in Tacoma started to swing in a moderate wind. |
| `%%IMAGE-PATH%%` | Image of the case | landscape image | assets/images/tacoma.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Twisting deck of a suspension bridge |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | Public domain, Wikimedia Commons |
| `%%CASE-TEXT%%` | The story in short | 2–3 sentences | Four months after opening, the deck of the Tacoma Narrows Bridge began to twist in a wind of about 60 km/h. |
| `%%NARRATION-1%%` | Spoken guiding question | 1–2 sentences | So here is the question that will guide us today. |
| `%%GUIDING-QUESTION%%` | Question the session answers | 1 sentence | Why can a moderate wind destroy a steel bridge? |
| `%%NARRATION-2%%` | Spoken intro to the prediction | 1 sentence | What do you think happened next? |
| `%%PREDICT-QUESTION%%` | Prediction question | 1 sentence | What happened to the bridge that day? |
| `%%PREDICT-CORRECT%%` | Correct prediction | max 10 words | It collapsed within about an hour |
| `%%PREDICT-WRONG-1%%` | Plausible wrong prediction | max 10 words | It calmed down when the wind dropped |
| `%%PREDICT-WRONG-2%%` | Plausible wrong prediction | max 10 words | It was closed and survived undamaged |
| `%%PREDICT-HINT%%` | Hint | 1 sentence | Think of a swing that is pushed at just the right moment. |
| `%%PREDICT-FEEDBACK%%` | Short feedback after answering | 1 sentence | Right – the twisting grew until the deck broke. |
| `%%NARRATION-3%%` | Spoken reveal | 1–2 sentences | The deck tore apart and fell into the water. |
| `%%OUTCOME%%` | What really happened, link to topic | 2 sentences | The deck collapsed the same day. The cause – self-excited oscillation – is our topic. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

%%CASE-TEXT%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
> [!IMPORTANT] Guiding question
> %%GUIDING-QUESTION%%

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Predict:** %%PREDICT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%PREDICT-CORRECT%%
- [( )] %%PREDICT-WRONG-1%%
- [( )] %%PREDICT-WRONG-2%%
[[?]] %%PREDICT-HINT%%
***
%%PREDICT-FEEDBACK%%
***

****************************************

    --{{3}}--
%%NARRATION-3%%

      {{3}}
> [!NOTE] What really happened
> %%OUTCOME%%

<!-- TEMPLATE:END -->
