# Lesson 4: Subagents—Assemble a Virtual Expert Team

**Time: 10–15 minutes**

## Learning Objectives

- Delegate three well-defined analysis tasks in parallel.
- Understand isolated context and least privilege.
- Have the main Agent synthesize findings rather than concatenate answers.

## Step 1: Review the Project Roles

The project configures:

- `market-analyst`: checks data, calculations, and evidence gaps.
- `cfo-challenger`: challenges the recommendation through cash flow and downside scenarios.
- `executive-designer`: designs an information structure an executive can understand in five minutes.

All three roles are read-only and do not modify the website directly.

## Step 2: Delegate in Parallel

Enter in CodeBuddy Code:

```text
Please execute @prompts/delegate-analysis.txt. Run the three named Subagents as parallel background tasks, wait for all three results, and then synthesize them.
```

Check that CodeBuddy starts all three background tasks and later reports all three results. You can use `/agents` to inspect the configured roles. Do not let three Agents edit the same files simultaneously. They produce analysis; the main Agent synthesizes and implements it.

## Step 3: Request Synthesis

If the main Agent only lists the three reports, add:

```text
Do not simply concatenate the reports. Identify shared conclusions, conflicting views, the final decisions you adopted, and the recommendations you rejected with reasons.
```

## Why Use Subagents?

- Isolated contexts keep large amounts of search detail out of the main conversation.
- Specialist roles can have different system prompts and tool permissions.
- Independent tasks can run in parallel.
- A dissenting role can actively find weaknesses in the leading conclusion.

## When Not to Use Them

Starting multiple Subagents only adds latency and cost when changing one title, explaining one function, or running a simple query.

## Checkpoint

Confirm that the synthesized report contains at least:

- One point of consensus across all three roles.
- One conflict.
- One data gap.
- One reason to oppose the recommended market.
- One action that can be validated within 30 days.

Next: [`05-build.md`](05-build.md)
