# Instructor preparation and run sheet

Not for participants. Keep this with [`instructor-key.md`](instructor-key.md).

## Before the week

- CodeBuddy Code installed and signed in on every machine, tested by one person on each machine, not assumed. A room that spends the first forty minutes on authentication loses Day 1.
- This repository cloned on every machine, or on one machine per group.
- `python3 checks/check-project.py course` passes. Run it after any edit to the package.
- `materials/day3-budget/regional-kpis.xlsx` opens, and the `definitions` sheet is visible. Day 3's main trap is a column that means something other than it looks like, and it is defused on that sheet.
- A browser on hand that opens a local `index.html` from disk. Day 1 and one Day 4 topic deliver HTML.
- [`role-cards.md`](role-cards.md) printed and cut, one card per group. Do not hand out the uncut page. These are the Day 2 cards (Economy, Digital, Social) and are a different thing from the four Day 4 team roles, which are in the lesson and need no printing.
- [`presentation-rubric.md`](presentation-rubric.md) printed, one per participant, handed out on Day 1 rather than Day 4. Teams that know the five required elements and the six scoring weights on day one collect the material as they go.
- Groups of three fixed for the week. Mixed roles per group where possible — the packs reward someone who has stood at an intake desk.
- Read the arithmetic in the `day4-benefits/` section of [`instructor-key.md`](instructor-key.md) before Day 4. Three of the four cases turn on something other than the income figure, and a team will ask you to confirm a threshold calculation.

## What you do not need

No Python environment beyond the standard library, no API key, no packages to install, no notebook server. The checker is standard-library only. CodeBuddy Code does the work the course is about.

## Day 1 — Monday 9 November — agent fundamentals and tool-calls

| Time | What |
|---|---|
| 14:00–14:25 | [`lessons/00-agent-basics.md`](../lessons/00-agent-basics.md) |
| 14:25–15:10 | [`lessons/01-tool-calls.md`](../lessons/01-tool-calls.md), including the demonstration |
| 15:10–16:30 | Lab, `day1-website/` |
| 16:30–17:00 | Debrief |

In the opener, slow down at the tool-call anatomy — name, arguments, result — and read three real calls off the screen in those three parts. The rest of the week refers back to it, and a room that has not seen one call taken apart will treat the trail as decoration.

The demonstration is the hour's centre: run `prompts/day1-weak-prompt.txt`, then `prompts/day1-strong-prompt.txt` in a fresh conversation, against the same pack, on the projector. Do not describe the difference. Show it, then ask the room where the fee came from.

Ask the room to count the tool calls each prompt makes before the draft appears. The contrast is visible before anyone reads a word of the output, and it makes the point faster than the output does.

Expect the weak prompt to invent a state fee in som. If it does not on the first run, run it again — it will. Have a screenshot from a previous run as a fallback.

Hand out: the `day1-website/` pack, the rubric.

## Day 2 — Tuesday 10 November — retrieval, knowledge base, and memory

| Time | What |
|---|---|
| 14:00–15:00 | [`lessons/02-rag-memory.md`](../lessons/02-rag-memory.md) |
| 15:00–16:30 | Lab, `day2-briefing/` |
| 16:30–17:00 | Debrief |

Hand out one role card per group at the start of the lab, not at the start of the day.

The lesson is the longest of the week and the lab needs its full ninety minutes. If you are behind at 14:50, cut the skills walkthrough short and keep the counterfactual refusal test in Part 2 — watching the agent refuse an instruction and cite a file is the moment that lands, and it is where memory and retrieval visibly meet.

The vocabulary is new this year and is worth being explicit about: the pack is the knowledge base, `Grep` and `Read` are the retrieval step, and the filename in parentheses is the retrieval trace. Participants have been doing all three since Day 1 without the names.

Debrief by role. Ask each group for its two most important conclusions, then ask the room whether the three groups disagree or merely emphasise differently. They should mostly agree on the four unsupported claims and differ on what tomorrow's decision is.

## Day 3 — Wednesday 11 November — planning, workflow, and multiple agents

