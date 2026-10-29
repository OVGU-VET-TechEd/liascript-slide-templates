<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Closing with reflection prompts, a can-do checklist, a feedback matrix survey and a teaser for the next session.
-->

# Template `Summary_Recap_Template_3`

- **Purpose:** End a session with personal reflection, self-assessment and anonymous feedback, then build curiosity for next time.
- **Pairs with:** `Overview_Course_Template_3`, `Application_Transfer_Template_3`, `Introduction_Template_1`
- **Variants:** Add checklist lines or feedback rows as needed. Delete the teaser slide at the end of a course. Ticks in the checklist are saved in the learner's browser, so learners can come back to them.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the reflection slide | max 5 words | Look Back |
| `%%NARRATION-0%%` | Spoken intro to the reflection | 1 sentence | Take two minutes to look back on today. |
| `%%NARRATION-1%%` | Spoken intro to the checklist | 1 sentence | Tick what you can do now. |
| `%%CAN-DO-1%%` … `%%CAN-DO-3%%` | Can-do statement | max 12 words | I can calculate the pressure at a given depth. ; I can explain why the vessel shape does not matter. ; I can convert between Pa, kPa and bar. |
| `%%NARRATION-2%%` | Spoken intro to the feedback | 1 sentence | Finally, tell me how the session worked for you. |
| `%%TEASER-TITLE%%` | Title of the teaser slide | max 5 words | Next Time |
| `%%NARRATION-TEASER-0%%` | Spoken teaser | 1–2 sentences | Next week we find out why aircraft can fly. |
| `%%IMAGE-PATH%%` | Teaser picture | landscape | assets/images/wing.jpg |
| `%%IMAGE-ALT%%` | Description | max 12 words | Air flowing around an aircraft wing |
| `%%IMAGE-CAPTION%%` | Caption or credit | max 10 words | Photo: J. Doe, CC BY 4.0 |
| `%%TEASER-QUESTION%%` | Question for next time | 1 sentence | How can 400 tonnes of metal stay in the air? |
| `%%NEXT-DATE%%` | Date or session number | short | Session 5 · 12 November |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

**Reflect:** What is the most important thing you learned today – and what is still unclear?

[[___ ___ ___]]

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Tick:** What can you do now?

- [ ] %%CAN-DO-1%%
- [ ] %%CAN-DO-2%%
- [ ] %%CAN-DO-3%%

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Feedback:** How did this session work for you?

[(1 agree)(2 rather agree)(3 neutral)(4 rather disagree)(5 disagree)]
[                                                                   ] The pace was appropriate.
[                                                                   ] The explanations were clear.
[                                                                   ] The examples helped me understand.
[                                                                   ] The interactive parts were useful.

****************************************

## %%TEASER-TITLE%%

    --{{0}}--
%%NARRATION-TEASER-0%%

<!-- style="max-width:100%;width:60%;display:block;margin:0 auto;" -->
![%%IMAGE-ALT%%](%%IMAGE-PATH%% "%%IMAGE-CAPTION%%")

> [!IMPORTANT] Think about it until next time
> %%TEASER-QUESTION%%

*%%NEXT-DATE%%*

<!-- TEMPLATE:END -->
