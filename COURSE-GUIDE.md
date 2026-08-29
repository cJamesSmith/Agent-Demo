# Instructor Guide

## Learning Objective

This is not an HTML course. Students learn how to govern and use a Coding Agent by producing a visible deliverable: define an outcome, load organizational context, reuse a method, delegate to specialists, approve a plan, and verify the result.

## Recommended Schedule

### 25–35 Minute Executive Demo

| Time | Action | Teaching Point |
|---:|---|---|
| 0–3 | Show `inputs/` | The Agent works with a project and its materials, not just a chat |
| 3–6 | `/memory` | Organizational rules that remain in effect |
| 6–10 | Enter Plan Mode; show and revise the plan | People approve scope and risk before execution |
| 10–14 | `/executive-dashboard` | Methodology loads on demand and can be reused across a team |
| 14–18 | Run three Subagents in parallel | A virtual cross-functional team with least privilege |
| 18–25 | Use the reference implementation or build live | Turn source material into a working decision tool |
| 25–29 | Switch scenarios and introduce an executive change | Software can evolve through natural-language instructions |
| 29–33 | `git diff`, `/code-review`, `/rewind` | Inspect, review, and recover instead of only generating |
| 33–35 | Summarize the six elements | Prompt / Memory / Skill / Subagent / Planning / Command |

For the accelerated version, generate `site/` in advance and make only one small change live. A complete live build depends on network and model latency.

### 60–90 Minute Hands-On Workshop

Have students complete `lessons/00` through `07` independently. Pairs work well: one person acts as the business owner and the other as the risk approver.

## Teaching Analogies

- Planning: **“Ask the digital team to submit a construction plan before authorizing the work.”**
- Memory: **“This is the employee handbook read at the start of every workday.”**
- Skill: **“Turn an excellent employee's method into a reusable organizational standard.”**
- Subagents: **“The main Agent is the project manager; specialist Agents are a temporary functional team.”**
- Slash Commands: **“The control panel for inspecting, reviewing, recovering, and switching work modes.”**

## Suggested Discussion Questions

1. If the recommended market changes, did the data change or did the value priorities change?
2. Should the CFO challenger have permission to write files? Why or why not?
3. Why should the scoring formula exist somewhere other than the chat transcript?
4. What is the difference between the Agent saying “done” and the website actually working?
5. Which enterprise knowledge belongs in Memory, and which belongs in a Skill?

## Demo Contingencies

### The Skill Does Not Appear

1. Confirm the path is `.codebuddy/skills/executive-dashboard/SKILL.md`.
2. Restart the CodeBuddy Code session so it reloads project Skills.
3. If it still fails, ask the Agent to read the file directly, continue the course, and investigate the version afterward.

### A Subagent Does Not Start Automatically

Use `prompts/delegate-analysis.txt` to name each role explicitly. If necessary, directly request: “Use the market-analyst subagent.”

### Website Generation Is Too Slow

Switch to `reference/site/`:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/reference/site/` and explain that this is a pre-generated fallback built from the same plan.

### The Website Does Not Open

- Confirm that the command is running from the project root.
- Check whether the port is occupied; if so, use `python3 -m http.server 8765`.
- Do not open the site through `file://`; some browser behavior differs from a local server.

### Git Diff Is Unavailable

The distributed course directory might not be initialized as a Git repository. Compare the deliverable with the scaffold using `git diff --no-index -- starter/site/ site/`, then run `python3 checks/check-project.py student`. Exit code `1` from this comparison only means differences were found.

## Safety and Authenticity

- All business materials are fictional.
- Do not encourage students to upload real financial, customer, or employee data.
- External publication, deployment, messaging, and data deletion are outside this course's scope.
- The reference implementation is an instructional example, not market or investment advice.

## Success Criteria

Students do not need to write JavaScript by hand, but they must be able to:

- Define a testable outcome and constraints.
- Review an Agent plan instead of approving it blindly.
- Explain the distinct responsibility of each of the five capabilities.
- Judge output quality through execution, review, and evidence traceability.
- Apply the same method to a real business scenario.
