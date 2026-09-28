# Lesson 3: Planning, Workflow, and Multiple Agents

**Day 3 — Wednesday, 14:00–15:00 teaching. Lab 15:00–16:30.**

## Learning Objective

Break a decision into steps, arrange those steps into a workflow with the checkpoints in the right places, distribute them across specialist roles, and synthesize the results — identifying consensus, conflict, what you adopted, and what you rejected and why. Concatenating three reports is not synthesis.

Day 1 was one prompt, one deliverable. Day 2 was one prompt against a corpus. Today's task has an ordering problem: you cannot rank the service areas until you have the figures, cannot write the memo until you have the ranking, and cannot trust any of it unless something checks it. Order, state, and who does what are the subject.

## Part 1: Decomposition — What Are the Steps?

Before any structure, the question is what the steps actually are. Ask for them:

```text
Do not modify any files and do not start work. Break this task into numbered steps: rank the four service areas in @materials/day3-budget/ and recommend one pilot for the quarter. For each step say what it needs before it can start, and what it produces.
```

What comes back is a dependency list, and it tells you the shape of the work:

- Steps needing nothing but the pack can run **at the same time**.
- Steps needing another step's output must run **in order**.
- Steps where the answer changes what happens next are **branches**.

Today has one real branch, and it is the day's whole lesson: speed first and accuracy first lead to different pilots. A workflow that cannot represent a branch will quietly pick one and present it as the answer.

### Where the State Lives

Each step produces something the next step consumes. That accumulated material — the figures pulled, the ranking derived, the priority in force — is the task's state, and in this course it lives in exactly two places: the conversation, and the files you write.

That matters because a subagent does not share your conversation. Anything it needs, you pass in its instructions; anything it found, you get back in its report. Nothing is implicitly shared. A subagent asked to "continue the analysis" has no idea what analysis you mean.

## Part 2: Plan Mode — Approve the Approach First

Plan mode is a permission mode, not a politeness convention. File changes are blocked until you approve. It is the checkpoint that makes decomposition useful: the steps are written down and agreed before anything is produced.

### Step 1: Ask for a Plan

Enter plan mode, then:

```text
Please read @prompts/plan.txt and create the requested plan.
```

### Step 2: Review It Like a Manager, Not a Reader

Do not approve the first plan. Check whether it answers:

- Does it name which figures it will use and which months they cover, or just say it will analyse the workbook?
- Does it say what happens when the priority changes from speed to accuracy — or does it produce one ranking?
- Does it separate what the deputy can decide this quarter from what it cannot?
- Does it keep `materials/` unmodified?

Request at least one revision. For example:

```text
Revise the plan. The recommendation may differ depending on whether speed or accuracy comes first. State how you will handle that rather than choosing one priority silently.
```

### Why This Matters More Than It Looks

The plan is the cheapest place to catch a misunderstanding. A wrong plan costs one paragraph to fix. The same misunderstanding discovered in a finished dashboard costs the afternoon.

## Part 3: Why More Than One Agent

Four reasons, in order of how often they matter:

1. **Isolated context.** A role that reads six months of figures fills its own context with detail, not yours. You receive the finding, not the search.
2. **Least privilege.** The three roles in this project are read-only. They analyse; they cannot modify your dashboard. Analysis and editing are different jobs and should have different permissions.
3. **Parallelism.** Independent questions do not have to be asked in sequence.
4. **Real disagreement.** A role instructed to challenge the leading conclusion will find weaknesses that the role that produced it will not.

The fourth is the one people underuse, and it is the one today's pack is built for.

### Step 1: Review the Roles

```text
/agents
```

The project configures three, all `Read, Grep, Glob` only:

- **`source-checker`** — traces every claim to a pack file and lists the ones nothing supports.
- **`resident-advocate`** — reads the recommendation as a resident in the queue, and finds the wait a document is hiding.
- **`decision-challenger`** — attacks the leading recommendation and names the variables that would flip it.

Read one of the definitions in `.codebuddy/agents/`. Notice that each one says what it must output and forbids fabricating figures. A role with a vague brief returns a vague report.

### Step 2: Delegate in Parallel

```text
Please execute @prompts/delegate-analysis.txt. Run the three named subagents as parallel background tasks, wait for all three, then synthesize.
```

Check that three tasks actually start and that three results come back. Do not let multiple agents write to the same file. They produce analysis; the main agent produces the dashboard.

### Step 3: Force Synthesis

If the main agent hands you three reports in sequence, push back:

```text
Do not concatenate the reports. Give me: what all three agree on, where they conflict and which side you took, the data gap none of them could close, and the recommendation you rejected with the reason.
```

#### What Good Synthesis Looks Like Today

