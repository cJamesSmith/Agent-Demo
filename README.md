# 72-Hour Global Expansion Decision Room

> A hands-on course for learning the core CodeBuddy Code workflow by building a real web page.

## Your Role

You are not a programmer. You are the company's head of international business. The CEO has asked the team to answer three questions within 72 hours:

1. Which market should we enter first: Vietnam, Indonesia, or Thailand?
2. What evidence supports the recommendation?
3. Does the conclusion still hold when strategic priorities change?

You will use CodeBuddy Code to turn the fictional business materials in `inputs/` into an interactive executive decision dashboard.

## What You Will Learn

| Capability | Role in This Project | Enterprise Analogy |
|---|---|---|
| Planning | Review the materials and submit an implementation plan first | Project initiation and design review |
| Memory | Continuously follow audience, compliance, and communication rules | Employee handbook |
| Skills | Reuse a method for building executive decision dashboards | Standard operating procedure |
| Subagents | Bring in market, finance, and design perspectives in parallel | Cross-functional project team |
| Slash Commands | Control, inspect, and recover Agent work | Management console |

## Final Deliverable

You will produce a `site/` directory containing:

- A CEO summary and recommended market
- A comparison of key metrics across three countries
- Growth-first, profit-first, and risk-first strategic scenarios
- Adjustable weight sliders
- Rankings and recommendation explanations that update automatically
- A risk heatmap and 90-day action plan
- Traceable sources, assumptions, and data gaps

## Project Map

```text
inputs/       Fictional business materials for the Agent to read
lessons/      Lessons for students to complete in order
prompts/      Prompts ready to copy into CodeBuddy Code
.codebuddy/   Skills and Subagents beyond Memory
starter/      Incomplete website scaffold
checks/       Checkpoint validation tools
reference/    Instructor fallback implementation (do not open yet)
```

## Learning Path

Open these files in order:

1. [`lessons/00-setup.md`](lessons/00-setup.md) — Understand the project and prepare your environment
2. [`lessons/01-planning.md`](lessons/01-planning.md) — Plan before changing files
3. [`lessons/02-memory.md`](lessons/02-memory.md) — Learn the project's persistent rules
4. [`lessons/03-skills.md`](lessons/03-skills.md) — Invoke an organizational methodology
5. [`lessons/04-subagents.md`](lessons/04-subagents.md) — Assemble a virtual expert team
6. [`lessons/05-build.md`](lessons/05-build.md) — Build and run the website
7. [`lessons/06-slash-commands.md`](lessons/06-slash-commands.md) — Review, compare, and recover
8. [`lessons/07-reflect.md`](lessons/07-reflect.md) — Reflect and apply the method to real work

A standard class takes about 60–90 minutes. Instructors can use the accelerated path in `COURSE-GUIDE.md` to reduce it to 25–35 minutes.

## Get CodeBuddy Code

Download or install CodeBuddy Code from the official [installation guide](https://www.codebuddy.ai/docs/zh/ide/Getting-Started/Installation). The [quick-start guide](https://www.codebuddy.ai/docs/zh/cli/quickstart) covers sign-in and first launch.

## Distinguish Two Types of Input

The course uses these two labels:

**Enter in CodeBuddy Code:**

```text
Please read the inputs directory first...
```

**Run in the terminal:**

```bash
python3 checks/check-project.py setup
```

If you are already in the CodeBuddy Code interactive interface and need to run a terminal command yourself, enter:

```text
! python3 checks/check-project.py setup
```

## Three Classroom Rules

1. Do not look at `reference/site/` first. It is a fallback, not the starting point for your answer.
2. Do not let the Agent modify the website before you approve the plan.
3. Do not rely only on what the Agent says. Verify the result in the browser and with checkers and review commands.

## Data Disclaimer

All companies, people, interviews, market figures, and conclusions in this project are fictional and created solely for instruction. They do not represent real market research and must not be used for actual investment or business decisions.
