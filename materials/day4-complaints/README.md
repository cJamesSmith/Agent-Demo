# Day 4 task — complaint and service-ticket handling

Training exercise. Use only the files in this folder.

You are the complaints unit of the Agency for Public Services. Eighteen complaints arrived through the portal, the centres, and the hotline during the first week of November. Nobody has sorted them. The unit head wants the backlog triaged and the first replies out today.

Produce:

1. `triage.md` — every complaint in `complaints.md`, with the desk or unit that owns it, the category, the deadline in working days, and whether it must be escalated. Group by owner so each desk can be handed its own list.
2. `replies.md` — three drafted replies: one where the resident is right and the fix is ours, one where more information is needed from the resident, and one where the complaint cannot be resolved at this service. Choose which three and say why you chose them.
3. `escalations.md` — the complaints that must go to a supervisor or to another agency, with the trigger from `routing-rules.md` that requires it and what the escalation must include.

Answer in `triage.md`:

1. Which complaints are about the same underlying problem? Group them and say what the problem is.
2. Which complaints cannot be routed from the complaint text alone, and what is missing?
3. Which single fix would remove the largest number of these complaints?

Rules:

- Every deadline, fee, and document must come from this folder. Otherwise write "to be confirmed".
- A reply that cannot resolve a complaint must name the specific reason and the next step open to the resident. "Your request cannot be processed" is not a finished reply.
- Do not promise a service that `routing-rules.md` does not say exists.
- Two files in this folder do not agree about SMS notification. Do not pick one silently.
- Do not invent a resident's contact details, case number, or the outcome of a case still open.

Done: every complaint in `complaints.md` appears exactly once in `triage.md` with an owner and a deadline, the three replies are specific enough to send, and each escalation names its trigger.
