<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Think-Pair-Share session built around a dilemma with a vote before and after the discussion.
-->

# Template `Application_Transfer_Template_3`

- **Purpose:** Run a Think-Pair-Share discussion around a dilemma with a vote before and after the discussion.
- **Pairs with:** `Application_Transfer_Template_1`, `Application_Transfer_Template_2`, `Summary_Recap_Template_3`
- **Variants:** Replace the pre-vote options with a survey vector `[(1)]`…`[(4)]` if you want a stance scale. Delete the post-vote quiz and keep only the strongest-argument survey.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the dilemma | max 6 words | The Filter Or The Fine |
| `%%NARRATION-0%%` | Spoken setup of the dilemma | 2–3 sentences | A factory on the river must decide how to handle its wastewater this year. |
| `%%DILEMMA%%` | The dilemma both sides can defend | 2–4 sentences | The filter would cut the discharge by 90 percent but costs 400,000 euros and 30 jobs. Without it, the plant pays a fine of 60,000 euros per year and keeps the jobs. |
| `%%NARRATION-1%%` | Spoken intro to the pre-vote | 1 sentence | Before we discuss, tell me where you stand. |
| `%%PRE-VOTE-QUESTION%%` | Question for the pre-vote | 1 sentence | What should the company do? |
| `%%PRE-VOTE-CORRECT%%` | First vote option | max 10 words | Install the filter and accept the cost |
| `%%PRE-VOTE-WRONG-1%%` | Second vote option | max 10 words | Keep the jobs and pay the fine |
| `%%PRE-VOTE-WRONG-2%%` | Third vote option | max 10 words | Close the plant and move elsewhere |
| `%%PRE-VOTE-HINT%%` | Hint for the pre-vote | 1 sentence | Think about who pays the cost and who benefits. |
| `%%PRE-VOTE-FEEDBACK%%` | Feedback after the pre-vote | 1 sentence | No wrong answer – the dilemma is built so both sides have a point. |
| `%%NARRATION-2%%` | Spoken intro to the Think phase | 1 sentence | First work on your own. |
| `%%THINK-INSTRUCTION%%` | What to do in the Think phase | 1 sentence | Write down your two strongest arguments for your side. |
| `%%NARRATION-3%%` | Spoken intro to the Pair phase | 1 sentence | Now compare with a partner. |
| `%%PAIR-INSTRUCTION%%` | What to do in the Pair phase | 1 sentence | Exchange your two strongest arguments with a neighbour. |
| `%%NARRATION-4%%` | Spoken intro to the Share phase | 1 sentence | Then we bring it back to the whole group. |
| `%%SHARE-INSTRUCTION%%` | What to do in the Share phase | 1 sentence | The class discusses the strongest arguments and how the vote shifted. |
| `%%NARRATION-5%%` | Spoken intro to the post-vote | 1 sentence | Let us see how the discussion changed your mind. |
| `%%POST-VOTE-QUESTION%%` | Question for the post-vote | 1 sentence | What is your stance after the discussion? |
| `%%POST-VOTE-CORRECT%%` | First post-vote option | max 10 words | Install the filter and accept the cost |
| `%%POST-VOTE-WRONG-1%%` | Second post-vote option | max 10 words | Keep the jobs and pay the fine |
| `%%POST-VOTE-WRONG-2%%` | Third post-vote option | max 10 words | Close the plant and move elsewhere |
| `%%POST-VOTE-HINT%%` | Hint for the post-vote | 1 sentence | Compare your first vote with what you heard in the pair. |
| `%%POST-VOTE-FEEDBACK%%` | Feedback after the post-vote | 1 sentence | Compare the two votes – that shift is the learning. |
| `%%STRONGEST-ARGUMENT-QUESTION%%` | Question for the strongest-argument survey | 1 sentence | What was the strongest argument you heard? |

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

> [!IMPORTANT] Dilemma
> %%DILEMMA%%

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Decide:** %%PRE-VOTE-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%PRE-VOTE-CORRECT%%
- [( )] %%PRE-VOTE-WRONG-1%%
- [( )] %%PRE-VOTE-WRONG-2%%
[[?]] %%PRE-VOTE-HINT%%
***
%%PRE-VOTE-FEEDBACK%%
***

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!TIP] Think
> %%THINK-INSTRUCTION%%

    --{{3}}--
%%NARRATION-3%%

      {{3}}
> [!TIP] Pair
> %%PAIR-INSTRUCTION%%

    --{{4}}--
%%NARRATION-4%%

      {{4}}
> [!TIP] Share
> %%SHARE-INSTRUCTION%%

    --{{5}}--
%%NARRATION-5%%

      {{5}}
****************************************

**Decide:** %%POST-VOTE-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
- [(X)] %%POST-VOTE-CORRECT%%
- [( )] %%POST-VOTE-WRONG-1%%
- [( )] %%POST-VOTE-WRONG-2%%
[[?]] %%POST-VOTE-HINT%%
***
%%POST-VOTE-FEEDBACK%%
***

**Share:**

[[___]] %%STRONGEST-ARGUMENT-QUESTION%%

****************************************

<!-- TEMPLATE:END -->
