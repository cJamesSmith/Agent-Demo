# Lesson 3: Skills—Turn a Method into a Reusable Capability

**Time: 8–12 minutes**

## Learning Objectives

- Inspect the Skill provided by this project.
- Understand the relationship between a Skill, a one-time Prompt, and a Slash Command.
- Ask the Agent to load the executive decision-dashboard methodology.

## Step 1: List Skills

Enter in CodeBuddy Code:

```text
/skills
```

Find `executive-dashboard`. If it does not appear, create it.

## Step 2: Invoke It Explicitly

Enter:

```text
/executive-dashboard Southeast Asia market entry
```

Then ask:

```text
What concrete methods does this Skill add for this project that CODEBUDDY.md alone does not provide?
```

Expected topics include scoring rules, page structure, evidence labels, recommendations and counterarguments, and sensitivity analysis.

## Step 3: Observe Progressive Loading

The Skill directory contains:

```text
.codebuddy/skills/executive-dashboard/
├── SKILL.md
├── references/scoring.md
└── templates/page-outline.md
```

The Agent normally sees only the Skill's name and description. It loads the main instructions when the Skill is triggered, then reads the scoring reference and page template only when needed. This is called “progressive disclosure.”

## Skill and Slash Command

- `/help`, `/memory`, and similar entries are built-in Slash Commands.
- Custom capabilities are now best implemented as Skills.
- A user-invocable Skill also provides an entry point such as `/executive-dashboard`.
- The Agent can also match a Skill automatically, and a Skill can include templates, scripts, and reference materials.

## Checkpoint

Explain in one sentence:

> Memory stores ________; a Skill stores ________.

Suggested answer: persistent context and rules; specialized methods and workflows loaded on demand.

Next: [`04-subagents.md`](04-subagents.md)
