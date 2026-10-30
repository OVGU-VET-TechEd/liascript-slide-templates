<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Closing slide that collects a text reflection, a can-do checklist and session feedback, then teases the next topic.
-->

# Template `Summary_Recap_Template_3`

- **Purpose:** End a session with a personal reflection, a self-check of what learners can do now, and honest feedback on the session itself.
- **Pairs with:** `Summary_Recap_Template_1`, `Summary_Recap_Template_2`
- **Variants:** Replace the three-line text survey with a one-line `[[___]]` for a faster close. Delete slide 2 if the course ends here.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the reflection slide | max 6 words | Bridges: What Did We Learn? |
| `%%NARRATION-0%%` | Spoken closing intro | 1–2 sentences | Let us close the session with a short reflection. |
| `%%REFLECT-QUESTION%%` | Reflection prompt for the text survey | 1 sentence | What surprised you most about bridge design this week? |
| `%%NARRATION-1%%` | Spoken intro to the can-do list | 1 sentence | Check what you can do now and tick each item. |
| `%%CAN-DO-1%%` … `%%CAN-DO-3%%` | Can-do statement | max 10 words | Explain why arches distribute load ; Choose a bridge type for a given span ; Check a truss for stability |
| `%%NARRATION-2%%` | Spoken intro to the feedback matrix | 1 sentence | Tell us how the session worked for you. |
| `%%FEEDBACK-1%%` … `%%FEEDBACK-4%%` | Feedback statement | max 12 words | The explanations were easy to follow ; The exercises helped me learn ; The pace of the session was good ; I feel ready for the next topic |
| `%%EX-TITLE%%` | Title of the teaser slide | max 6 words | Coming Next: Suspension Bridges |
| `%%NARRATION-EX-0%%` | Spoken teaser intro | 1 sentence | Here is a first look at the next session. |
| `%%IMAGE-PATH%%` | Teaser image | landscape image | assets/images/suspension-bridge.jpg |
| `%%IMAGE-ALT%%` | Description of the image | max 12 words | Main cable and hangers of a suspension bridge |
| `%%IMAGE-CAPTION%%` | Source of the image | max 10 words | Course material, CC BY 4.0 |
| `%%NARRATION-EX-1%%` | Spoken intro to the guiding question | 1–2 sentences | This question will guide our next meeting. |
| `%%NEXT-QUESTION%%` | Question for the next session | 1 sentence | Why can a suspension bridge span farther than a beam bridge? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Reflect:** %%REFLECT-QUESTION%%

[[___ ___ ___]]

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Check now:** Tick what you can do without notes.

- [ ] %%CAN-DO-1%%
- [ ] %%CAN-DO-2%%
- [ ] %%CAN-DO-3%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Rate the session:**

[(1)(2)(3)(4)(5)]
[                    ] %%FEEDBACK-1%%
[                    ] %%FEEDBACK-2%%
[                    ] %%FEEDBACK-3%%
[                    ] %%FEEDBACK-4%%

****************************************

<!-- TEMPLATE:END -->

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
> [!IMPORTANT] Next question
> %%NEXT-QUESTION%%
