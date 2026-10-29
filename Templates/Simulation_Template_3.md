<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Executable Python in the browser (Pyodide) with an exploration task and a find-the-error program with tiered hints.

import:   https://raw.githubusercontent.com/LiaTemplates/Pyodide/0.3.5/README.md
-->

# Template `Simulation_Template_3`

- **Purpose:** Learners run Python in the browser: first explore a working program, then repair a program with one error.
- **Pairs with:** `Concept_Explanation_Template_1`, `Simulation_Template_2`, `Application_Transfer_Template_2`
- **Variants:** Both programs are content fields (defaults below: a cup of coffee cooling down). Keep exactly ONE faulty line in the second program. The exploration answer must match what YOUR program prints. The first run loads Python (a few seconds).

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the exploration slide | max 5 words | Coffee Cooling in Python |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | This program models how a cup of coffee cools down minute by minute. |
| `%%CODE-INTRO%%` | What the program does | 1–2 sentences | Each minute the coffee loses 10 % of its temperature difference to the room. |
| `%%PY-CODE%%` | Working Python program, prints its results | 5–25 lines | see default program below |
| `%%NARRATION-1%%` | Spoken exploration task | 1 sentence | Change the cooling rate and run the program again. |
| `%%EXPLORE-TASK%%` | Exploration task with a numeric answer | 1–2 sentences | Set k to 0.2. After how many minutes is the coffee below 40 °C for the first time? |
| `%%EXPLORE-ANSWER%%` | Numeric answer, dot as decimal sign | number | 6 |
| `%%EXPLORE-HINT%%` | Hint | 1 sentence | Change only the line with k and read the printed table. |
| `%%EXPLORE-FEEDBACK%%` | Feedback after solving | 1 sentence | After 6 minutes the coffee has 38.4 °C. |
| `%%ERROR-TITLE%%` | Title of the error slide | max 5 words | Find the Error |
| `%%NARRATION-ERR-0%%` | Spoken intro to the broken program | 1–2 sentences | This program should do the same, but it crashes. |
| `%%ERROR-TASK%%` | Task description | 1 sentence | Run the program, read the error message and repair the faulty line. |
| `%%PY-ERROR-CODE%%` | The same program with exactly one error | 5–25 lines | see default program below |
| `%%NARRATION-ERR-1%%` | Spoken comment on the hints | 1 sentence | Stuck? Open the hints one after another. |
| `%%HINT-1%%` | Small hint | 1 sentence | Read the last line of the error message. |
| `%%HINT-2%%` | Bigger hint | 1 sentence | Compare the variable names in line 2 and line 7. |
| `%%SOLUTION%%` | Corrected line | 1 line | `temp = temp - k * (temp - room)` |

**Default for `%%PY-CODE%%`:**

```python
temp = 90.0    # start temperature in °C
room = 20.0    # room temperature in °C
k = 0.1        # cooling rate per minute

for minute in range(0, 11):
    print(f"{minute:2d} min: {temp:5.1f} °C")
    temp = temp - k * (temp - room)
```

**Default for `%%PY-ERROR-CODE%%`:**

```python
temp = 90.0
room = 20.0
k = 0.1

for minute in range(0, 11):
    print(f"{minute:2d} min: {temp:5.1f} °C")
    temp = temp - k * (temp - rooom)
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%CODE-INTRO%%

**Try it:** Click ▶ below the code.

```python
%%PY-CODE%%
```
@Pyodide.eval

    --{{1}}--
%%NARRATION-1%%

      {{1}}
****************************************

**Explore:** %%EXPLORE-TASK%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%EXPLORE-ANSWER%%]]
[[?]] %%EXPLORE-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%EXPLORE-ANSWER%%")
// ADAPT: relative tolerance (0 = exact)
Math.abs(v - ref) <= 0 * Math.abs(ref)
</script>
***
%%EXPLORE-FEEDBACK%%
***

****************************************

## %%ERROR-TITLE%%

    --{{0}}--
%%NARRATION-ERR-0%%

**Repair:** %%ERROR-TASK%%

```python
%%PY-ERROR-CODE%%
```
@Pyodide.eval

    --{{1}}--
%%NARRATION-ERR-1%%

      {{1}}
****************************************

<details>

<summary>💡 Hint 1</summary>

%%HINT-1%%

</details>
<details>

<summary>💡 Hint 2</summary>

%%HINT-2%%

</details>
<details>

<summary>✅ Solution</summary>

%%SOLUTION%%

</details>

****************************************

<!-- TEMPLATE:END -->
