<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Executable and editable JavaScript that prints a table of values, with a read-off quiz and Basis and Extra tasks.
-->

# Template `Simulation_Template_2`

- **Purpose:** Learners run and change a small JavaScript program that prints a table of values. No import needed.
- **Pairs with:** `Concept_Explanation_Template_3`, `Simulation_Template_1`, `Application_Transfer_Template_2`
- **Variants:** The program is a content field (default below: free fall). The read-off answer must match what YOUR program prints. Delete the Extra task for a shorter slide.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title | max 5 words | Free Fall in Code |
| `%%NARRATION-0%%` | Spoken intro | 1–2 sentences | This small program calculates how far a stone falls each second. |
| `%%CODE-INTRO%%` | What the program does | 1–2 sentences | The program prints the fall distance s for t = 0 … 5 s. |
| `%%JS-CODE%%` | JavaScript program, prints with console.log | 5–25 lines | see default program below |
| `%%NARRATION-1%%` | Spoken intro to the quiz | 1 sentence | Run the code and read the table. |
| `%%OUTPUT-QUESTION%%` | Question about the printed output | 1 sentence | How far has the stone fallen after 3 s (in m)? |
| `%%OUTPUT-ANSWER%%` | Value as printed, dot as decimal sign | number | 44.14 |
| `%%OUTPUT-HINT%%` | Hint | 1 sentence | Look at the line that starts with 3. |
| `%%NARRATION-2%%` | Spoken intro to the tasks | 1 sentence | Now change the program yourself. |
| `%%TASK-BASIS%%` | Basis task | 1–2 sentences | Change g to the value on the Moon (1.62 m/s²) and run the code again. |
| `%%BASIS-HINT%%` | Hint for the Basis task | 1 sentence | Only one number in the first lines needs to change. |
| `%%BASIS-SOLUTION%%` | Solution of the Basis task | 1 line | `const g = 1.62` |
| `%%TASK-EXTRA%%` | Extra task | 1–2 sentences | Also print the speed v = g · t in a third column. |
| `%%EXTRA-SOLUTION%%` | Solution of the Extra task | 1–2 lines | Add `const v = g * t` and print `v.toFixed(2)` as third value. |

**Default for `%%JS-CODE%%`:**

```js
const g = 9.81      // gravity in m/s²
const tMax = 5      // last time step in s

console.log("t (s) | s (m)")
for (let t = 0; t <= tMax; t++) {
  const s = 0.5 * g * t * t
  console.log(t + "     | " + s.toFixed(2))
}
```

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

%%CODE-INTRO%%

**Try it:** Click ▶ below the code. You can edit the code and run it again.

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
****************************************

**Read off:** %%OUTPUT-QUESTION%%

<!-- data-hint-button="1" data-solution-button="2" -->
[[%%OUTPUT-ANSWER%%]]
[[?]] %%OUTPUT-HINT%%
<script>
const v = parseFloat(`@input`.replace(",", "."))
const ref = parseFloat("%%OUTPUT-ANSWER%%")
// ADAPT: relative tolerance (0.01 = 1 %)
Math.abs(v - ref) <= 0.01 * Math.abs(ref)
</script>

****************************************

    --{{2}}--
%%NARRATION-2%%

      {{2}}
****************************************

**Basis:** %%TASK-BASIS%%

<details>

<summary>💡 Hint 1</summary>

%%BASIS-HINT%%

</details>
<details>

<summary>✅ Solution</summary>

%%BASIS-SOLUTION%%

</details>

**Extra:** %%TASK-EXTRA%%

<details>

<summary>✅ Solution</summary>

%%EXTRA-SOLUTION%%

</details>

****************************************

<!-- TEMPLATE:END -->
