# Agent instructions

## Scientific invariants

- A go trial repeats the immediately preceding audio file.
- A no-go trial must differ from the immediately preceding audio file.
- The first trial cannot be a go trial.
- A recorded seed must reproduce the same sequence.
- The default 12-trial block contains exactly four go trials.
- Trigger codes must match `protocol/experiment_specification.md`.
- CSV columns and meanings must match `protocol/data_dictionary.md`.

## Boundaries

- Never use real participant identifiers in demonstrations or tests.
- Do not enable the parallel port without explicit scientist approval and hardware validation.
- Do not claim browser, software, audio, or EEG timing has been validated.
- Do not change the protocol silently. Record scientific decisions in the protocol first.
- Keep generated data out of source modules.

## Required checks

- Run `python -m unittest discover -s tests -v` after changing scientific logic.
- Confirm no accidental no-go repeats across multiple seeds.
- Inspect CSV headers after changing export logic.
