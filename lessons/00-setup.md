# Lesson 0: Understand the Task and Environment

**Time: 5–8 minutes**

## Learning Objectives

- Understand that CodeBuddy Code can read and work with an entire project, not just answer questions.
- Confirm that the course files are complete.
- Build the habit of defining the outcome and constraints before prescribing code.

## Step 1: Enter the Project

Download or install CodeBuddy Code using the official [installation guide](https://www.codebuddy.ai/docs/zh/cli/installation). The official [quick-start guide](https://www.codebuddy.ai/docs/zh/cli/quickstart) covers sign-in and first launch. CodeBuddy Code supports macOS, Linux, and Windows. If you install it through npm, use Node.js 18.20 or later.

Run in the terminal:

```bash
cd /path/to/Agent-Demo
codebuddy
```

On first launch, select the appropriate CodeBuddy site and finish browser sign-in. If you already have a CodeBuddy Code session open in this directory, you do not need to restart it. This course is already configured, so do not run `/init`; it could replace the prepared project Memory.

## Step 2: Ask the Agent to Introduce the Project

Enter in CodeBuddy Code:

```text
Do not modify any files yet. Explore this project and tell me in no more than eight lines:
1. What is my business task?
2. What input materials are available?
3. Which CodeBuddy Code capabilities are configured in the project?
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

- `codebuddy` is not found: confirm Node.js 18.20 or later, install CodeBuddy Code with `npm install -g @tencent-ai/codebuddy-code`, then run `codebuddy` and sign in.
- The checker reports missing files: do not create replacement files yourself; ask the instructor to redistribute the course directory.

Next: [`01-planning.md`](01-planning.md)
