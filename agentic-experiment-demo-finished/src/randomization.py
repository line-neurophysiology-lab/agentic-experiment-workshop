import random
import re


def discover_active_stimuli(stimuli_dir):
    files = sorted(stimuli_dir.glob("face_*.wav"))
    if len(files) < 2:
        raise RuntimeError(f"Expected at least two face WAV files in {stimuli_dir}")
    return files


def build_one_back_sequence(stimuli, trial_count=12, go_count=4, seed=1):
    if trial_count < 3 or not 1 <= go_count < trial_count or len(stimuli) < 2:
        raise ValueError("Invalid trial, go, or stimulus count")
    rng = random.Random(seed)
    go_indices = set(rng.sample(range(1, trial_count), go_count))
    trials = []
    for index in range(trial_count):
        is_go = index in go_indices
        if is_go:
            stimulus = trials[-1]["stimulus"]
        else:
            choices = stimuli if not trials else [item for item in stimuli if item != trials[-1]["stimulus"]]
            stimulus = rng.choice(choices)
        trials.append({"trial": index + 1, "stimulus": stimulus, "is_go": is_go})
    return trials


def stimulus_category(path):
    name = path.name
    if re.search(r"_scr\.wav$", name, re.IGNORECASE):
        return "sf"
    if re.match(r"face_\d+\.wav$", name, re.IGNORECASE):
        return "f"
    if name.lower().startswith("letter_"):
        return "l"
    raise ValueError(f"Unknown stimulus category: {name}")
