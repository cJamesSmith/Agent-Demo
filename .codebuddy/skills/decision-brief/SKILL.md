---
name: decision-brief
description: Turn meeting minutes, figures, public comments, and an existing deck into a short brief for a decision-maker. Use for pre-meeting briefs, claim checking, correcting an existing deck, and separating what can be decided now from what must wait.
argument-hint: "[the question the meeting must answer]"
allowed-tools: Read, Grep, Glob, Edit, Write, Bash
---

# Decision Brief Method

Produce a brief a decision-maker can act on in ten minutes and defend in a meeting. Not a summary of the materials.

## Core Process

1. **State the question.** One sentence, the question the meeting must answer. If the materials answer a different question, say so at the top.
2. **Build the claim table.** List every substantive claim from the existing deck or draft. For each: the source file that supports it, or the file that contradicts it, or "nothing in the pack supports this". See [references/claim-checking.md](references/claim-checking.md).
3. **Find where the time or the problem actually goes.** Work from the figures and the first-hand comments, not from the summary someone else wrote. A summary that was not present at the event is weaker evidence than a table that was.
4. **Handle disagreement explicitly.** When two source files give different causes or different figures, present both with their filenames and their dates, and say which is better evidence and why. Never resolve a contradiction silently.
5. **Split the decisions.** What can be decided at this meeting with the evidence in hand; what must wait, and specifically for what. A decision that needs data arriving in six weeks is not a decision for tomorrow.
6. **Name what must be withdrawn.** Claims already in public that the evidence does not support. These are urgent and belong near the front.
7. **Cite everything.** Source filename in parentheses after each conclusion. A conclusion without one is not finished.

## Structure

Use **Question → Where the problem is → Evidence → Claims to withdraw → Decide now → Must wait**. See [templates/briefing-outline.md](templates/briefing-outline.md).

Facts must be traceable to a file. Inferences must state what they are inferred from. Anything not in the pack is "to be confirmed", never an estimate.

## Definition of Done

The decision-maker knows what to decide within one minute of opening the brief. Every figure traces to a named file. Every unsupported public claim is listed. The distinction between deciding now and waiting is explicit, and the reason for waiting is a specific missing input, not caution.
