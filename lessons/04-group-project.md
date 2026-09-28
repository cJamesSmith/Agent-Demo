# Lesson 4: Group Project and Final Presentation

**Day 4 — Thursday. Brief 14:00–14:20. Work 14:20–16:00. Presentations 16:00–17:00.**

## What Today Is

The first three days each taught one technique against a pack designed to teach it. Today nobody tells you which to use. Your team takes a public-service topic, produces the deliverables, and defends them for 5–10 minutes.

You will use all three days' work: tool-calls aimed at the right files, retrieval with a citation trail, and a planned workflow with a review step. Where you use each is your decision, and you will be asked about it.

## The Five Topics

Each team draws one at 14:00. Two teams may share a topic — they present separately, and the differences are worth the discussion.

| Topic | Pack | Deliverables |
|---|---|---|
| Benefit eligibility advice | `materials/day4-benefits/` | `eligibility-guide.md`, `case-assessments.md`, `information-requests.md` |
| Complaint and service-ticket handling | `materials/day4-complaints/` | `triage.md`, `replies.md`, `escalations.md` |
| Public service navigation | `materials/day4-interagency/` | `journey.md`, `interagency-sop.md`, `conflicts.md` |
| Public consultation synthesis | `materials/day4-consultation/` | `synthesis.md`, `decision-note.md`, `response-table.md` |
| Home sewing workshop service | `materials/day4-service/` | `public-page.html`, `internal-sop.md`, `letters.md` |

Read your pack's `README.md` first. It states the task, the deliverables, and the rules. Then read `do-not-invent.md` before you write a single prompt.

## Every Pack Contains a Contradiction

At least two files in your pack disagree with each other. This is deliberate, and it is not a puzzle to be solved by picking the more convincing file.

A team that reads one source will produce a confident, wrong document. A team that finds the contradiction, states it, says which source it followed and why, and flags the decision for a human has done the job correctly — even if the instructor would have chosen the other source.

Say this out loud in your presentation. It is the most valuable thing you will have found.

## Dividing the Work

The failure mode is one person driving the agent while two watch. Take a role each, at 14:20, out loud, so everyone knows who owns what.

| Role | Owns | Runs |
|---|---|---|
| **Agent Designer** | The prompts: role, source boundary, deliverable, constraints, and the written done-condition | The build prompts |
| **Tool / RAG Engineer** | Retrieval across the pack, and the citation trail behind every claim | `@` and search across the pack, `source-checker` |
| **Workflow Engineer** | The order of work, the delegation, and the merge — so the three deliverables agree with each other | Plan mode, `decision-challenger` |
| **Evaluator / Presenter** | Test cases, the privacy and risk check, the timer, and the presentation | `prompts/review.txt` |

**A three-person team merges Workflow Engineer with Evaluator / Presenter.** A four-person team uses all four. Do not add a second Presenter.

Two rules about these roles:

- **The Evaluator must not be the producer.** Whoever wrote a deliverable does not sign off on it. This is the same reason Day 3's three subagents are read-only.
- **The citation trail is a job, not a formatting pass.** The Tool / RAG Engineer has the least visible role and the one that decides whether the work survives a question. An unverified document is not a deliverable.

Suggested clock, 100 minutes:

- **14:20–14:35, together.** Read the pack. Agree what "done" means and write it down. Find the contradiction.
- **14:35–15:30, split.** By role, as above. The review runs over the draft as it appears, not after it is finished.
- **15:30–15:50, together.** Merge, resolve what the review found, mark every "to be confirmed".
- **15:50–15:55.** Run the self-check below.
- **15:55–16:00.** Run through the presentation once, out loud, with a timer.

## The Self-Check at 15:50

Seven lines. Read them out; the Evaluator asks, and whoever produced the thing answers.

1. All three deliverables exist and are not empty. Confirm with `python3 checks/check-project.py project <topic> <your folder>`.
2. Every substantive claim carries a filename.
3. Every item in your pack's `do-not-invent.md` reads "to be confirmed" in the deliverable.
4. The contradiction is stated, both filenames named, and the source you followed given with a reason.
5. Your own deliverables agree with each other on day counts and document lists.
6. One place a person corrected the agent is written down, in words you can say in the presentation.
7. Nothing in your deliverables exposes a resident's personal details beyond what the task needs, and you can say which check found that.

The checker answers line 1 only. It will pass a document that invents a fee and cites nothing. Lines 2 to 7 are people.

Any line you cannot answer is the next thing you work on, ahead of anything that would make the document look better.

## Suggested Use of the Week's Techniques

Not a prescription — a starting point.

- **Aimed tool-calls** for the first draft of each deliverable: role, source boundary, deliverable, constraints, done-condition. Check what the agent actually opened.
- **Retrieval and citation** as you go, not at the end. Search the whole pack before answering from the first file; carry the filename with the claim from the moment it appears.
- **Memory** is already working. `CODEBUDDY.md` is enforcing the source rule without you asking.
- **Planning** before you generate three interdependent files, so the day counts and document lists agree before they are written in three places.
- **Delegation** for the review pass, and for `decision-challenger` on whatever your team is most confident about.

## Test Cases, Before You Are Asked for Them

The Evaluator writes three questions a real resident would ask, before the deliverables are finished. Run them against what you have built and record what happened.

At least one should be a question your pack cannot answer. A deliverable that handles that question well — by saying what is unknown and who settles it — is the strongest thing you can show. One that answers it anyway is the failure this week is built to catch.

## The Presentation

5–10 minutes. The full requirements and the scoring weights are in `materials/presentation-rubric.md` — read it before you start work, not after. Five things must appear:

1. **The decision or product**, stated first, in one sentence.
2. **The source file** behind each substantive claim.
3. **One place a person corrected the agent** — what it produced, what was wrong, how you found it.
4. **One item left at "to be confirmed"**, and who would have to answer it.
5. **Where you used each of the three days' techniques**, and one place a technique was the wrong tool.

Open your actual deliverable on screen. Do not present slides about a document you do not show.

Point 3 is not a confession. A team that reports no corrections either did not check or is not saying. The instructor will ask.

Two dimensions of the score are easy to lose without noticing. **Accuracy and error handling** is where your test cases go — what you asked, what came back, what you fixed. **Privacy, safety, and social impact** is one honest paragraph: what personal detail your deliverable deliberately does not carry, which claim would need a person's approval before it reached a resident, and who is worst affected if you got something wrong. A team that has thought about the third question has usually found something about its own pack.

## What Fails

- A polished document whose claims cannot be traced to a file.
- A number that is not in the pack.
- "Incomplete documents" or equivalent vagueness where a specific reason was required.
- Deliverables that contradict each other — a public page and an internal procedure giving different day counts.
- A presentation that describes the process and never shows the product.

## What Passes

A plain document, every line traceable, contradictions flagged rather than smoothed over, gaps marked "to be confirmed" instead of filled in, and a team that can answer "where did that come from?" for any sentence on the page.

That is the whole week, and it is the part that transfers to real work on Monday.
