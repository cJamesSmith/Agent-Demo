#!/usr/bin/env python3
"""Structural checks for the CodeBuddy Code learning project."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SETUP_FILES = [
    "README.md",
    "CODEBUDDY.md",
    "COURSE-GUIDE.md",
    "inputs/market-data.csv",
    "inputs/customer-interviews.md",
    "inputs/competitor-analysis.md",
    "inputs/risk-memo.md",
    "inputs/data-dictionary.md",
    ".codebuddy/skills/executive-dashboard/SKILL.md",
    ".codebuddy/skills/executive-dashboard/references/scoring.md",
    ".codebuddy/skills/executive-dashboard/templates/page-outline.md",
    ".codebuddy/agents/market-analyst.md",
    ".codebuddy/agents/cfo-challenger.md",
    ".codebuddy/agents/executive-designer.md",
]

LESSON_FILES = [f"lessons/{index:02d}-{name}.md" for index, name in enumerate([
    "setup",
    "planning",
    "memory",
    "skills",
    "subagents",
    "build",
    "slash-commands",
    "reflect",
])]

UNSUPPORTED_LESSON_TOKENS = [
    "/diff",
    "/run",
    "/reload-skills",
    "/code-review high",
]

SITE_MARKERS = {
    "index.html": [
        "executive-summary",
        "market-comparison",
        "scenario-simulator",
        "risk-heatmap",
        "action-plan",
        "evidence",
    ],
    "styles.css": ["prefers-reduced-motion"],
    "app.js": ["normalize", "calculate", "render"],
}

REFERENCE_MARKERS = {
    "index.html": [
        "recommended-market",
        "market-cards",
        "weights-grid",
        "risk-table",
        "evidence-grid",
        "aria-pressed",
    ],
    "styles.css": ["@media", "prefers-reduced-motion", "overflow-x"],
    "app.js": [
        "rebalanceWeights",
        "calculateRanking",
        "renderDashboard",
        "cashflow",
    ],
}


def pass_line(message: str) -> None:
    print(f"PASS  {message}")


def fail_line(message: str) -> None:
    print(f"FAIL  {message}")


def check_files(relative_paths: list[str]) -> list[str]:
    failures = []
    for relative_path in relative_paths:
        path = ROOT / relative_path
        if path.is_file() and path.stat().st_size > 0:
            pass_line(relative_path)
        else:
            fail_line(f"Missing or empty: {relative_path}")
            failures.append(relative_path)
    return failures


def check_markers(site_directory: Path, markers: dict[str, list[str]]) -> list[str]:
    failures = []
    for filename, expected_markers in markers.items():
        path = site_directory / filename
        if not path.is_file():
            fail_line(f"Missing: {path.relative_to(ROOT)}")
            failures.append(str(path))
            continue

        content = path.read_text(encoding="utf-8")
        missing = [marker for marker in expected_markers if marker not in content]
        if missing:
            fail_line(f"{path.relative_to(ROOT)} missing markers: {', '.join(missing)}")
            failures.extend(f"{path}:{marker}" for marker in missing)
        else:
            pass_line(f"{path.relative_to(ROOT)} required structure")
    return failures


def check_no_external_reference_assets() -> list[str]:
    failures = []
    site = ROOT / "reference/site"
    for filename in ("index.html", "styles.css", "app.js"):
        path = site / filename
        content = path.read_text(encoding="utf-8")
        forbidden = [
            token for token in ("https://", "http://", "fetch(", "XMLHttpRequest")
            if token in content
        ]
        if forbidden:
            fail_line(f"{path.relative_to(ROOT)} contains external dependencies: {', '.join(forbidden)}")
            failures.extend(f"{path}:{token}" for token in forbidden)
        else:
            pass_line(f"{path.relative_to(ROOT)} has no external network dependencies")
    return failures


def check_codebuddy_lessons() -> list[str]:
    failures = []
    combined = "\n".join(
        (ROOT / relative_path).read_text(encoding="utf-8")
        for relative_path in LESSON_FILES
    )
    found = [token for token in UNSUPPORTED_LESSON_TOKENS if token in combined]
    if found:
        fail_line(f"Lessons contain legacy or unsupported instructions: {', '.join(found)}")
        failures.extend(f"lessons:{token}" for token in found)
    else:
        pass_line("Lessons contain no known legacy or unsupported commands")

    required = [
        "codebuddy",
        "CODEBUDDY.md",
        ".codebuddy/skills/",
        "Shift+Tab",
        "/agents",
        "/code-review site/",
        "/rewind",
    ]
    missing = [token for token in required if token not in combined]
    if missing:
        fail_line(f"Lessons are missing CodeBuddy workflow markers: {', '.join(missing)}")
        failures.extend(f"lessons:{token}" for token in missing)
    else:
        pass_line("Lessons include the required CodeBuddy workflow")
    return failures


def run_setup() -> list[str]:
    print("\n[Course and CodeBuddy Code Configuration]")
    failures = check_files(SETUP_FILES + LESSON_FILES)
    failures.extend(check_codebuddy_lessons())

    codebuddy_md = (ROOT / "CODEBUDDY.md").read_text(encoding="utf-8")
    if "fictional" in codebuddy_md.lower() and "fact" in codebuddy_md.lower() and "assumption" in codebuddy_md.lower():
        pass_line("CODEBUDDY.md includes truthfulness and evidence rules")
    else:
        fail_line("CODEBUDDY.md is missing truthfulness or evidence rules")
        failures.append("CODEBUDDY.md:rules")

    for agent_name in ("market-analyst", "cfo-challenger", "executive-designer"):
        content = (ROOT / f".codebuddy/agents/{agent_name}.md").read_text(encoding="utf-8")
        if "tools: Read, Grep, Glob" in content:
            pass_line(f"{agent_name} uses read-only tools")
        else:
            fail_line(f"{agent_name} does not retain a read-only tool scope")
            failures.append(f"agent:{agent_name}:tools")
    return failures


def run_student() -> list[str]:
    print("\n[Student Site]")
    site = ROOT / "site"
    if not site.exists():
        fail_line("site/ has not been created. Complete Lesson 5 before running the student check.")
        return ["site"]
    return check_markers(site, SITE_MARKERS)


def run_reference() -> list[str]:
    print("\n[Reference Site]")
    failures = check_markers(ROOT / "reference/site", REFERENCE_MARKERS)
    failures.extend(check_no_external_reference_assets())
    return failures


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    valid_modes = {"setup", "student", "reference", "all"}
    if mode not in valid_modes:
        print("Usage: python3 checks/check-project.py [setup|student|reference|all]")
        return 2

    failures: list[str] = []
    if mode in {"setup", "all"}:
        failures.extend(run_setup())
    if mode in {"student", "all"}:
        failures.extend(run_student())
    if mode in {"reference", "all"}:
        failures.extend(run_reference())

    print()
    if failures:
        print(f"RESULT  {len(failures)} check(s) failed")
        return 1
    print("RESULT  All checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
