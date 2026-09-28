#!/usr/bin/env python3
"""Structural checks for the Uzbekistan AI agent week course package."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SETUP_FILES = [
    "README.md",
    "CODEBUDDY.md",
    "uzbekistan-ai-agent-week-en.md",
    "uzbekistan-ai-agent-week.md",
    "lessons/00-agent-basics.md",
    "lessons/01-tool-calls.md",
    "lessons/02-rag-memory.md",
    "lessons/03-planning-workflow-multiagent.md",
    "lessons/04-group-project.md",
    "materials/README.md",
    "materials/instructor-key.md",
    "materials/instructor-prep.md",
    "materials/presentation-rubric.md",
    "materials/role-cards.md",
    "prompts/day1-weak-prompt.txt",
    "prompts/day1-strong-prompt.txt",
    "prompts/plan.txt",
    "prompts/inspect-memory.txt",
    "prompts/delegate-analysis.txt",
    "prompts/build-dashboard.txt",
    "prompts/priority-change.txt",
    "prompts/review.txt",
    ".codebuddy/skills/decision-brief/SKILL.md",
    ".codebuddy/skills/decision-brief/references/claim-checking.md",
    ".codebuddy/skills/decision-brief/templates/briefing-outline.md",
    ".codebuddy/skills/pilot-dashboard/SKILL.md",
    ".codebuddy/skills/pilot-dashboard/references/comparison-rules.md",
    ".codebuddy/agents/source-checker.md",
    ".codebuddy/agents/resident-advocate.md",
    ".codebuddy/agents/decision-challenger.md",
]

PACKS = {
    "day1-website": [
        "README.md",
        "centre-facts.md",
        "do-not-invent.md",
        "resident-questions.txt",
    ],
    "day2-briefing": [
        "README.md",
        "draft-decision.md",
        "minutes-03-nov.md",
        "minutes-05-nov.md",
        "october-snapshot.csv",
        "october-snapshot.md",
        "old-deck.md",
        "public-comments.md",
    ],
    "day3-budget": [
        "README.md",
        "budget-note.md",
        "priority-memo.md",
        "regional-kpis.csv",
        "regional-kpis.xlsx",
    ],
    "day4-benefits": [
        "README.md",
        "applicant-cases.md",
        "do-not-invent.md",
        "eligibility-rules.md",
        "intake-notes.md",
    ],
    "day4-service": [
        "README.md",
        "agreed-sentences.md",
        "desk-rota.md",
        "refusal-rules.md",
        "service-facts.md",
        "three-cases.md",
    ],
    "day4-complaints": [
        "README.md",
        "complaints.md",
        "desk-notes.md",
        "do-not-invent.md",
        "routing-rules.md",
    ],
    "day4-consultation": [
        "README.md",
        "do-not-invent.md",
        "draft-articles.md",
        "responses.csv",
        "responses.md",
        "weighting-rules.md",
    ],
    "day4-interagency": [
        "README.md",
        "agency-a-centre.md",
        "agency-b-tax.md",
        "agency-c-sanitary.md",
        "do-not-invent.md",
        "resident-diaries.md",
    ],
}

# Day 4 topic -> the deliverables a team must produce.
PROJECT_DELIVERABLES = {
    "benefits": [
        "eligibility-guide.md",
        "case-assessments.md",
        "information-requests.md",
    ],
    "service": ["public-page.html", "internal-sop.md", "letters.md"],
    "complaints": ["triage.md", "replies.md", "escalations.md"],
    "consultation": ["synthesis.md", "decision-note.md", "response-table.md"],
    "interagency": ["journey.md", "interagency-sop.md", "conflicts.md"],
}

# Files whose relative markdown links must resolve on disk.
LINK_SOURCES = [
    "README.md",
    "uzbekistan-ai-agent-week-en.md",
    "uzbekistan-ai-agent-week.md",
    "materials/README.md",
    "materials/instructor-prep.md",
    "checks/README.md",
]

LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

# Names from the retired market-dashboard course. Any survivor is a stale reference.
STALE_TOKENS = [
    "WorkBuddy",
    "Southeast Asia",
    "executive-dashboard",
    "market-analyst",
    "cfo-challenger",
    "executive-designer",
    "inputs/",
]

STALE_SCAN_SUFFIXES = {".md", ".txt", ".py"}
STALE_SKIP_DIRS = {".git", "node_modules"}

# These two describe the stale tokens, so they are allowed to contain them.
STALE_SKIP_FILES = {Path("checks/check-project.py"), Path("checks/README.md")}


def _report(label: str, problems: list[str]) -> bool:
    if problems:
        print(f"FAIL  {label}")
        for problem in problems:
            print(f"      {problem}")
        return False
    print(f"OK    {label}")
    return True


def check_setup() -> bool:
    missing = [name for name in SETUP_FILES if not (ROOT / name).is_file()]
    empty = [
        name
        for name in SETUP_FILES
        if (ROOT / name).is_file() and (ROOT / name).stat().st_size == 0
    ]
    return _report(
        "setup: course files present",
        [f"missing: {name}" for name in missing] + [f"empty: {name}" for name in empty],
    )


def check_packs() -> bool:
    problems: list[str] = []
    for pack, files in PACKS.items():
        folder = ROOT / "materials" / pack
        if not folder.is_dir():
            problems.append(f"missing pack folder: materials/{pack}")
            continue
        for name in files:
            path = folder / name
            if not path.is_file():
                problems.append(f"missing: materials/{pack}/{name}")
            elif path.stat().st_size == 0:
                problems.append(f"empty: materials/{pack}/{name}")
    return _report("packs: every pack has its declared files", problems)


def check_links() -> bool:
    problems: list[str] = []
    sources = list(LINK_SOURCES) + sorted(
        str(path.relative_to(ROOT)) for path in (ROOT / "lessons").glob("*.md")
    )
    for source in sources:
        path = ROOT / source
        if not path.is_file():
            problems.append(f"missing link source: {source}")
            continue
        for target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).exists():
                problems.append(f"{source} -> {target} does not exist")
    return _report("links: relative markdown links resolve", problems)


def check_stale() -> bool:
    problems: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in STALE_SCAN_SUFFIXES:
            continue
        relative = path.relative_to(ROOT)
        if STALE_SKIP_DIRS.intersection(relative.parts):
            continue
        if relative in STALE_SKIP_FILES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for token in STALE_TOKENS:
            if token in text:
                problems.append(f"{relative}: stale reference to {token!r}")
    return _report("stale: no references to the retired course", problems)


def check_project(topic: str, folder: Path) -> bool:
    if topic not in PROJECT_DELIVERABLES:
        known = ", ".join(sorted(PROJECT_DELIVERABLES))
        print(f"FAIL  project: unknown topic {topic!r}. Known topics: {known}")
        return False
    problems = []
    for name in PROJECT_DELIVERABLES[topic]:
        path = folder / name
        if not path.is_file():
            problems.append(f"missing: {path}")
        elif path.stat().st_size == 0:
            problems.append(f"empty: {path}")
    return _report(f"project ({topic}): deliverables present in {folder}", problems)


def usage() -> None:
    print(__doc__.strip())
    print()
    print("Usage:")
    print("  python3 checks/check-project.py setup")
    print("  python3 checks/check-project.py packs")
    print("  python3 checks/check-project.py links")
    print("  python3 checks/check-project.py stale")
    print("  python3 checks/check-project.py course        # the four checks above")
    print("  python3 checks/check-project.py project <topic> [folder]")
    print()
    print("Topics: " + ", ".join(sorted(PROJECT_DELIVERABLES)))


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        usage()
        return 2

    command = argv[1]

    if command == "setup":
        return 0 if check_setup() else 1
    if command == "packs":
        return 0 if check_packs() else 1
    if command == "links":
        return 0 if check_links() else 1
    if command == "stale":
        return 0 if check_stale() else 1
    if command == "course":
        results = [check_setup(), check_packs(), check_links(), check_stale()]
        return 0 if all(results) else 1
    if command == "project":
        if len(argv) < 3:
            usage()
            return 2
        folder = Path(argv[3]).resolve() if len(argv) > 3 else Path.cwd()
        return 0 if check_project(argv[2], folder) else 1

    usage()
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
