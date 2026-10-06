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

- Keep an active `visual.Window` open during presentation and response collection.
- Collect responses in a polling loop with `event.getKeys(...)`; do not rely on `event.waitKeys(maxWait=...)` without an active window.
- Keep each trial active until both the response window and audio playback have ended. A response must not cause the next sound to start early.
- Clear buffered keyboard events before each trial.
- Treat reaction time as elapsed time from the software audio-play command, not validated physical audio onset.
- Refer to `../agentic-experiment-demo-finished/src/app.py` for the worked presentation pattern.

## Architecture and checks

- Keep randomization, trigger mapping, export, and timing calculations independent of PsychoPy.
- Import PsychoPy only in the presentation layer.
- Run `python -m unittest discover -s tests -v` after changing scientific logic.
- Confirm no accidental no-go repetitions across multiple seeds.
- Inspect CSV headers after changing export logic.

## Working agreement

- Read the protocol, data dictionary, and this file before proposing changes.
- Complete `PLAN.md` before implementation.
- Implement only the milestone explicitly requested by the user.
- Do not modify files outside the requested milestone, even if later work appears straightforward.
- Run the tests relevant to the requested milestone.
- Report what those tests establish and what remains unvalidated.
- Stop after completing and testing the requested milestone. Do not continue to later milestones without a new user request.
- State ambiguities that require a scientific decision instead of silently choosing an answer.
