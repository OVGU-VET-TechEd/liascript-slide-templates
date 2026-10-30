<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  One knowledge-check slide that reveals a single choice, a multiple choice and a text answer one per step.
-->

# Template `Interactive_Exercise_Template_1`

- **Purpose:** Check understanding of the just-taught topic with three short questions of different types on one slide.
- **Pairs with:** `Concept_Explanation_Template_1`, `Summary_Recap_Template_1`, `Interactive_Exercise_Template_2`
- **Variants:** Replace the text answer with a numeric answer with tolerance. Reveal all three quizzes together in one step instead of one per step.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the knowledge check | max 6 words | Check Your Resonance Knowledge |
| `%%NARRATION-0%%` | Spoken intro to the quiz round | 1–2 sentences | Let us see what the bridge story has already taught us. |
| `%%Q1-STEM%%` | Question text of the single choice | 1 sentence | What does resonance amplify in an oscillating system? |
| `%%Q1-CORRECT%%` | Correct option | max 10 words | The amplitude of the oscillation |
| `%%Q1-WRONG-1%%` | Plausible wrong option | max 10 words | The frequency of the oscillation |
| `%%Q1-WRONG-2%%` | Plausible wrong option | max 10 words | The damping of the oscillation |
| `%%Q1-HINT%%` | Hint for the single choice | 1 sentence | Think of a swing that gets higher and higher. |
| `%%Q1-FEEDBACK%%` | Short feedback after answering | 1 sentence | Yes – resonance makes the swings grow larger and larger. |
| `%%NARRATION-1%%` | Spoken intro to the multiple choice | 1 sentence | Now pick all the conditions that resonance needs. |
| `%%Q2-STEM%%` | Question text of the multiple choice | 1 sentence | Which conditions are needed for resonance to build up? |
| `%%Q2-CORRECT-1%%` | Correct option | max 10 words | The driving frequency matches the natural frequency |
| `%%Q2-CORRECT-2%%` | Correct option | max 10 words | Repeated energy input keeps the oscillation growing |
| `%%Q2-WRONG-1%%` | Plausible wrong option | max 10 words | A large amplitude from the start |
| `%%Q2-WRONG-2%%` | Plausible wrong option | max 10 words | Strong damping of the system |
| `%%Q2-HINT%%` | Hint for the multiple choice | 1 sentence | Resonance needs a matching frequency and a continuous push. |
| `%%Q2-FEEDBACK%%` | Short feedback after answering | 1 sentence | Exactly – matching frequency plus repeated input, and damping would stop it. |
| `%%NARRATION-2%%` | Spoken intro to the text answer | 1 sentence | Last one – type the term we keep coming back to. |
| `%%NARRATION-3%%` | Spoken reveal of the answer | 1 sentence | Yes – the natural frequency, the one the system prefers. |
| `%%Q3-STEM%%` | Question text of the text answer | 1 sentence | At which frequency does resonance occur? |
| `%%Q3-ANSWER%%` | Expected answer | max 4 words | natural frequency |
| `%%Q3-HINT%%` | Hint for the text answer | 1 sentence | It is the frequency the system prefers without any drive. |
| `%%Q3-FEEDBACK%%` | Short feedback after answering | 1 sentence | Correct – resonance happens at the natural frequency of the system. |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Choose:** %%Q1-STEM%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%Q1-CORRECT%%
- [( )] %%Q1-WRONG-1%%
- [( )] %%Q1-WRONG-2%%
[[?]] %%Q1-HINT%%
***
%%Q1-FEEDBACK%%
***

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Select all that apply:** %%Q2-STEM%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%Q2-CORRECT-1%%
- [(X)] %%Q2-CORRECT-2%%
- [( )] %%Q2-WRONG-1%%
- [( )] %%Q2-WRONG-2%%
[[?]] %%Q2-HINT%%
***
%%Q2-FEEDBACK%%
***

****************************************

    --{{3}}--
%%NARRATION-3%%

      {{3}}
****************************************

**Type:** %%Q3-STEM%%

[[%%Q3-ANSWER%%]]
[[?]] %%Q3-HINT%%
<script>
const given = `@input`.trim().toLowerCase()
// ADAPT: add further accepted spellings
const accepted = ["%%Q3-ANSWER%%"]
accepted.map(a => a.trim().toLowerCase()).includes(given)
</script>
***
%%Q3-FEEDBACK%%
***

****************************************

<!-- TEMPLATE:END -->
