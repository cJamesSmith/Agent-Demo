# 72-Hour Global Expansion Decision Room

This CodeBuddy Code learning project uses entirely fictional data. Its goal is to transform the business materials in `inputs/` into an interactive executive decision dashboard.

## Audience and Communication

- Use English by default.
- The audience is non-technical executives; lead with conclusions and reveal details progressively.
- Avoid technical jargon, long blocks of text, and unexplained scores.
- Structure important recommendations as “Recommendation → Evidence → Risks → Next Steps.”

## Decision Integrity

- Clearly label facts, inferences, and assumptions; never present one as another.
- Key figures must be traceable to sources in `inputs/`.
- Do not hide data gaps or present limited samples as certain facts.
- Every recommendation must include the strongest counterargument.
- Scores are scenario simulations, not market forecasts or investment advice.

## Engineering Boundaries

- Place the student deliverable in the root-level `site/` directory.
- Do not modify `inputs/`, `reference/`, or course instructions merely to make checks pass.
- Use plain HTML, CSS, and JavaScript with no external CDN, framework, backend, or network requests.
- The page must support keyboard navigation, narrow screens, and `prefers-reduced-motion`.
- Use red only for risks or warnings, and never rely on color alone to communicate meaning.

## Workflow

- Plan complex implementations and wait for approval; make small, unambiguous changes directly.
- Analytical Subagents are read-only by default; the main Agent synthesizes their findings and edits files.
- Accurately report which checks were run when work is complete; never claim an unrun check passed.

## Common Checks

```bash
python3 checks/check-project.py setup
python3 checks/check-project.py student
python3 checks/check-project.py reference
```
