# Workshop progression

## 1. Scientist describes the experiment

Complete `protocol/experiment_brief.md`. Use scientific language; do not design the software yet.

Suggested prompt:

> Read the experiment brief and project instructions. Do not implement anything. Identify missing decisions, contradictions, risks to validity, and requirements that cannot be tested in software.

## 2. Scientist resolves important ambiguities

Record approved answers in `protocol/decisions.md`.

Suggested prompt:

> Update the experiment specification and data dictionary using only the decisions recorded by the scientist. Preserve unresolved questions explicitly.

## 3. Agent proposes a verifiable plan

Suggested prompt:

> Complete PLAN.md. Separate scientific logic from PsychoPy presentation. Connect each milestone to acceptance criteria and tests. Do not implement yet.

## 4. Agent implements one layer at a time

Start with schedule generation, followed by scoring and export. Add PsychoPy only after the scientific logic passes its tests.

Suggested prompt:

> Implement only the next approved milestone. Run the relevant tests and explain which protocol requirements they establish.

## 5. Scientist validates the experiment

Inspect a synthetic run, its trial table, timing behavior and any device integration. Record what passed, what failed, and what remains unvalidated.
