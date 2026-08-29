# Course Checker

The checker uses only the Python standard library. It verifies that the course structure and key website hooks are present.

## Check Course Setup

```bash
python3 checks/check-project.py setup
```

Validates the input materials, eight lessons, `CLAUDE.md`, the Skill, and three read-only Subagents.

## Check the Student Site

```bash
python3 checks/check-project.py student
```

Run this after Lesson 5 has created `site/` in the project root. It checks key sections and calculation/rendering hooks; it does not prove that the visual design and business logic are fully correct.

## Check the Instructor Reference Site

```bash
python3 checks/check-project.py reference
```

Confirms that the reference site includes scenarios, weights, rankings, risks, and evidence structure, and that it has no external network dependencies.

## Run All Checks

```bash
python3 checks/check-project.py all
```

Before the student creates `site/`, `all` is expected to fail during the student stage. This is a normal learning checkpoint, not a damaged course package.

## Why Manual Validation Is Still Necessary

Structural checks cannot find every problem. You must also:

- Switch through every scenario in the browser.
- Adjust sliders and confirm the total remains 100%.
- Confirm that the recommendation explanation updates in sync.
- Test at mobile width and with keyboard controls.
- Use `/code-review` to check consistency between calculations and evidence.
