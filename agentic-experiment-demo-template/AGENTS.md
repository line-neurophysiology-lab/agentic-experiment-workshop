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

- Plan before implementation.
- Implement and test one component at a time.
- State ambiguities that require a scientific decision.
- Run relevant tests after each change.
