# 10-minute workshop demo

## Goal

Use an AI coding agent to turn a short experiment specification into tested experiment code.

The demonstration uses a simple auditory 1-back task:

> Press SPACE when the sound repeats.

## 1. Give the agent the protocol — 1 minute

Show:

- `protocol/experiment_specification.md`
- `protocol/data_dictionary.md`
- `AGENTS.md`

Suggested prompt:

> Read the protocol, data dictionary, and project instructions. Do not write code yet. Identify any scientific ambiguity that would affect the implementation.

## 2. Ask for a plan — 1 minute

Suggested prompt:

> Complete `PLAN.md` with a short implementation plan. Separate the experiment logic from PsychoPy presentation and connect each step to a test. Do not write implementation code yet. Stop after updating the plan.

Highlight that randomization is scientific logic, PsychoPy is the presentation layer, and hardware triggers remain disabled.

## 3. Implement one component — 3 minutes

Suggested prompt:

> Implement only `src/randomization.py` and `tests/test_randomization.py`. Verify that the same seed reproduces the sequence, trial 1 is no-go, and there are exactly four real repetitions. Do not modify `app.py`, `export.py`, `triggers.py`, or any other files. Run the randomization tests, report the result, and stop.

Run:

```bash
python -m unittest tests.test_randomization -v
```

## 4. Show the completed experiment — 3 minutes

Open `../agentic-experiment-demo-finished` and run:

```bash
python main.py
```

Demonstrate that:

- The participant presses SPACE when the sound repeats.
- The seed makes the sequence reproducible.
- Results are exported as one row per trial.
- Triggers are simulated by default.

## 5. Main takeaway — 2 minutes

The agent did not decide the experiment. The scientist supplied:

- The experimental rules.
- The meaning of the data.
- The safety boundaries.
- The acceptance criteria.

The agent helped translate those decisions into modular, testable code.

Software tests can verify logical rules. They cannot establish scientific validity, participant comprehension, audio latency, or EEG timing.

## Take-home material

The `../trial-experiment-template` folder provides the same specification-first structure for students to develop their own experiment ideas.
