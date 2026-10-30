<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Run a small JavaScript program in the slide, read off its printed output and check it with a quiz and two tasks.
-->

# Template `Simulation_Template_2`

- **Purpose:** Let learners run a small JavaScript program directly in the slide and read concrete numbers off its printed output.
- **Pairs with:** `Simulation_Template_1`, `Simulation_Template_3`, `Concept_Explanation_Template_1`
- **Variants:** Replace the quiz with a single-choice question about the trend in the output. Add a second program block for a before/after comparison.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the run slide | max 6 words | Watching Money Grow |
| `%%NARRATION-0%%` | Spoken intro to the program | 1–2 sentences | Let us watch compound interest work by running a small program. |
| `%%PROGRAM-DESC%%` | What the program does | 1–2 sentences | The program starts with 10000 euros at 3 percent interest and prints the balance after each of the first ten years. |
| `%%JS-CODE%%` | JavaScript program | 5–25 lines | see default program below |
| `%%NARRATION-1%%` | Spoken intro to the read-off quiz | 1 sentence | Now check what you read in the output. |
| `%%READOFF-QUESTION%%` | Question about the printed output | 1 sentence | What balance does the program print after year 10? |
| `%%READOFF-ANSWER%%` | Value to read off, no quotes or backslashes | number | 10398 |
| `%%READOFF-HINT%%` | Hint for the read-off | 1 sentence | Look at the last line the program prints. |
| `%%READOFF-FEEDBACK%%` | Short feedback after answering | 1 sentence | Correct – 10000 times 1.03 to the power of 10 is about 10398. |
| `%%EX-TITLE%%` | Title of the tasks slide | max 6 words | Change It and Read Off |
| `%%NARRATION-EX-0%%` | Spoken intro to the tasks | 1 sentence | Now change the program yourself and answer the two tasks. |
| `%%NARRATION-EX-1%%` | Spoken intro to the extra task | 1 sentence | For the extra task, keep the rate and look further ahead. |
| `%%BASIS-TASK%%` | Basis task: change and read off | 1–2 sentences | Change the interest rate to 5 percent, run the program again and read off the new balance after year 10. |
| `%%BASIS-ANSWER%%` | Expected value for the basis task | number | 16289 |
| `%%BASIS-HINT-1%%` | First hint for the basis task | 1 sentence | The rate is the number 0.03 near the top of the program. |
| `%%BASIS-HINT-2%%` | Second hint for the basis task | 1 sentence | Replace 0.03 with 0.05 and press Run again. |
| `%%BASIS-SOLUTION%%` | Solution text for the basis task | 1 sentence | 10000 times 1.05 to the power of 10 is about 16289. |
| `%%EXTRA-TASK%%` | Extra task: compute from the output | 1–2 sentences | Use the printed output: how much interest has the account earned by the end of year 10? |
| `%%EXTRA-ANSWER%%` | Expected value for the extra task | number | 398 |
| `%%EXTRA-HINT-1%%` | First hint for the extra task | 1 sentence | Interest earned is the final balance minus the starting amount. |
| `%%EXTRA-HINT-2%%` | Second hint for the extra task | 1 sentence | The program starts with 10000 euros; subtract that from the balance printed for year 10. |
| `%%EXTRA-SOLUTION%%` | Solution text for the extra task | 1 sentence | The balance grows from 10000 to about 10398, so the interest earned is 398 euros. |

**Default for `%%JS-CODE%%`:**

```js
let balance = 10000;
const rate = 0.03;
for (let year = 1; year <= 10; year++) {
  balance = balance * (1 + rate);
  console.log("Year " + year + ": " + balance.toFixed(0) + " euros");
}
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%PROGRAM-DESC%%

```js
%%JS-CODE%%
```
<script>
@input
""
</script>

    --{{1}}--
%%NARRATION-1%%

      {{1}}
**Read off:** %%READOFF-QUESTION%%

[[%%READOFF-ANSWER%%]]
[[?]] %%READOFF-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%READOFF-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%READOFF-FEEDBACK%%
***

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

**Basis task:** %%BASIS-TASK%%

<details>
<summary>💡 Hint 1</summary>

%%BASIS-HINT-1%%

</details>

<details>
<summary>💡 Hint 2</summary>

%%BASIS-HINT-2%%

</details>

<details>
<summary>✅ Solution</summary>

%%BASIS-SOLUTION%%

</details>

[[%%BASIS-ANSWER%%]]
[[?]] %%BASIS-HINT-1%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%BASIS-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%BASIS-SOLUTION%%
***

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
**Extra task:** %%EXTRA-TASK%%

<details>
<summary>💡 Hint 1</summary>

%%EXTRA-HINT-1%%

</details>

<details>
<summary>💡 Hint 2</summary>

%%EXTRA-HINT-2%%

</details>

<details>
<summary>✅ Solution</summary>

%%EXTRA-SOLUTION%%

</details>

[[%%EXTRA-ANSWER%%]]
[[?]] %%EXTRA-HINT-1%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%EXTRA-ANSWER%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>
***
%%EXTRA-SOLUTION%%
***

<!-- TEMPLATE:END -->
