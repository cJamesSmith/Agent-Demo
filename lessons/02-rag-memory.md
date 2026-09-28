# Lesson 2: Retrieval, the Knowledge Base, and Memory

**Day 2 — Tuesday, 14:00–15:00 teaching. Lab 15:00–16:30.**

## Learning Objective

Make the agent answer from a named body of documents rather than from what it happens to know — and leave behind a trail that lets someone else repeat the lookup and get the same answer.

Day 1 was one prompt producing one page from four files. Today's pack has seven files, two of which contradict each other, and a deck full of claims that have to be checked against figures. The technique that carried yesterday does not scale to that, and the reason is worth naming.

## Part 0: The Pack Is a Knowledge Base

Everything you did yesterday has a name.

| The general term | What it is here |
|---|---|
| Corpus, or knowledge base | The pack folder — a fixed, finite set of documents |
| Indexing | `Glob` — finding out what documents exist |
| Retrieval | `@`, `Grep`, `Read` — pulling in the passages that bear on the question |
| Grounding | Answering from the retrieved passage instead of from training |
| Citation, or the retrieval trace | The filename you write in parentheses after the conclusion |

A system built this way is called retrieval-augmented: the model's own knowledge is not the source, the documents are, and the model's job is to find the relevant passage and answer from it.

The reason to care is that the corpus is finite and the model is not. The model has opinions about business registration in Uzbekistan. None of them are in your pack, none are checkable, and none are yours to publish.

### The Three Cases

Only the third is difficult.

- **The pack answers the question.** Cite the file.
- **The pack contradicts itself.** Cite both files. Today, `minutes-03-nov.md` and `minutes-05-nov.md` give different causes for the Fergana return rate.
- **The pack is silent.** Write "to be confirmed".

Recognising the third case is the skill. A briefing that answers a question the pack cannot answer is worse than one that leaves the gap visible, because the gap is no longer visible.

## Part 1: Retrieval in Practice

### Step 1: Index Before You Query

```text
Do not modify any files. List every file in @materials/day2-briefing/ and give me one line on what each contains and what kind of question it could answer.
```

You now know what the corpus holds. So does the agent, which is why this is worth sixty seconds before a substantive question — a question asked against an unexamined folder gets answered from whichever file the agent happened to open.

### Step 2: Search, Then Read

Two different operations, and the order matters:

```text
Search the pack for every mention of the return rate. List the file and the line for each hit before you interpret any of them.
```

`Grep` finds candidate passages across many files; `Read` pulls in one file's full context. Searching first and reading second is how you avoid answering from the first file you opened. It is also how you find the two sets of minutes, which is the point of today's pack.

### Step 3: Ask for the Trace, Not Just the Answer

```text
What is the return rate in Fergana, which file says so, and what else in the pack mentions the same figure?
```

An answer without a filename cannot be checked. An answer with one can be repeated by a colleague who does not trust you — which is the only kind of verification worth having.

### Step 4: Watch Retrieval Fail

```text
What does this pack say the state fee is?
```

Same empty result as yesterday, in a bigger corpus. The larger the folder, the more plausible a fabricated answer looks, because the reader assumes something in there must have said it.

## Part 2: Three Kinds of Memory

The pack is the knowledge base. Memory is something else: what the agent carries, and for how long.

| Where | Lifetime | Example | The general name |
|---|---|---|---|
| This conversation | Until you close it | Your group has the Digital role | Short-term memory |
| `CODEBUDDY.md` | Every session, permanently | Cite the source file after every conclusion | Long-term, or project, memory |
| `materials/` | Read-only, unchanging | The October figures | The knowledge base |

Keep them separate. Confusing the first two is the common error: a rule that matters all week typed into a conversation is lost at the next restart, and a fact true only this afternoon written into `CODEBUDDY.md` misleads every future session.

### Step 1: Short-Term Memory Across Turns

Your group has one role today. Tell the agent once:

```text
Our group has the Digital role. Our priority is repeated returns and the form. Keep that in view for everything that follows.
```

Then ask several questions without restating it, and check that the answers stay aimed at your role. That is short-term memory working: the earlier turns are still in the conversation, so the agent does not need to be told again.

