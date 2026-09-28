# AI Agent Training for the Uzbekistan Government Team

9–12 November, 14:00–17:00 local time each day. Groups of three stay together all week.

Days 1 to 3 each teach one technique and then practise it on that day's pack. Day 4 is the group project and the final presentation.

- Agenda: [uzbekistan-ai-agent-week-en.md](uzbekistan-ai-agent-week-en.md) · [中文](uzbekistan-ai-agent-week.md)
- Teaching modules: [lessons/](lessons/)
- Participant packs: [materials/](materials/)
- Presentation requirements and scoring: [materials/presentation-rubric.md](materials/presentation-rubric.md)
- Run sheet and preparation: [materials/instructor-prep.md](materials/instructor-prep.md) (keep with the instructor)
- Answer checks: [materials/instructor-key.md](materials/instructor-key.md) (keep with the instructor)
- Day 2 role cards: [materials/role-cards.md](materials/role-cards.md) (print and cut; hand out one card per group)

## The week

| Day | Topic | Module | Pack | Done |
| --- | --- | --- | --- | --- |
| Day 1 — Mon 9 Nov | Agent fundamentals and tool-calls | [`01-tool-calls.md`](lessons/01-tool-calls.md) | [`day1-website/`](materials/day1-website/) | `index.html` |
| Day 2 — Tue 10 Nov | Retrieval, knowledge base, and memory | [`02-rag-memory.md`](lessons/02-rag-memory.md) | [`day2-briefing/`](materials/day2-briefing/) | `briefing.md` and a six-slide `slides.md` |
| Day 3 — Wed 11 Nov | Planning, workflow, and multiple agents | [`03-planning-workflow-multiagent.md`](lessons/03-planning-workflow-multiagent.md) | [`day3-budget/`](materials/day3-budget/) | `dashboard.html` or `dashboard.xlsx`, plus a half-page `memo.md` |
| Day 4 — Thu 12 Nov | Group project | [`04-group-project.md`](lessons/04-group-project.md) | one of five topics | three deliverables and a 5–10 minute presentation |

Days 2 and 3: 14:00–15:00 teaching and a live demonstration, 15:00–16:30 group work, 16:30–17:00 debrief.

Day 1 starts twenty-five minutes earlier in the material: [`lessons/00-agent-basics.md`](lessons/00-agent-basics.md) runs 14:00–14:25 on what an agent is, how to read a tool call, and the read-only boundary; teaching runs 14:25–15:10, and the lab starts at 15:10.

Day 4: 14:00–14:20 brief and topic allocation, 14:20–16:00 group work, 16:00–17:00 presentations.

## Day 4 topics

| Topic | Pack | Deliverables |
| --- | --- | --- |
| Benefit eligibility advice | [`day4-benefits/`](materials/day4-benefits/) | `eligibility-guide.md`, `case-assessments.md`, `information-requests.md` |
| Complaint and service-ticket handling | [`day4-complaints/`](materials/day4-complaints/) | `triage.md`, `replies.md`, `escalations.md` |
| Public service navigation | [`day4-interagency/`](materials/day4-interagency/) | `journey.md`, `interagency-sop.md`, `conflicts.md` |
| Public consultation synthesis | [`day4-consultation/`](materials/day4-consultation/) | `synthesis.md`, `decision-note.md`, `response-table.md` |
| Home sewing workshop service | [`day4-service/`](materials/day4-service/) | `public-page.html`, `internal-sop.md`, `letters.md` |

## Rules

1. Each afternoon uses only that day's folder.
2. If a fee, deadline, or legal rule is not in the pack, write “to be confirmed”.
3. Centre No. 3, the meetings, and every figure are invented for the exercise.
4. The process wording follows individual-entrepreneur registration on [my.gov.uz](https://my.gov.uz) and the public “start a business in 15 minutes” arrangement from January 2026: once an application is complete, registration takes no more than 30 minutes. An electronic signature, a bank account, and a cash register are outside that clock.

Every pack contains planted problems — items that must be marked “to be confirmed”, and on Day 4, contradictions between two files in the same folder. Finding them is the exercise.

These files are not a government notice and not legal advice.

## Checking the package

```bash
python3 checks/check-project.py course
```

See [checks/README.md](checks/README.md).
