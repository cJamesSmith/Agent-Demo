# Lesson 2: Memory—Make the Agent Follow Project Rules

**Time: 8–10 minutes**

## Learning Objectives

- Understand that `CLAUDE.md` contains project instructions loaded across sessions.
- Distinguish persistent rules from one-time tasks.
- Verify that the Agent has read the Memory.

## Step 1: Inspect Memory

Enter in Claude Code:

```text
/memory
```

Select the project Memory and inspect the root-level `CLAUDE.md`.

If opening an editor is inconvenient in the classroom environment, enter:

```text
Read the project Memory and list the five most important items as “Rule → Effect on the website.”
```

You can also reference the prepared prompt:

```text
@prompts/inspect-memory.txt
```

## Step 2: Run a Counterfactual Test

Enter:

```text
To make the page seem more persuasive, can we hide the data gaps and show only the recommendation? Answer according to the project rules.
```

Expected result: the Agent should refuse to hide material uncertainty and point out the requirements to separate facts, inferences, and assumptions and to show counterarguments.

## Step 3: Decide What Should Be Remembered

| Content | Where It Belongs |
|---|---|
| Every executive page must lead with the conclusion | `CLAUDE.md` |
| Rename the title to “Southeast Asia Decision Room” today | Current conversation |
| A complete decision-dashboard production workflow | Skill |
| A real customer password or API key | Nowhere |

## Key Reminder

`CLAUDE.md` is not a document repository. It enters every session, so it should be short, explicit, and broadly applicable. Put long workflows in Skills; path-specific rules can go in `.claude/rules/`.

## Checkpoint

Enter:

```text
If I restart Claude Code tomorrow, which project constraints will still apply, and why?
```

The Agent should mention that the project-level `CLAUDE.md` loads automatically.

Next: [`03-skills.md`](03-skills.md)
