# Implementation plan

## Intended outcome

Build the PsychoPy auditory 1-back task defined in `protocol/experiment_specification.md` and export data according to `protocol/data_dictionary.md`.

## Resolved ambiguities (scientist decisions, 2026-10-05)

- No-go stimulus sampling: unconstrained beyond "differs from immediately preceding file" (demo scope, no balance/no-replacement requirement).
- Go trials: exactly 4 total, split 2 repeats on `f` (face) and 2 repeats on `sf` (scrambled face).
- Letter (`l`) stimuli: excluded entirely from this block; never selected, never produce a `stimulus_trigger` value.
- `reaction_time_ms` / response window: measured from the software audio-play command only. This is explicitly software timing, not validated hardware or EEG-grade timing (per `AGENTS.md` safety boundary).

## Architecture

Experiment logic (deterministic, pure Python) is kept separate from PsychoPy presentation so the scientific rules can be tested without launching PsychoPy:

- `src/randomization.py` — pure sequence generation from a seed. No PsychoPy, no I/O.
- `src/triggers.py` — trigger code mapping and simulated/hardware output switch. Hardware path disabled by default.
- `src/export.py` — maps a completed trial record to the data-dictionary schema and writes output rows.
- `src/app.py` — PsychoPy presentation loop that wires the above together (audio playback, response collection, timing, ITI). Requires PsychoPy to run; not unit-tested the same way.

## Milestones

### M1 — Randomization (`src/randomization.py`, `tests/test_randomization.py`)
Generate a 12-trial sequence from an integer seed: trial 1 is no-go; exactly 4 go trials (2 repeating an `f` stimulus, 2 repeating an `sf` stimulus); every go trial repeats the immediately preceding file exactly; every no-go trial differs from the immediately preceding file; only `f`/`sf` stimuli are ever selected (no `l`); same seed reproduces the same sequence.
- Tests: same-seed reproducibility, trial-1-is-no-go, exactly-4-go-trials, go-category split is 2/2, every go trial truly repeats the prior file, every no-go trial truly differs from the prior file, no `l` category ever appears.

### M2 — Triggers (`src/triggers.py`, `tests/test_triggers.py`)
Map (category, is_go) to the active trigger codes (6/7/9/10), map button press to 12, and provide a block-start code (5). Hardware output defaults to off; a simulated/observable event is always recorded regardless of hardware state.
- Tests: correct code for each of the 4 stimulus conditions, button-press code, hardware-disabled-by-default, simulated event still observable when hardware is off.

### M3 — Export (`src/export.py`, `tests/test_export.py`)
Convert a completed trial record into a row matching `protocol/data_dictionary.md` exactly (column names, types, blank-not-zero for missing response fields), and write one row per completed trial.
- Tests: schema/column match, `correct` derivation from `is_go`/`responded`, blank (not zero/false-as-string) `response_trigger` and `reaction_time_ms` when no response occurred, one row per trial for a full block.

### M4 — PsychoPy presentation (`src/app.py`)
Wire randomization + triggers + export into the live task: play audio, collect Space within the 1.2 s software response window, honor the 0.4 s ITI, abort on Escape, keep hardware trigger output off unless explicitly enabled by the scientist.
- Not unit-testable without PsychoPy; depends on M1–M3 being correct first. Implemented only when explicitly requested, per `AGENTS.md`.

## Scientist validation (cannot be automated)

- Actual audio playback latency from the software play command to physical sound onset (affects whether response-window/EEG timing claims are valid).
- Hardware trigger output correctness and timing, only once explicitly approved for hardware testing.
- Participant comprehension of the go/no-go instruction in a real session.
- Any claim of EEG-timing accuracy — must remain unvalidated/unclaimed until the scientist confirms it separately.
