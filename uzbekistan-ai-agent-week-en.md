# AI Agent Training for the Uzbekistan Government Team

## 1. Scope and conventions

The programme runs from 9 to 12 November, 14:00–17:00 local time on each of the four days. Participant packs are held in `materials/`, the teaching modules in `lessons/`, and the answer checks in `materials/instructor-key.md`, which remains with the instructor and is not distributed.

Participants work in groups of three, and group membership is fixed for the week. Where a group of four is unavoidable, the fourth member takes the fourth role on Day 4. Each afternoon draws exclusively on the pack for that day. Where a fee, a deadline, or a legal rule does not appear in the pack, participants are required to record it as "to be confirmed" rather than to supply a value of their own. Centre No. 3, the meetings described, and every figure in the packs are invented for the purposes of the exercise. The procedural wording follows individual-entrepreneur registration as published on [my.gov.uz](https://my.gov.uz), together with the publicly reported "start a business in 15 minutes" arrangement in force from January 2026: once an application is complete, registration takes no more than thirty minutes. An electronic signature, a bank account, and a cash register fall outside that thirty-minute period.

## 2. Structure of the week

Days 1 to 3 each address a single technique and then apply it immediately to the pack for that day. Day 4 is given over to the group project, in which all three are used together.

| Day | Topic | Lab | Module |
| --- | --- | --- | --- |
| Day 1 — Mon 9 Nov | Agent fundamentals and tool-calls | `materials/day1-website/` | [`lessons/01-tool-calls.md`](lessons/01-tool-calls.md) |
| Day 2 — Tue 10 Nov | Retrieval, knowledge base, and memory | `materials/day2-briefing/` | [`lessons/02-rag-memory.md`](lessons/02-rag-memory.md) |
| Day 3 — Wed 11 Nov | Planning, workflow, and multiple agents | `materials/day3-budget/` | [`lessons/03-planning-workflow-multiagent.md`](lessons/03-planning-workflow-multiagent.md) |
| Day 4 — Thu 12 Nov | Group project | one topic pack per team | [`lessons/04-group-project.md`](lessons/04-group-project.md) |

Days 2 and 3 follow an identical timetable: teaching and a live demonstration from 14:00 to 15:00, group work from 15:00 to 16:30, and a debrief from 16:30 to 17:00. The debrief is not a presentation. Each group reports what it produced, which file it cited, and one instance in which a person corrected the agent.

Day 1 opens with [`lessons/00-agent-basics.md`](lessons/00-agent-basics.md) from 14:00 to 14:25. That session covers what distinguishes an agent from a chatbot, the observe–think–act cycle as watched on screen rather than drawn as a diagram, the anatomy of a single tool call — its name, its arguments, its result — the distinction between tools that read and tools that write, and the read-only boundary. Teaching then runs from 14:25 to 15:10, and the lab begins at 15:10.

Day 4 allocates 14:00–14:20 to the brief and the distribution of topics, 14:20–16:00 to group work, and 16:00–17:00 to the final presentations.

The course is conducted entirely through CodeBuddy Code. Participants write no program code: each technique is taught through the agent's own observable conduct. Tool-calling is watched in the agent's own `Read`, `Grep`, and `Write` calls; retrieval is the pack folder, addressed with `@` and with search, and the cited filename is the retrieval trace; memory is the distinction between the present conversation and `CODEBUDDY.md`; and the planner, executor, and reviewer are plan mode, the build prompts, and the read-only review roles in `.codebuddy/agents/`.

The run sheet, the preparation checklist, and guidance on what to point to when a group stalls are set out in [`materials/instructor-prep.md`](materials/instructor-prep.md).

## 3. Day 1, Monday 9 November — agent fundamentals and tool-calls

**Learning outcome.** By the close of the afternoon, a participant can read a tool call, direct the agent's tools at the correct files by means of the prompt, and obtain a usable first draft that leaves an auditable trail.

**Taught material.** What distinguishes a language model, a chatbot, and an agent; the observe–think–act cycle; the anatomy of a tool call, being its name, its arguments, and its result; which tools read and which write, and the setting of permission by tool rather than by agent; the three ways in which a call returns nothing, and what the agent should do in each; the five components of a task prompt — role, source boundary, deliverable, constraints, and done-condition; the referencing of files with `@`; and the practice of requiring the agent to write "to be confirmed" in place of a plausible invented number, which is error handling expressed as a sentence.

The demonstration runs `prompts/day1-weak-prompt.txt` and `prompts/day1-strong-prompt.txt` against the same pack, so that the room observes the difference in the output rather than receiving it as an argument in the abstract. The room is asked to count the tool calls each prompt produces before the draft appears: the weak prompt makes very few, having been given no reason to open anything.

**Lab and deliverable.** The lab is held in `materials/day1-website/`, and the deliverable is `index.html`. The page addresses three services only: individual-entrepreneur registration, a PINFL, and an appointment for an electronic signature. It states what the applicant must bring, the two available channels (the service desk and my.gov.uz), the point at which the thirty minutes begin, the address `12 Mirzo Ulugbek Street`, the telephone number `+998 66 555 01 03`, and the opening hours; and it answers each of the questions raised in `resident-questions.txt`.

**Pass condition.** The five items listed in `do-not-invent.md` must appear as "to be confirmed". A page that states a state fee in som has failed the day, however well presented it may otherwise be.

## 4. Day 2, Tuesday 10 November — retrieval, knowledge base, and memory

**Learning outcome.** By the close of the afternoon, a participant can make the agent answer from a named body of documents rather than from what it happens to know, and can leave behind a trail by which a colleague may repeat the lookup and obtain the same answer.

**Taught material.** The pack folder understood as a knowledge base, and the vocabulary that attaches to it — indexing, retrieval, grounding, and the citation as retrieval trace; the ordering of search before reading, so that an answer is not taken from whichever file was opened first; the three cases in which a corpus may stand, being that it answers the question, that it contradicts itself, or that it is silent, of which only the third is difficult; the three kinds of memory, being the present conversation, `CODEBUDDY.md`, and the read-only pack, and what belongs in each; what must be retained nowhere, personal data in particular; the `decision-brief` skill and the principle of progressive disclosure, by which method is loaded on demand exactly as fact is; and the conduct of an independent review with `prompts/review.txt`, in preference to asking the agent to assess its own work.

The counterfactual test is the centre of the hour: the agent is instructed to retain an unsupported claim, and refuses, citing `october-snapshot.md`. The rule came from memory and the figure that made the refusal defensible came from retrieval; either alone would have been weaker.

**Lab and deliverable.** The lab is held in `materials/day2-briefing/`. Participants act as aides to the deputy of the Agency for Public Services, and the question before them is why residents do not experience "15 minutes" in practice. All groups receive the same pack but a different brief: Economy ranks by days to operate, Digital by returns and the form, and Social by access in Karakalpakstan. The cards are held in [`materials/role-cards.md`](materials/role-cards.md); they should be printed, cut, and issued one per group at the start of the lab.

Groups establish where the time is in fact spent, which lines in `old-deck.md` the remaining files do not support, and what may be decided tomorrow as against what must wait. The deliverables are a `briefing.md` of approximately two pages, with a source filename given after each conclusion, and a `slides.md` of exactly six slides.

## 5. Day 3, Wednesday 11 November — planning, workflow, and multiple agents

**Learning outcome.** By the close of the afternoon, a participant can break a decision into steps, arrange those steps into a workflow with the checkpoints in the proper places, distribute them among specialist roles, and synthesize the results rather than concatenate them.

**Taught material.** The decomposition of a task into steps, and the reading of the dependencies among them, by which it is determined what must run in order, what may run at once, and where the task branches; where the state of a task resides between steps, and the consequence that a subagent shares nothing implicitly and must be told what it needs; plan mode as the checkpoint at which decomposition is agreed before anything is produced, together with the refusal to approve a first plan; the four shapes of workflow — sequential, parallel, conditional, and human-in-the-loop; the three roles of planner, executor, and reviewer, and the structural requirement that the reviewer not be the producer; why an isolated context is preferable to a single long conversation; least privilege, exercised through the three read-only roles defined in `.codebuddy/agents/`; delegation in parallel; and the synthesis step, understood as an account of consensus, conflict, what was adopted, and what was rejected and on what grounds.

The session also treats the question of which decisions genuinely require a person, and the observation that a checkpoint which is rubber-stamped is worse than none, since it leaves a signature; and the circumstances in which neither planning nor delegation is warranted, which is the majority of cases.

**Lab and deliverable.** The lab is held in `materials/day3-budget/`. The file `regional-kpis.xlsx` records May to October 2026 for four service areas, reporting applications, days to operate, return rate, staff, spend, and satisfaction. The quarter can fund one action in one area: additional staff, a simpler form, or a status-tracking page. The deputy currently places speed first; groups also address whether the choice holds if accuracy is placed first instead.

The deliverables are a `dashboard.html` or `dashboard.xlsx` containing a comparison table, one chart, and both priorities, together with a `memo.md` of half a page. The final twenty minutes are reserved for the second priority.

**Rationale for delegation.** This pack rewards delegation because the roles genuinely disagree: speed first points in one direction and accuracy first points in another. A group that obtains a single answer from three agents has not, in substance, run three agents.

## 6. Day 4, Thursday 12 November — group project and final presentation

**Learning outcome.** Each team takes one topic in public service, produces the stated deliverables, and presents for five to ten minutes. The three techniques of the preceding days are used together, and no one directs which is to be applied where.

**Allocation.** At 14:00 each team draws one of the five topics. Two teams may share a topic; they present separately, and the divergence between them is itself worth discussion.

| Topic | Pack | Deliverables |
| --- | --- | --- |
| Benefit eligibility advice | `materials/day4-benefits/` | `eligibility-guide.md`, `case-assessments.md`, `information-requests.md` |
| Complaint and service-ticket handling | `materials/day4-complaints/` | `triage.md`, `replies.md`, `escalations.md` |
| Public service navigation | `materials/day4-interagency/` | `journey.md`, `interagency-sop.md`, `conflicts.md` |
| Public consultation synthesis | `materials/day4-consultation/` | `synthesis.md`, `decision-note.md`, `response-table.md` |
| Home sewing workshop service | `materials/day4-service/` | `public-page.html`, `internal-sop.md`, `letters.md` |

**Division of labour within a team.** Four roles are assigned at 14:20 and stated aloud: the Agent Designer, who owns the prompts and the written done-condition; the Tool and Retrieval Engineer, who owns the search across the pack and the citation trail behind every claim; the Workflow Engineer, who owns the order of the work, the delegation, and the merge by which the three deliverables are made to agree; and the Evaluator and Presenter, who owns the test cases, the check upon privacy and risk, the timer, and the presentation. A team of three merges the last two roles. Whoever produced a deliverable does not certify it.

**Contradictions in the packs.** Every pack contains at least one contradiction between two files, and a team that reads only one source will reach the wrong conclusion. Identifying the contradiction and stating which source was followed forms part of the work rather than an obstacle to it.

**Presentations.** Presentations run from 16:00 to 17:00, eight minutes for each team with two minutes to change over. Where more than six teams are present, presentations begin at 15:45 and each is capped at five minutes. The requirements are set out in [`materials/presentation-rubric.md`](materials/presentation-rubric.md): the decision reached, the source file behind each claim, one instance in which a person corrected the agent, one item left at "to be confirmed", and an account of where each of the three days' techniques was used.

**Scoring.** Six weighted dimensions, set out in the same file: the definition of the problem and its public-service value, at fifteen per cent; the completeness of the deliverables, at twenty-five; the appropriate use of the week's techniques, at twenty-five; accuracy, robustness, and the handling of error, at fifteen; usability and the clarity of the demonstration, at ten; and privacy, safety, and social impact, at ten. The last of these is satisfied by one honest paragraph and not by a disclaimer.

A team that presents a polished document whose claims it cannot source has not completed the week. A team that presents a plain document and can defend every line has.
