from psychopy import core, event, gui, sound, visual

from . import config
from .export import export_results
from .randomization import build_one_back_sequence, discover_active_stimuli, stimulus_category
from .timing import trial_hold_seconds
from .triggers import TriggerOutput, trial_trigger


def collect_session_info():
    info = {"participant_id": "demo-001", "seed": "20261004"}
    dialog = gui.DlgFromDict(info, title="Auditory 1-back workshop demo", order=["participant_id", "seed"])
    if not dialog.OK:
        core.quit()
    info["seed"] = int(info["seed"])
    return info


def main():
    session = collect_session_info()
    stimuli = discover_active_stimuli(config.STIMULI_DIR)
    trials = build_one_back_sequence(stimuli, config.TRIAL_COUNT, config.GO_COUNT, session["seed"])
    trigger = TriggerOutput(config.USE_PARALLEL_PORT, config.PARALLEL_PORT_ADDRESS, config.TRIGGER_PULSE_SECONDS)
    window = visual.Window(fullscr=False, size=(1100, 700), color="#101820", units="height")
    fixation = visual.TextStim(window, text="+", height=0.12, color="white")
    message = visual.TextStim(window, text="Press SPACE when the sound repeats\n\nPress any key to begin", height=0.045, color="white")
    message.draw(); window.flip(); event.waitKeys()
    results = []
    try:
        trigger.send(config.TRIGGERS["one_back_start"], "one_back_start")
        for trial in trials:
            fixation.draw(); window.flip(); event.clearEvents()
            clip = sound.Sound(str(trial["stimulus"]))
            code = trial_trigger(trial["is_go"], trial["stimulus"], config.TRIGGERS)
            trigger.send(code, f"{'go' if trial['is_go'] else 'nogo'}_{stimulus_category(trial['stimulus'])}")
            trial_duration = trial_hold_seconds(config.RESPONSE_WINDOW_SECONDS, clip.getDuration())
            response_clock = core.Clock(); clip.play(); response_clock.reset()
            responded, reaction_time_ms = False, ""
            while response_clock.getTime() < trial_duration:
                keys = event.getKeys(keyList=["space", "escape"], timeStamped=response_clock)
                if keys:
                    key, key_time = keys[0]
                    if key == "escape": raise KeyboardInterrupt
                    if not responded and key_time <= config.RESPONSE_WINDOW_SECONDS:
                        responded, reaction_time_ms = True, round(key_time * 1000)
                        trigger.send(config.TRIGGERS["button_press"], "button_press")
                core.wait(0.001)
            clip.stop()
            results.append({
                "participant_id": session["participant_id"], "seed": session["seed"],
                "trial": trial["trial"], "stimulus": trial["stimulus"].name,
                "stimulus_category": stimulus_category(trial["stimulus"]), "is_go": trial["is_go"],
                "stimulus_trigger": code, "responded": responded,
                "response_trigger": config.TRIGGERS["button_press"] if responded else "",
                "correct": responded == trial["is_go"], "reaction_time_ms": reaction_time_ms,
            })
            core.wait(config.INTER_TRIAL_SECONDS)
        output = export_results(results, session["participant_id"], config.DATA_DIR)
        message.text = f"Block complete\n\nSaved to {output.name}\n\nPress any key to close"
        message.draw(); window.flip(); event.waitKeys()
    except KeyboardInterrupt:
        if results: export_results(results, session["participant_id"], config.DATA_DIR)
    finally:
        trigger.close(); window.close(); core.quit()
