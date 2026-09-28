# Course checker

Uses only the Python standard library. It verifies that the course package is structurally intact. It cannot tell you whether the teaching content is any good.

## Check the whole package

```bash
python3 checks/check-project.py course
```

Runs the four checks below. Run this after editing any course file, and before handing packs out.

### `setup`

Every agenda, module, prompt, skill, agent, and instructor file is present and non-empty. That includes the two files the instructor needs before the room fills up: `materials/instructor-prep.md` and `materials/role-cards.md`.

### `packs`

Each of the eight pack folders has its declared files. Catches a pack handed out with a source file missing — which would make the exercise unsolvable and look like a participant error.

### `links`

Every relative Markdown link in the READMEs, both agendas, the instructor run sheet, and the lesson modules resolves on disk. A renamed lesson leaves dangling links in four other files; this is what finds them.

### `stale`

No file still references the retired market-dashboard course — `WorkBuddy`, `Southeast Asia`, `executive-dashboard`, the three old subagent names, or `inputs/`.

## Check a team's Day 4 deliverables

```bash
python3 checks/check-project.py project consultation ~/teams/team-3
```

Topics: `benefits`, `complaints`, `consultation`, `interagency`, `service`. The folder argument defaults to the current directory.

This confirms the three deliverables exist and are non-empty. It says nothing about whether they are correct.

## What the checker cannot do

It does not read content. It will pass a page that invents a state fee, a briefing that cites no sources, and a consultation synthesis that counts the duplicate rows. Those are caught by a person, using `materials/instructor-key.md`, and by the participants themselves running `prompts/review.txt`.

Specifically, still check by hand:

- Every item in each pack's `do-not-invent.md` reads "to be confirmed" in the deliverable.
- Figures trace to the pack, with the file named.
- A team's own deliverables agree with each other on day counts and document lists.
- The Day 4 contradiction was found and stated, not silently resolved.
