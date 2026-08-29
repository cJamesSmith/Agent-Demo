#!/usr/bin/env python3
"""Structural checks for the Claude Code learning project."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SETUP_FILES = [
    "README.md",
    "CLAUDE.md",
    "COURSE-GUIDE.md",
    "inputs/market-data.csv",
    "inputs/customer-interviews.md",
    "inputs/competitor-analysis.md",
    "inputs/risk-memo.md",
    "inputs/data-dictionary.md",
    ".claude/skills/executive-dashboard/SKILL.md",
    ".claude/skills/executive-dashboard/references/scoring.md",
    ".claude/skills/executive-dashboard/templates/page-outline.md",
    ".claude/agents/market-analyst.md",
    ".claude/agents/cfo-challenger.md",
    ".claude/agents/executive-designer.md",
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
            fail_line(f"缺少或为空：{relative_path}")
            failures.append(relative_path)
    return failures


def check_markers(site_directory: Path, markers: dict[str, list[str]]) -> list[str]:
    failures = []
    for filename, expected_markers in markers.items():
        path = site_directory / filename
        if not path.is_file():
            fail_line(f"缺少：{path.relative_to(ROOT)}")
            failures.append(str(path))
            continue

        content = path.read_text(encoding="utf-8")
        missing = [marker for marker in expected_markers if marker not in content]
        if missing:
            fail_line(f"{path.relative_to(ROOT)} 缺少标识：{', '.join(missing)}")
            failures.extend(f"{path}:{marker}" for marker in missing)
        else:
            pass_line(f"{path.relative_to(ROOT)} 关键结构")
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
            fail_line(f"{path.relative_to(ROOT)} 含外部依赖：{', '.join(forbidden)}")
            failures.extend(f"{path}:{token}" for token in forbidden)
        else:
            pass_line(f"{path.relative_to(ROOT)} 无外部网络依赖")
    return failures


def run_setup() -> list[str]:
    print("\n[课程与 Claude Code 配置]")
    failures = check_files(SETUP_FILES + LESSON_FILES)

    claude_md = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    if "虚构" in claude_md and "事实" in claude_md and "假设" in claude_md:
        pass_line("CLAUDE.md 包含真实性与证据规则")
    else:
        fail_line("CLAUDE.md 缺少真实性或证据规则")
        failures.append("CLAUDE.md:rules")

    for agent_name in ("market-analyst", "cfo-challenger", "executive-designer"):
        content = (ROOT / f".claude/agents/{agent_name}.md").read_text(encoding="utf-8")
        if "tools: Read, Grep, Glob" in content:
            pass_line(f"{agent_name} 使用只读工具")
        else:
            fail_line(f"{agent_name} 未保持只读工具范围")
            failures.append(f"agent:{agent_name}:tools")
    return failures


def run_student() -> list[str]:
    print("\n[学生网页]")
    site = ROOT / "site"
    if not site.exists():
        fail_line("尚未创建 site/。请完成第 5 课后再运行 student 检查。")
        return ["site"]
    return check_markers(site, SITE_MARKERS)


def run_reference() -> list[str]:
    print("\n[参考网页]")
    failures = check_markers(ROOT / "reference/site", REFERENCE_MARKERS)
    failures.extend(check_no_external_reference_assets())
    return failures


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    valid_modes = {"setup", "student", "reference", "all"}
    if mode not in valid_modes:
        print("用法：python3 checks/check-project.py [setup|student|reference|all]")
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
        print(f"RESULT  {len(failures)} 项未通过")
        return 1
    print("RESULT  全部检查通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
