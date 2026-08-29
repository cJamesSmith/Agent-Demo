# Lesson 1: Planning—Approve the Approach Before Building

**Time: 10–15 minutes**

## Learning Objectives

- Let the Agent understand the materials and task in read-only mode.
- Review scope, scoring, risks, and validation.
- Experience how people retain control at key decision points.

## Step 1: Enter Plan Mode

Enter in Claude Code:

```text
/plan
```

You can also press `Shift+Tab` until the status bar shows Plan Mode.

> Plan Mode is a permission mode, not merely a prompt. File changes are blocked until the plan is approved.

## Step 2: Submit the Business Objective

Copy the contents of `prompts/plan.txt` into Claude Code, or reference it with `@prompts/plan.txt`.

```text
Please read @prompts/plan.txt and create the requested plan.
```

## Step 3: Review the Plan Like a Manager

Do not approve it immediately. Check whether the plan answers:

- Does it cover all seven website sections?
- Does it explain how scores are calculated from raw data?
- Does it separate facts, inferences, and assumptions?
- Does it preserve the strongest counterargument?
- Does it explain browser-level and code-level validation?
- Does it modify only `site/`, leaving the original inputs untouched?

Request at least one revision. For example:

```text
Revise the plan to add a sensitivity indicator showing whether the recommendation changes when data confidence falls. Also state explicitly that the source materials under inputs/ will not be modified.
```

## Step 4: Approve the Plan

Once no major questions remain, enter:

```text
The plan is approved. Do not implement it yet; I still need to complete the Memory, Skill, and Subagents lessons.
```

You deliberately delay implementation because the following lessons will load more organizational capabilities for the Agent.

## Checkpoint

Complete this sentence:

> The value of Planning is not making the Agent write a longer list; it is establishing a review boundary between ________ and ________.

Suggested answer: understanding/decision-making and file modification/execution.

## Why Not Plan Every Time?

A long plan adds cost without reducing risk when correcting a typo or changing one color. Planning is appropriate for multi-file tasks, multiple viable approaches, business rules, or work requiring explicit validation.

Next: [`02-memory.md`](02-memory.md)
