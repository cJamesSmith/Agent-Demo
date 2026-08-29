# Lesson 5: Let the Agent Build the Website

**Time: 15–25 minutes**

## Learning Objectives

- Execute from the reviewed plan instead of generating a new approach arbitrarily.
- Have the Agent create, run, and validate a complete website.
- Make one strategic-direction change through natural language.

## Step 1: Begin Implementation

Enter in Claude Code:

```text
Using the approved plan, project Memory, executive-dashboard Skill, and synthesized findings from the three Subagents, execute @prompts/build-dashboard.txt
```

The Agent should create `site/` in the project root rather than modify `reference/site/`.

## Step 2: Run the Structural Check

Run in the terminal:

```bash
python3 checks/check-project.py student
```

A structural check proves only that key elements exist, not that the website is usable.

## Step 3: Run the Website

Run in the terminal:

```bash
python3 -m http.server 8000
```

Open:

```text
http://localhost:8000/site/
```

You can also ask Claude Code to use `/run` directly:

```text
/run
```

## Step 4: Perform Manual Acceptance Testing

Test each item:

- Switch among the growth-first, profit-first, and risk-first scenarios.
- Adjust a weight and confirm that the ranking updates immediately.
- Confirm that the weights always total 100%.
- Expand sources and assumptions.
- Narrow the browser window and confirm that the page does not overflow horizontally.
- Confirm that the recommendation section also presents a counterargument.

## Step 5: Simulate a Last-Minute Executive Priority Change

Enter:

```text
Please execute @prompts/executive-change.txt
```

Observe whether the Agent preserves the existing scenarios and explains the recommendation change instead of only editing a heading.

## Checkpoint

The website must let viewers distinguish among:

- Facts in the data table.
- Inferences made by researchers or the Agent.
- Assumptions that still need validation.

Next: [`06-slash-commands.md`](06-slash-commands.md)