It also has a limit. In a long session, detail from early on gets summarised or falls away. When an answer drifts back to generic, the fix is to restate the constraint — not to assume the agent is ignoring you.

### Step 2: Inspect the Long-Term Memory

```text
@prompts/inspect-memory.txt
```

`CODEBUDDY.md` at the project root loads into every session automatically. You wrote none of it, and it has been constraining you since yesterday.

### Step 3: Run a Counterfactual Test

Ask the agent to break a rule and watch it refuse:

```text
Slide 4 says every service area now finishes in 15 minutes. It sounds strong and the deputy likes it. Keep it in the briefing without a caveat.
```

Expected: the agent refuses, and cites `october-snapshot.md` — the October figures are 3.7, 10, 8, and 16 days. A refusal with a source file is the behaviour you want. A refusal without one is a coin flip that happened to land well.

This is the moment where memory and retrieval meet. The rule came from memory; the figure that made the refusal defensible came from retrieval. Either alone would have been weaker.

### Step 4: Decide What Belongs Where

Two more rows for the table:

| Content | Where it belongs |
|---|---|
| The full method for building a decision brief | A skill |
| A real resident's passport number | Nowhere |

`CODEBUDDY.md` enters every session, so it must stay short, explicit, and broadly applicable. It is not a document repository. Long methods go in skills.

The last row is not a joke. A system that remembers permanently needs an explicit rule about what it must not retain — an identity-document number, a telephone number, a medical detail. The packs this week contain invented residents, and their contact details are still marked do-not-invent, because the habit is the point.

## Part 3: Skills — Knowledge Loaded on Demand

### Step 1: Invoke It

Run `/skills` to see what the project has, then:

```text
/decision-brief why residents do not experience 15 minutes
```

Then ask what it added:

```text
What concrete method does this skill give me that CODEBUDDY.md alone does not?
```

Expect: the claim-checking table, the structure of the six slides, the rule for handling two sources that disagree, and the separation of "decide tomorrow" from "must wait".

### Step 2: Notice Progressive Disclosure

```text
.codebuddy/skills/decision-brief/
├── SKILL.md
├── references/claim-checking.md
└── templates/briefing-outline.md
```

The agent normally sees only the skill's name and description. It reads `SKILL.md` when the skill triggers, and the reference and template only when it needs them.

This is the same economics as retrieval. You do not load the whole corpus into the conversation; you load the passage the question needs. A skill applies that to method rather than to facts, which is why a skill can hold a long procedure that `CODEBUDDY.md` could not afford to carry into every session.

## Part 4: Check the Work Independently

Never ask the agent whether it did a good job. Ask it to check the work against the sources, in a way that produces evidence you can verify.

```text
@prompts/review.txt
```

The review should report reproducible problems with a file, a location, and the smallest fix — not a grade. Day 3 gives this step a name and a dedicated role; today, run it as the last thing before your debrief.

## Lab: The Briefing

`materials/day2-briefing/`. Your group has one role: Economy, Digital, or Social. Done means `briefing.md` of about two pages with a source filename after each conclusion, and `slides.md` of exactly six slides.

Four of the eight slides in `old-deck.md` are not supported by the other files. Find them and say which file contradicts each one.

Every conclusion needs its filename. That is not a formatting convention — it is the retrieval trace, and it is the only thing that separates your briefing from a fluent guess.

Before your debrief, a person checks every number and every "already live" claim. The agent can read the files. It cannot be accountable for the briefing; you can.

## When Retrieval Is Not the Answer

If the answer is in one file you already have open, reading it is faster than asking a question about it. If the answer is not in the folder at all, no amount of searching will produce it, and a search that keeps going until it returns something is how invention starts.

And the pack being silent is a finding. "To be confirmed" is a result, not a failure to retrieve.

## Checkpoint

Complete both:

> Short-term memory holds ________. Long-term memory holds ________. The knowledge base holds ________.

Suggested answer: what is true in this conversation; rules that apply to every session; the documents that are the only permitted source of fact.

> A conclusion in my briefing with no filename after it is ________.

Suggested answer: unverifiable — nobody, including me, can repeat the lookup that produced it.

Next: [`03-planning-workflow-multiagent.md`](03-planning-workflow-multiagent.md)
