# Trial-based experiment template

This repository template helps a scientist turn an experiment idea into a specified, testable PsychoPy implementation with an AI coding agent.

It is intentionally experiment-neutral. It contains no predefined task, condition, stimulus, trigger code, or scoring rule.

## Recommended workflow

1. Complete `protocol/experiment_brief.md` in scientific language.
2. Ask the agent to identify ambiguities without writing code.
3. Resolve scientific decisions in `protocol/decisions.md`.
4. Ask the agent to complete the specification, data dictionary, and `PLAN.md`.
5. Implement and test schedule generation, scoring, export, triggers, and finally PsychoPy presentation.
6. Run a synthetic pilot and inspect its output.
7. Record the checks that still require the scientist or laboratory hardware.

## Project structure

```text
protocol/       Scientific intent, decisions and data contract
src/            Experiment implementation
tests/          Executable acceptance criteria
stimuli/        Authorized experiment assets
data/synthetic/ Synthetic trial-level data only
outputs/        Derived reports, figures and summaries
```

## Data policy

Use synthetic participant identifiers during development and workshops. Do not commit participant data, credentials, API keys, or identifiable information.

## Status

This is a starting template, not a working experiment and not a validated research instrument.
