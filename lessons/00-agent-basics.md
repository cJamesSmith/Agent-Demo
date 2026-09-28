# Lesson 0: What an Agent Is, and the Read-Only Boundary

**Day 1 — Monday, 14:00–14:25**

## Learning Objectives

- Say what separates an agent from a chatbot, in one sentence, without using the word "smart".
- Name the four stages of the loop while watching them happen on screen.
- Read a single tool call — its name, its arguments, its result.
- Know which of the agent's tools read and which of them write.
- Confirm your pack is complete before you start.
- Build the habit of establishing a boundary before the agent writes anything.

## Three Things That Are Often Confused

The difference is not how clever each one is. It is what each one can do about something it does not know.

| | What it does | What it does when it does not know |
|---|---|---|
| A language model | Produces text from a prompt | Produces plausible text anyway |
| A chatbot | Produces text across a conversation | Produces plausible text anyway, in context |
| An agent | Produces text, and acts | Goes and looks, then reports what it found — or that it found nothing |

Only the third row can be checked against a file. That is the whole reason this week uses one.

An agent that invents a state fee has not stopped being an agent. It has been allowed to behave like the first row, which is what the next module is about.

## The Loop

Observe → think → act → observe. The agent reads something, decides what it needs next, does one thing, and reads the result. Then again, until the task is done or it runs out of moves.

You are not going to memorise that. You are going to watch it.

## Step 1: Open the Working Folder

Open this project folder in CodeBuddy Code. Everything the agent can see is inside it: the packs in `materials/`, the project rules in `CODEBUDDY.md`, the prepared prompts in `prompts/`.

You do not paste your source files into the conversation. You point at them.

## Step 2: Ask the Agent to Read the Pack

Type:

```text
Do not modify any files yet. Read everything in @materials/day1-website/ and tell me in no more than eight lines:
1. What is my task?
2. Which files am I allowed to use?
3. What must I deliver?
4. What am I explicitly forbidden from inventing?
```

### Observe

Watch the lines that scroll past before the answer arrives. Each one is an act in the loop — a file opened, a folder listed, a search run. Name three of them out loud before you read the answer.

The agent should open several files on its own rather than asking you to supply them one at a time. That is the clearest practical difference between a coding agent and a chat window.

It should also find `do-not-invent.md` without being told the filename. If it does not mention the five forbidden items, your source boundary was not clear enough — which is exactly what the next module is about.

## Step 3: Read One Tool Call

The acts you just watched come from a small, fixed set. Each one is a **tool call**, and every tool call has the same three parts.

| Part | Today's example |
|---|---|
| **Name** — which tool | `Read` |
| **Arguments** — what to run it on | `materials/day1-website/centre-facts.md` |
| **Result** — what came back | The forty lines of that file, or an error |

That is the whole mechanism. The model does not open a file; it asks for a named tool with specific arguments, something outside the model runs it, and the result comes back into the conversation as new text. The model then decides what to ask for next.

Scroll back to the calls from Step 2 and read three of them in those three parts, out loud. The arguments are the part worth watching: a tool called on the wrong path returns nothing useful, and the agent has to notice and try again.

### Which Tools Write

| Tool | What it does | Changes the disk |
|---|---|---|
| `Read` | Opens one file | No |
| `Grep` | Searches file contents | No |
| `Glob` | Finds files by name | No |
| `Write` | Creates or replaces a file | Yes |
| `Edit` | Changes part of a file | Yes |
| `Bash` | Runs a shell command | Yes, and anything else |

The first three cannot damage your pack. The last three can. This is why the three review roles you will meet on Day 3, in `.codebuddy/agents/`, are given only `Read`, `Grep`, and `Glob`. A role whose job is to check your work has no business rewriting it.

Permissions are set per tool, not per agent in the abstract. "What can this agent do?" is answered by the list of tools it holds.

## Step 4: Watch a Tool Call Fail

A tool call can come back empty. That is not a malfunction — it is one of the two normal outcomes, and what the agent does next is the whole question.

Ask for something that is not there:

```text
Do not modify any files. What does @materials/day1-website/ say the state fee is, in som?
```

### Observe

The agent searches, finds nothing, and should tell you so. That is a successful failure: the call returned no result and the loop reported it.

There are three ways a call comes back with nothing, and they are not equally innocent:

| What happened | What the agent should do |
|---|---|
| The path was wrong | Correct the arguments and call again |
| The tool worked, the file has no such fact | Report the gap — "to be confirmed" |
| The tool was the wrong choice | Pick a different tool, not a different answer |

The middle row is the one this week is built around. The failure mode is the fourth, unlisted option: nothing in the pack answers the question, so the agent falls back on general knowledge about business registration in Uzbekistan and produces a number. It is a fluent number. It is not from your files, and no one reading the page will be able to tell.

The model did not lack the fact. The call had nowhere to look and no instruction about what to do then. The weak-prompt demonstration in the next module is exactly this failure, at full size.

## Step 5: Check the Project Rules

Type:

```text
Read CODEBUDDY.md and list the rules that will constrain today's page.
```

These rules load in every session, including tomorrow's. You did not have to repeat them. That is project memory, and it is Day 2's subject.

## Why "Do Not Modify Any Files Yet"

You are establishing a boundary before the agent has the chance to act on a misunderstanding. Reading is cheap and reversible. Writing twelve files based on a misread task is neither.

## When the Agent Is the Wrong Tool

When you already know the answer, an agent is a slow way to write it down. When the task needs a judgement only a person is allowed to make — whether to publish, whom to escalate to, which of two ministries is right — an agent can assemble the evidence and must not make the call.

And when nothing in the folder can answer the question, the honest output is "to be confirmed", not a search of the wider internet. An agent is only as good as the boundary you drew around it.

## Checkpoint

Answer all four:

- What does the agent work on? — The files in the whole folder, plus the tools configured for the project.
- What are the three parts of a tool call? — The name, the arguments, and the result.
- Why say "do not modify files" first? — To confirm the agent understood the task before it acts on its understanding.
- What separates an agent from a chatbot? — An agent can go and look, so its answers can be checked against a file.

Next: [`01-tool-calls.md`](01-tool-calls.md)
