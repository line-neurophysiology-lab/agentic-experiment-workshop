# Agent instructions

## Source of truth

- Read `protocol/experiment_brief.md`, `protocol/experiment_specification.md`, `protocol/data_dictionary.md`, and `protocol/decisions.md` before implementation.
- Treat the scientist's protocol and recorded decisions as authoritative.
- Never resolve a scientific ambiguity silently. Record it in `PLAN.md` and request a scientist decision.
- Update the protocol before implementing an approved change to experimental behavior.

## Architecture

- Keep schedule generation, scoring, trigger mapping, and export independent of PsychoPy.
- Import PsychoPy only in the presentation/application layer.
- Represent the experiment explicitly as sessions, blocks, and trials when those levels exist.
- Use a local seeded random-number generator. Do not alter global random state.
- Keep one trial-level output row per completed trial unless the data dictionary explicitly says otherwise.

## Safety and data

- Use synthetic participant identifiers during development and tests.
- Write synthetic trial data under `data/synthetic/`.
- Write figures, reports and derived summaries under `outputs/`.
- Never overwrite an existing data file silently.
- Keep physical trigger and device output disabled by default.
- Require an explicit configuration flag and scientist approval before hardware access.
- Do not claim hardware-grade timing without empirical validation.
- Do not modify source stimuli unless the scientist explicitly requests it.

## Verification

- Convert protocol acceptance criteria into automated tests where possible.
- Run `python -m unittest discover -s tests -v` after changing scientific logic.
- Distinguish software checks from scientist review and hardware validation.
- Report remaining assumptions, limitations and failed checks clearly.
