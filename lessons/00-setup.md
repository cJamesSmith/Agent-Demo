# Lesson 0: Understand the Task and Environment

**Time: 5–8 minutes**

## Learning Objectives

- Understand that Claude Code can read and work with an entire project, not just answer questions.
- Confirm that the course files are complete.
- Build the habit of defining the outcome and constraints before prescribing code.

## Step 1: Enter the Project

Run in the terminal:

```bash
cd /Users/bytedance/Agent-Demo
claude
```

If you already have a Claude Code session open in this directory, you do not need to restart it.

## Step 2: Ask the Agent to Introduce the Project

Enter in Claude Code:

```text
Do not modify any files yet. Explore this project and tell me in no more than eight lines:
1. What is my business task?
2. What input materials are available?
3. Which Claude Code capabilities are configured in the project?
4. What must I ultimately deliver?
```

### Observe

The Agent should proactively read multiple files instead of asking you to paste them one by one. This is one of the clearest differences between a Coding Agent and a conventional chat window.

## Step 3: Run the Course Check

Run in the terminal:

```bash
python3 checks/check-project.py setup
```

Continue to the next lesson only after you see `PASS`.

## Checkpoint

You should now be able to answer:

- What does the Agent work on? — The files and tools in the entire project.
- Why say “do not modify files” first? — To establish a boundary before entering formal Planning.

## Troubleshooting

- `claude` is not found: install and sign in to Claude Code first.
- The checker reports missing files: do not create replacement files yourself; ask the instructor to redistribute the course directory.

Next: [`01-planning.md`](01-planning.md)
