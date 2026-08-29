# Lesson 6: Slash Commands—Control, Review, and Recover

**Time: 10–15 minutes**

## Learning Objectives

- Inspect actual changes instead of relying on the Agent's self-report.
- Use different review methods to find problems.
- Know how to return to a safe state.

## 1. Inspect Actual Changes

Run in the terminal:

```bash
git diff --no-index -- starter/site/ site/
```

This compares the generated site with the starter scaffold even when `site/` is not tracked by Git. Exit code `1` is normal here: it means differences were found. Inspect whether the Agent added an external CDN. If the course is a Git repository, also run `git diff -- inputs/ reference/` and confirm it is empty.

> `git diff --no-index` works without a Git repository. Git is still recommended for tracking changes outside `site/` and for permanent history.

## 2. `/code-review`: Independently Find Correctness Problems

Enter:

```text
/code-review site/
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
Temporarily change the website accent color to purple and add “Rewind Demo” to the page title.
```

Do not keep the result. Use:

```text
/rewind
```

Choose whether to restore code, conversation, or both. Instructors can describe the options without performing the destructive change.

> CodeBuddy checkpoints track edits made with its file-editing tools. Changes made by shell commands or outside CodeBuddy are not guaranteed to be recoverable, so `/rewind` does not replace Git.

## 5. `/memory` and `/skills`

These are not “magic commands” that produce a website. They are control entry points for inspecting the Agent's persistent context and reusable capabilities.

## Checkpoint

Explain the difference among these in one sentence:

- `/code-review`
- `/simplify`
- `/rewind`

Next: [`07-reflect.md`](07-reflect.md)
