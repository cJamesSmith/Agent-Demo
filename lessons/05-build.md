# Lesson 5: Let the Agent Build the Website

**Time: 15–25 minutes**

## Learning Objectives

- Execute from the reviewed plan instead of generating a new approach arbitrarily.
- Have the Agent create, run, and validate a complete website.
- Make one strategic-direction change through natural language.

## Step 1: Begin Implementation

Exit Plan Mode before building: press `Shift+Tab` until the status bar shows **Accept Edits**. This mode allows file edits while still asking before other tool actions such as terminal commands.

Enter in CodeBuddy Code:

```text
/executive-dashboard Using the approved plan, project Memory, and synthesized findings from the three Subagents, execute @prompts/build-dashboard.txt
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

You can also ask CodeBuddy Code to run the server for you:

```text
Run python3 -m http.server 8000 in the background and tell me when the site is ready.
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
