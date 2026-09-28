# Lesson 1: Directing Tool Calls

**Day 1 — Monday, 14:25–15:10 teaching. Lab 15:10–16:30.**

## Learning Objective

Write a prompt that sends the agent to the right files with the right tools, produces a usable first draft, and leaves an auditable trail — so that a colleague can check every line against a source file without asking you where it came from.

## Your Prompt Is the Tool Configuration

The previous module took a tool call apart: a name, arguments, a result. You do not type tool calls. You write a prompt, and the prompt decides which tools fire and what arguments they get.

| What your prompt says | What the agent does |
|---|---|
| Nothing about sources | Few or no `Read` calls. It answers from training |
| "Use only `@materials/day1-website/`" | `Glob` the folder, then `Read` each file |
| "Check whether a state fee appears anywhere" | `Grep` across the pack, and report an empty result |
| "Write `index.html`" | One `Write`, after the reads |

This is the practical lever. You cannot reach into the loop and correct an argument mid-run, so the prompt is where you aim it — before it starts, not after.

## The Five Parts of a Task Prompt

Most weak prompts are missing three of these.

| Part | The question it answers | Weak | Strong |
|---|---|---|---|
| Role | Who is writing, for whom? | *(absent)* | "You write for residents at the intake desk, not for officials." |
| Source boundary | What may it use? | *(absent — so it uses everything it knows)* | "Use only the files in `@materials/day1-website/`." |
| Deliverable | What exactly comes out? | "a webpage" | "One file, `index.html`, that opens in a browser with no server." Shape the output and you can check it; ask for "a webpage" and you get prose about webpages. |
| Constraints | What must it not do? | *(absent)* | "If a fee is not in the files, write 'to be confirmed'. Do not describe this as company registration." |
| Done-condition | How do we know it is finished? | *(absent)* | "Every question in `resident-questions.txt` has a visible answer on the page." |

A prompt missing the source boundary produces confident invention. A prompt missing the done-condition produces something that looks finished and is not.

## Step 1: Watch the Two Prompts (demonstration)

The instructor runs both against the same pack.

```text
@prompts/day1-weak-prompt.txt
```

Then, in a fresh conversation:

```text
@prompts/day1-strong-prompt.txt
```

### Observe

Look at three specific places in the two outputs:

1. **The state fee.** The weak prompt almost always produces a number in som. That number is not in any file in the pack. It is invented, and it is the kind of invention that gets a public page taken down.
2. **The 30 minutes.** The weak prompt tends to promise that the whole visit takes 30 minutes. The pack says the clock starts only after the application is complete, and excludes the PINFL, the electronic signature, the bank account, and the cash register.
3. **Company registration.** The weak prompt often drifts into LLC language, because that is the more common thing on the internet. This service is individual-entrepreneur registration.

None of these are model failures. All three are prompt failures. The pack contains the correct answer in every case.

### Watch the Tool Calls, Not Only the Output

Run the two prompts again and count the calls before the first draft appears. The weak prompt makes very few — often none. It had no reason to open anything, so it did not, and everything on the page came from training data.

The strong prompt produces a visible trail: the folder listed, each file read, a search for the fee that comes back empty. Same model, same pack. The difference is that one prompt sent the agent to the files and the other did not.

This is the failed tool call from the previous module, at full size — the fourth, unlisted option in that table. The agent looked, found nothing, and had no instruction about what to do then, so it fell back on general knowledge. The fix is not a better model. It is a boundary and a rule about silence.

## Step 2: Reference Files Instead of Pasting

`@` points the agent at a file or a folder:

```text
@materials/day1-website/centre-facts.md
```

This is better than pasting the text for three reasons: the file stays the single source of truth, the agent can re-read it when it needs to, and the source filename is available for the citation you will have to write anyway.

## Step 3: Force "To Be Confirmed"

This is error handling, written as a sentence. An empty result is a normal outcome, and the prompt has to say what to do with one. The single most useful sentence in a government prompt:

> If a fee, a waiting time, or a legal limit is not written in the files, print "to be confirmed". Do not estimate it.

Without that sentence the agent has two options on an empty result — invent, or stop. It will invent, because inventing looks more helpful. The sentence gives it a third, and the third is the only one you can publish.

Test that it worked. Type:

```text
List every item on the page that is marked "to be confirmed", and for each one, state which file you looked in before concluding it was missing.
```

Five items should appear, matching `do-not-invent.md`. Note what the question asks for: not just the list, but the file the agent checked before concluding the fact was absent. An item marked "to be confirmed" with no file behind it is a guess that happened to be cautious.

If fewer than five appear, something was invented. Find it now, not during the presentation.

## Step 4: Iterate on the Prompt, Not the Output

When a draft is wrong, the instinct is to hand-fix the output. Resist it once, as an exercise. Instead, name the rule that was missing and add it:

```text
The page says a relative can collect a PINFL. centre-facts.md says the applicant must come in person and a relative cannot apply or collect. Correct that line, and tell me which part of my instructions allowed that error through.
```

Hand-fixing repairs one line. Fixing the prompt repairs the same class of error everywhere it occurs — including the next three days.

## Lab: The Resident Page

`materials/day1-website/`. Done means `index.html`, with an answer to each of the six questions in `resident-questions.txt`, and the five items from `do-not-invent.md` marked "to be confirmed".

Before your debrief, a person — not the agent — checks the phone number, the hours, and the document lists against `centre-facts.md`. The footer reads `Prepared with CodeBuddy Code, reviewed by [group names]`. Put your actual names there. You are signing it.

## When a Long Prompt Is Not the Answer

Length is not the point; specificity is. "Fix the typo in the heading" needs no role, no constraints, no done-condition. Invest in the prompt when the task is multi-file, when a wrong answer is expensive, or when someone else will have to verify the result.

## Checkpoint

Complete the sentence:

> The weak prompt invented a state fee not because the model lacked the fact, but because nothing in the prompt told it ________.

Suggested answer: which files were the only permitted source, and what to do when the answer was not in them.

And one more, in your own words: what in a prompt decides how many files the agent opens?

Next: [`02-rag-memory.md`](02-rag-memory.md)
