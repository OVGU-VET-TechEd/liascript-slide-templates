<!--
author:   %%AUTHOR%%
email:    %%EMAIL%%
version:  0.2.0
language: en
narrator: US English Female
mode:     Presentation
comment:  Course overview as a module table plus learning objectives with Bloom verbs and an interest survey.
-->

# Template `Overview_Course_Template_1`

- **Purpose:** Show the structure of the course (what, how, how long) and the learning objectives in classic form.
- **Pairs with:** `Introduction_Template_1`, `Introduction_Template_2`, `Content_Introduction_Template_1`
- **Variants:** Add or delete table rows. Delete step 5 on the second slide to skip the survey.

<!-- data-type="none" -->
| Placeholder | Meaning | Limit | Example |
|---|---|---|---|
| `%%SLIDE-TITLE%%` | Title of the overview slide | max 5 words | Course at a Glance |
| `%%NARRATION-0%%` | Spoken intro to the module table | 1–2 sentences | The course has four modules over twelve weeks. |
| `%%MODULE-1%%` … `%%MODULE-4%%` | Module topic | max 6 words | Fluid properties ; Hydrostatics ; Fluid dynamics ; Pipe flow |
| `%%FORMAT-1%%` … `%%FORMAT-4%%` | Format of the module | max 4 words | Lecture and quiz ; Lecture and lab ; Lecture and simulation ; Project work |
| `%%DURATION-1%%` … `%%DURATION-4%%` | Duration | max 3 words | 2 weeks ; 3 weeks ; 4 weeks ; 3 weeks |
| `%%ASSESSMENT%%` | How the course is assessed | 1 sentence | Written exam (90 min) and two lab reports. |
| `%%OBJ-TITLE%%` | Title of the objectives slide | max 6 words | What You Will Be Able to Do |
| `%%NARRATION-OBJ-0%%` | Spoken intro to the objectives | 1 sentence | By the end of the course you can do four things. |
| `%%NARRATION-OBJ-1%%` … `%%NARRATION-OBJ-4%%` | Spoken comment per objective | 1 sentence | First, you can explain the basic terms. ; Second, you can calculate pressures. ; Third, you can analyse flows in pipes. ; And finally, you can evaluate a design. |
| `%%VERB-1%%` … `%%VERB-4%%` | Bloom verb, rising level | 1 word | explain ; calculate ; analyse ; evaluate |
| `%%OBJECTIVE-1%%` … `%%OBJECTIVE-4%%` | Rest of the objective | max 12 words | the key properties of fluids ; pressures in resting fluids ; flows in simple pipe systems ; a pump design against requirements |
| `%%NARRATION-OBJ-5%%` | Spoken intro to the survey | 1 sentence | Which modules are you looking forward to? |

**Note:** the survey on slide 2 reuses `%%MODULE-1%%` … `%%MODULE-4%%` from slide 1.

<!-- TEMPLATE:BEGIN -->

## %%SLIDE-TITLE%%

    --{{0}}--
%%NARRATION-0%%

<!-- data-type="none" -->
| No | Module | Format | Duration |
|----|--------|--------|----------|
| 1 | %%MODULE-1%% | %%FORMAT-1%% | %%DURATION-1%% |
| 2 | %%MODULE-2%% | %%FORMAT-2%% | %%DURATION-2%% |
| 3 | %%MODULE-3%% | %%FORMAT-3%% | %%DURATION-3%% |
| 4 | %%MODULE-4%% | %%FORMAT-4%% | %%DURATION-4%% |

> [!NOTE] Assessment
> %%ASSESSMENT%%

## %%OBJ-TITLE%%

    --{{0}}--
%%NARRATION-OBJ-0%%

**By the end of this course you can …**

    --{{1}}--
%%NARRATION-OBJ-1%%

      {{1}}
- **%%VERB-1%%** %%OBJECTIVE-1%%

    --{{2}}--
%%NARRATION-OBJ-2%%

      {{2}}
- **%%VERB-2%%** %%OBJECTIVE-2%%

    --{{3}}--
%%NARRATION-OBJ-3%%

      {{3}}
- **%%VERB-3%%** %%OBJECTIVE-3%%

    --{{4}}--
%%NARRATION-OBJ-4%%

      {{4}}
- **%%VERB-4%%** %%OBJECTIVE-4%%

    --{{5}}--
%%NARRATION-OBJ-5%%

      {{5}}
****************************************

**Choose:** Which modules are you most curious about? (several possible)

[[m1]] %%MODULE-1%%
[[m2]] %%MODULE-2%%
[[m3]] %%MODULE-3%%
[[m4]] %%MODULE-4%%

****************************************

<!-- TEMPLATE:END -->