This pack is built so the roles cannot all agree. Speed first points at more staff in the Republic of Karakalpakstan: 16 days in October, 9 officers, the longest time and heaviest load per officer. Accuracy first points somewhere else entirely — Fergana's return rate sits around 25–29 percent from May through October, far above the other three areas, and staff do not fix a return rate.

If your three agents produce one tidy answer, the delegation did not work. The honest output names both, states which priority the deputy holds today, and says plainly that the answer changes when the priority does.

One more trap worth catching: `budget_spent_mln_uzs` is past operating spend. It is not the price of the pilot. An agent that treats it as a budget will rank the areas backwards.

### Step 4: Verify the Sources Yourself

Ask for the trail:

```text
For each figure in the memo, name the sheet and the months it came from.
```

Then open `regional-kpis.xlsx` and check two of them by hand. Delegation multiplies output. It does not multiply accountability, which stays with you.

## Part 4: The Four Workflow Shapes

Parallel is one shape. Four are worth knowing, and today's task uses all of them.

| Shape | What it means | Today |
|---|---|---|
| **Sequential** | Each step consumes the last | You cannot build the dashboard until the synthesis exists |
| **Parallel** | Independent questions, asked at once | The three roles |
| **Conditional** | The route depends on an earlier result | Speed first or accuracy first — different pilots |
| **Human-in-the-loop** | The run stops and waits for a person | Plan-mode approval; the hand-check in Step 4 |

You used the first two and the fourth before they had names. Plan mode was sequential with a checkpoint: the agent planned, stopped, and did not write until you approved.

The third is the one worth practising, because it is the one an agent skips. Asked to recommend a pilot, it will produce one recommendation. The branch exists in the task whether or not it appears in the output, and an output that hides it has answered a question the deputy did not ask:

```text
Do not give me one recommendation. Produce the ranking twice — once with days-to-operate first, once with return rate first — and then tell me which areas change position and which do not.
```

An area that wins under both priorities is a robust choice. An area that wins under one is a decision, and decisions belong to a person.

### The Three Roles

The roles have names too, and you have already played them:

| Role | What it does | Where it already is |
|---|---|---|
| Planner | Decides the steps before any file is written | Plan mode, `prompts/plan.txt` |
| Executor | Produces the deliverable | `prompts/build-dashboard.txt` |
| Reviewer | Checks the result against the sources | `prompts/review.txt`, `source-checker` |

Naming them is the point. The pattern is not a framework you install; it is a division of labour you were already using, and once it is named you can notice when one of the three is missing. A task that goes straight from question to finished document has no Reviewer, and the person who finds the error will be someone outside your team.

The Reviewer has one structural requirement: it must not be the thing that produced the work. That is why `source-checker` is a separate read-only role rather than a final instruction to the agent that wrote the dashboard. Asking a producer to check its own output gets you its own reasoning back, restated with more confidence.

### Which Steps Need a Person

Plan-mode approval is a human checkpoint. So is the hand-check in Step 4. The harder question is which of today's decisions genuinely need one.

Ask your group, before you build:

```text
List the decisions in this task that need my approval before you proceed, and for each one say what goes wrong if you decide it alone.
```

Two things go wrong with the answer. Too few checkpoints and the agent commits a quarter's budget to a ranking nobody checked. Too many and you have approved eleven things, read none of them, and the approval means nothing. A checkpoint you rubber-stamp is worse than no checkpoint, because it leaves a signature.

Today, one genuinely needs a person: whether the recommendation changes when the priority changes. That is not a calculation, it is a decision about what to tell the deputy. The rest is arithmetic the agent can do and you can check.

## When Not to Plan, and When Not to Delegate

Most of the time, on both counts. Three agents to change a title, explain a function, or answer a question you could answer by opening one file adds latency and cost and nothing else. Delegate when the questions are genuinely independent, when the detail would swamp your main conversation, or when you want a role whose job is to disagree.

The same restraint applies to sequencing. A two-step task does not need a Planner, an Executor, and a Reviewer; it needs someone to do it and someone to read it. Plan mode for a one-line correction wastes everyone's time. Structure that costs more than the task is not rigour, and a diagram of a workflow is not a workflow.

## Lab: One Pilot This Quarter

`materials/day3-budget/`. Done means `dashboard.html` or `dashboard.xlsx` with a comparison table, one chart, and both priorities, plus a half-page `memo.md`: the recommendation, three figures, one risk, and one question the workbook cannot answer.

The last 20 minutes are for the second priority. Changing an adjective without recalculating is not done.

## Checkpoint

Your synthesis should contain at least:

- One point all three roles agree on.
- One genuine conflict, and which side you took.
- One data gap the workbook cannot close.
- One reason to oppose your own recommendation.
- A clear answer to whether the choice survives the switch from speed to accuracy.

And name, for your own task: which steps ran in order because they had to, which could have run at the same time, where the branch was, and which single step you would not let an agent finish without you.

Next: [`04-group-project.md`](04-group-project.md)
