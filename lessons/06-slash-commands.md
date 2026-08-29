# Lesson 6: Slash Commands—Control, Review, and Recover

**Time: 10–15 minutes**

## Learning Objectives

- Inspect actual changes instead of relying on the Agent's self-report.
- Use different review methods to find problems.
- Know how to return to a safe state.

## 1. `/diff`: Inspect Actual Changes

Enter:

```text
/diff
```

Look for which files the Agent changed, whether it touched `inputs/`, and whether it added an external CDN.

> If the course directory has not been initialized as a Git repository, the `/diff` experience may be limited. Ask the Agent to list the new files in `site/` and use the checker instead. Git is recommended for real projects.

## 2. `/code-review`: Independently Find Correctness Problems

Enter:

```text
/code-review high site/
```

Or use the course prompt:

```text
Please execute @prompts/review.txt
```

Review priorities:

- Whether any scoring direction is reversed.
- Whether weight normalization is stable.
- Whether data sources match the displayed values.
- Whether keyboard controls and narrow-screen layouts work.

## 3. `/simplify`: Clean Up the Implementation

`/code-review` primarily finds correctness defects; `/simplify` focuses on reuse, simplicity, and maintainability. They are not the same task.

```text
/simplify site/
```

## 4. `/rewind`: Restore a Checkpoint

Before making an obvious visual experiment, enter:

```text
Make the entire website fluorescent green and hide the sources section.
```

Do not keep the result. Use:

```text
/rewind
```

Choose whether to restore code, conversation, or both. Instructors can describe the options without performing the destructive change.

## 5. `/memory` and `/skills`

These are not “magic commands” that produce a website. They are control entry points for inspecting the Agent's persistent context and reusable capabilities.

## Checkpoint

Explain the difference among these in one sentence:

- `/code-review`
- `/simplify`
- `/rewind`

Next: [`07-reflect.md`](07-reflect.md)
