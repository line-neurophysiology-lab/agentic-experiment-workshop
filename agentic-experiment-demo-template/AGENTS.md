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

## PsychoPy presentation layer

- Response and timing code must use an active-window polling loop: a `visual.Window` must exist, and key capture must happen inside a `while clock.getTime() < duration: event.getKeys(...); core.wait(...)` loop, not `event.waitKeys(maxWait=...)` without a window. Without a window, PsychoPy's event backend has nothing to pump, so `waitKeys` returns immediately instead of blocking, and no visuals are ever shown.
- Before considering any milestone involving response windows, ITIs, or stimulus timing complete, verify the implementation against this pattern (see `../agentic-experiment-demo-finished/src/app.py` for a worked reference) rather than assuming `waitKeys`/`getKeys` behave correctly on their own.

## Working agreement

- Read the protocol, data dictionary, and this file before proposing changes.
- Complete `PLAN.md` before implementation.
- Implement only the milestone explicitly requested by the user.
- Do not modify files outside the requested milestone, even if later work appears straightforward.
- Run the tests relevant to the requested milestone.
- Report what those tests establish and what remains unvalidated.
- Stop after completing and testing the requested milestone. Do not continue to later milestones without a new user request.
- State ambiguities that require a scientific decision instead of silently choosing an answer.
