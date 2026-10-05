import sys
import uuid
from pathlib import Path

from psychopy import core, event, sound, visual

from src.export import export_results
from src.randomization import build_one_back_sequence
from src.triggers import TRIGGERS, TriggerEmitter

STIMULI_DIR = Path(__file__).resolve().parent.parent / "stimuli"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

RESPONSE_KEY = "space"
ABORT_KEY = "escape"
RESPONSE_WINDOW_S = 1.2
ITI_S = 0.4
TRIAL_COUNT = 12
GO_COUNT = 4
POLL_INTERVAL_S = 0.001


def _usable_stimuli():
    """Face and scrambled-face filenames only; letter files are retained but unused."""
    return sorted(
        (Path(path.name) for path in STIMULI_DIR.glob("*.wav") if not path.stem.startswith("letter")),
        key=str,
    )


def _new_participant_id():
    return f"demo-{uuid.uuid4().hex[:8]}"


def run_block(seed, window, hardware_enabled=False, hardware_sender=None):
    """Run one 1-back block and return the completed trial records.

    Uses a manual polling loop (not event.waitKeys) because key capture in
    PsychoPy needs an active window event pump to actually block for the
    response window; waitKeys without one returns immediately.

    Hardware trigger output defaults to off; a caller must pass
    hardware_enabled=True explicitly, which should only happen after the
    scientist has approved hardware testing.
    """
    sequence = build_one_back_sequence(_usable_stimuli(), TRIAL_COUNT, GO_COUNT, seed)
    emitter = TriggerEmitter(hardware_enabled=hardware_enabled, hardware_sender=hardware_sender)
    fixation = visual.TextStim(window, text="+", height=0.12, color="white")
    completed = []

    emitter.send(TRIGGERS["one_back_start"])

    for trial in sequence:
        fixation.draw()
        window.flip()
        event.clearEvents()

        audio = sound.Sound(str(STIMULI_DIR / trial["stimulus"]))
        clock = core.Clock()
        audio.play()
        clock.reset()
        emitter.send(trial["stimulus_trigger"])

        responded = False
        reaction_time_ms = None
        aborted = False
        while clock.getTime() < RESPONSE_WINDOW_S:
            keys = event.getKeys(keyList=[RESPONSE_KEY, ABORT_KEY], timeStamped=clock)
            if keys:
                key_name, key_time = keys[0]
                if key_name == ABORT_KEY:
                    aborted = True
                    break
                if not responded:
                    responded = True
                    reaction_time_ms = round(key_time * 1000)
                    emitter.send(TRIGGERS["button_press"])
            core.wait(POLL_INTERVAL_S)

        audio.stop()

        if aborted:
            break

        completed.append(
            {
                "seed": seed,
                "trial": trial["trial"],
                "stimulus": trial["stimulus"],
                "stimulus_category": trial["stimulus_category"],
                "is_go": trial["is_go"],
                "stimulus_trigger": trial["stimulus_trigger"],
                "responded": responded,
                "reaction_time_ms": reaction_time_ms,
            }
        )

        core.wait(ITI_S)

    return completed


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    participant_id = _new_participant_id()

    window = visual.Window(fullscr=False, size=(1100, 700), color="#101820", units="height")
    message = visual.TextStim(
        window,
        text="Press SPACE when the sound repeats\n\nPress any key to begin",
        height=0.045,
        color="white",
    )
    message.draw()
    window.flip()
    event.waitKeys()

    try:
        rows = run_block(seed, window)
        output_path = export_results(rows, participant_id, DATA_DIR)
        message.text = f"Block complete\n\nSaved to {output_path.name}\n\nPress any key to close"
        message.draw()
        window.flip()
        event.waitKeys()
        print(f"Wrote {len(rows)} trial rows to {output_path}")
    finally:
        window.close()
        core.quit()


if __name__ == "__main__":
    main()
