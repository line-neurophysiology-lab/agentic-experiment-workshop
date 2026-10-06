# Agent instructions

## Scientific invariants

- A go trial repeats the immediately preceding audio file.
- A no-go trial differs from the immediately preceding audio file.
- Trial 1 cannot be a go trial.
- The same seed must reproduce the same sequence.
- The default block has 12 trials and exactly four go trials.
- Follow the protocol and data dictionary; do not silently reinterpret them.

## Safety boundaries

- Use synthetic participant identifiers only.
- Keep physical trigger output disabled unless the scientist explicitly approves hardware testing.
- Never describe unvalidated software timing as physical audio-onset or EEG timing.
- Do not modify or replace stimulus files.

## Working agreement

- Read the protocol, data dictionary, and this file before proposing changes.
- Complete `PLAN.md` before implementation.
- Implement only the milestone explicitly requested by the user.
- Do not modify files outside the requested milestone, even if later work appears straightforward.
- Run the tests relevant to the requested milestone.
- Report what those tests establish and what remains unvalidated.
- Stop after completing and testing the requested milestone. Do not continue to later milestones without a new user request.
- State ambiguities that require a scientific decision instead of silently choosing an answer.