| Time | What |
|---|---|
| 14:00–15:00 | [`lessons/03-planning-workflow-multiagent.md`](../lessons/03-planning-workflow-multiagent.md) |
| 15:00–16:30 | Lab, `day3-budget/` |
| 16:30–17:00 | Debrief |

Plan mode moved here from Day 2, so this lesson now runs decomposition, then plan mode, then the workflow shapes, then delegation. It is a full hour. If you are behind, shorten the decomposition exercise — the plan-mode revision and the delegation are what the lab needs.

At 16:10, whatever state the room is in, issue `prompts/priority-change.txt`. The deputy has changed the instruction. Twenty minutes is enough to recalculate and not enough to rewrite comfortably, which is the intended pressure.

Watch for two failures: a group whose three subagents produced one tidy answer, and a group that answered the priority change by editing adjectives. Both are worth naming in the debrief, without naming the group.

## Day 4 — Thursday 12 November — group project

| Time | What |
|---|---|
| 14:00–14:20 | Brief and topic allocation |
| 14:20–16:00 | Group work |
| 16:00–17:00 | Presentations |

Allocate one of the five topics by draw. Two teams may share a topic; they present separately and the difference is the best discussion of the day.

Make the four team roles happen out loud at 14:20 — Agent Designer, Tool / RAG Engineer, Workflow Engineer, Evaluator / Presenter, with a three-person team merging the last two. Teams that skip this default to one person driving and two watching, which is the failure this day is most prone to. Walk the room at 14:30 and ask any silent participant which role they hold.

With more than six teams, start presentations at 15:45 and cap each at 5 minutes. This fallback is already in the rubric, so announce it rather than improvising.

Tell teams they may run `python3 checks/check-project.py project <topic> <folder>` themselves. Run it yourself on each team's folder before they present — it takes seconds and catches an empty file before it becomes a slide.

During presentations, use the three moves at the end of `instructor-key.md`: point at a number on screen and ask where it came from; ask any team reporting no corrections what they checked and how; where two teams share a topic, put the difference to both rather than grading one right.

## When a group stalls

Every pack has a planted trap, and every trap is documented in `instructor-key.md`. Do not give the answer. Point at the file.

| Day | The stall | What to point at |
|---|---|---|
| 1 | The page looks finished in thirty minutes | Ask them to list every "to be confirmed" item and name the file they checked. There should be five |
| 1 | The agent answered without opening anything | Ask them to scroll back and count the tool calls before the draft |
| 2 | The group accepts the old deck | Ask which slide they checked against a figure, and read the October numbers aloud |
| 2 | The group resolves the Fergana disagreement silently | Ask for the date on each set of minutes |
| 2 | Conclusions arrive with no filenames | Ask where the answer came from, for one conclusion, and wait |
| 3 | Three agents, one answer | Ask what `decision-challenger` said that the other two did not |
| 3 | The areas rank backwards | Ask them to read the `definitions` sheet entry for `budget_spent_mln_uzs` aloud |
| 3 | One ranking, no branch | Ask what changes if accuracy comes first, and require the second ranking |
| 4 | No contradiction found | Ask them to name the two files that describe the same step, and read both |
| 4 | `day4-benefits/`: all four cases decided | Ask which body decides, and read the sentence in `eligibility-rules.md` that says the desk does not |
| 4 | One person driving, two watching | Ask each member which of the four roles they hold |

## When a group finishes early

They have not. Ask for the source file behind a claim you pick off the screen, then ask whether their own deliverables agree with each other on day counts. One of those two questions usually reopens the work.

If both hold up, the group is genuinely ahead: have them run `prompts/review.txt` and fix what it finds, or on Day 4, rehearse the presentation a second time with a timer. Do not give them extra scope.

## What this package cannot check for you

The checker verifies structure only. It will pass a page that invents a state fee, a briefing that cites nothing, and a consultation synthesis that counts the duplicate rows. Everything that matters is checked by a person against `instructor-key.md`, and by participants running `prompts/review.txt`. See [`../checks/README.md`](../checks/README.md).
