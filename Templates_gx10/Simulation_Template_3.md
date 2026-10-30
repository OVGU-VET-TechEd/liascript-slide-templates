<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Run a working Python program, read off its result, then find a planted bug in a second version.

import:   https://raw.githubusercontent.com/LiaTemplates/Pyodide/0.3.5/README.md
-->

# Template `Simulation_Template_3`

- **Purpose:** Run a working Python program, let learners read a value off its output, then find a planted bug in a second version.
- **Pairs with:** `Simulation_Template_1`, `Simulation_Template_2`
- **Variants:** Swap the topic by replacing both programs and the question fields. Delete step 2 of the first slide if you do not want a key message.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the run session | max 6 words | Watch Money Grow |
| `%%NARRATION-0%%` | Spoken intro to the program | 2–3 sentences | This program computes compound interest. Run it and watch the balance grow year by year. |
| `%%INTRO-TEXT%%` | What the program does | 1–2 sentences | The program starts with 1000 euros, adds 5 percent interest each year and prints the balance for ten years. |
| `%%PY-CODE%%` | Working Python program | 5–25 lines | see default program below |
| `%%NARRATION-1%%` | Spoken lead-in to the quiz | 1 sentence | Now read the result off the output. |
| `%%EXPLORE-QUESTION%%` | Question about the output | 1 sentence | What number does the program print as the final amount? |
| `%%RESULT-VALUE%%` | Correct value from the output | number | 1628.89 |
| `%%HINT-1%%` | Hint for the numeric quiz | 1 sentence | Look at the last line the program prints. |
| `%%NARRATION-2%%` | Spoken lead-in to the key message | 1 sentence | Here is the idea to take away. |
| `%%KEY-MESSAGE%%` | Key message | 1–2 sentences | Compound interest multiplies the balance each year, so growth accelerates over time. |
| `%%EX-TITLE%%` | Title of the bug slide | max 6 words | Find the Bug |
| `%%NARRATION-EX-0%%` | Spoken intro to the buggy version | 1–2 sentences | This second version should give the same result. Run it and compare. |
| `%%EX-INTRO%%` | Framing of the bug | 1–2 sentences | One line was changed. The program now prints a different final amount. |
| `%%PY-CODE-BROKEN%%` | Program with one planted bug | 5–25 lines | see default program below |
| `%%NARRATION-EX-1%%` | Spoken lead-in to the hunt | 1 sentence | Let us hunt the bug together, with hints if you need them. |
| `%%ERROR-TASK%%` | Find-the-error instruction | 1–2 sentences | Run the program, compare it with the first one and explain which line is wrong and why. |
| `%%ERROR-HINT-1%%` | First tiered hint | 1 sentence | Compare the two programs line by line and find the one line that differs. |
| `%%ERROR-HINT-2%%` | Second tiered hint | 1 sentence | The line that applies the interest uses the wrong operation. |
| `%%ERROR-SOLUTION%%` | Solution text | 1–2 sentences | The line amount = amount + rate adds 0.05 instead of 5 percent. It should be amount = amount * (1 + rate). |

**Default for `%%PY-CODE%%`:**

```python
principal = 1000
rate = 0.05
years = 10
amount = principal
for year in range(1, years + 1):
    amount = amount * (1 + rate)
    print(year, round(amount, 2))
print("final:", round(amount, 2))
```

**Default for `%%PY-CODE-BROKEN%%`:**

```python
principal = 1000
rate = 0.05
years = 10
amount = principal
for year in range(1, years + 1):
    amount = amount + rate
    print(year, round(amount, 2))
print("final:", round(amount, 2))
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%INTRO-TEXT%%

**Try it:** Run the program and read its output.

```python @Pyodide.eval
%%PY-CODE%%
```

    --{{1}}--
%%NARRATION-1%%

**Try it:** %%EXPLORE-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%RESULT-VALUE%%]]
[[?]] %%HINT-1%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%RESULT-VALUE%%")
// ADAPT: relative tolerance (0.02 = 2 %)
Math.abs(v - ref) <= 0.02 * Math.abs(ref)
</script>

    --{{2}}--
%%NARRATION-2%%

      {{2}}
> [!NOTE] Key message
> %%KEY-MESSAGE%%

## %%EX-TITLE%%

    --{{0}}--
%%NARRATION-EX-0%%

%%EX-INTRO%%

**Try it:** Run this version and compare the output.

```python @Pyodide.eval
%%PY-CODE-BROKEN%%
```

    --{{1}}--
%%NARRATION-EX-1%%

      {{1}}
**Find the error:** %%ERROR-TASK%%

<details>
<summary>💡 Hint 1</summary>

%%ERROR-HINT-1%%

</details>

<details>
<summary>💡 Hint 2</summary>

%%ERROR-HINT-2%%

</details>

<details>
<summary>✅ Solution</summary>

%%ERROR-SOLUTION%%

</details>

<!-- TEMPLATE:END -->
