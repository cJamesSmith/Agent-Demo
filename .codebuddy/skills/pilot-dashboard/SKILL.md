---
name: pilot-dashboard
description: Choose one intervention in one area from operational figures, and show whether the choice survives a change of priority. Use for pilot selection, budget allocation between options, regional comparisons, and priority sensitivity checks.
argument-hint: "[the decision to be made]"
allowed-tools: Read, Grep, Glob, Edit, Write, Bash
---

# Pilot Selection Method

Produce a comparison a decision-maker can act on, which states plainly whether the recommendation depends on the current priority.

## Core Process

1. **Read the definitions first.** Before using any column, find its definition. A metric that measures one step of a process cannot be used to argue about the whole process. Note any column that is easy to mistake for something else — past spend is not a budget.
2. **Match each option to the metric it moves.** Each intervention has a main effect and a stated limit. An option that mainly reduces one metric cannot be justified by a different metric improving. Write the mapping out before comparing anything. See [references/comparison-rules.md](references/comparison-rules.md).
3. **Build the comparison table.** One row per area, one column per relevant metric, with the period stated. Include the load per staff member where staffing is one of the options — a raw count of applications does not show where people are stretched.
4. **Check the trend, not only the latest month.** A rate that has held for six months is a different case from one that spiked once. Say which you are looking at.
5. **Recommend under the stated priority.** Name the option, the area, and the three figures that carry the choice.
6. **Re-run under the alternative priority.** Recalculate. Do not adjust the adjectives around the same conclusion. Then state explicitly whether the choice holds or changes — a changed answer is a finding, not a failure.
7. **State one risk and one question the data cannot answer.** Every dataset has a question outside it. Name one.

## The Chart

One chart, showing the metric the recommendation turns on, across all areas, over the available months. Not a gallery. If a second chart is needed to make the case, the case is not yet clear.

## Definition of Done

The recommendation is visible immediately, with its area and its three supporting figures. Both priorities appear with their own recalculated answer. Every figure names its sheet and its months. The risk and the unanswerable question are stated, not implied.
