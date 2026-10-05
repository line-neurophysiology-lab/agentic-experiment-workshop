import random
from pathlib import Path

TRIGGER_CODES = {
    ("f", True): 6,
    ("sf", True): 7,
    ("f", False): 9,
    ("sf", False): 10,
}

_MAX_ATTEMPTS = 1000


def _infer_category(stimulus):
    stem = Path(stimulus).stem
    if stem.startswith("letter"):
        return "l"
    if stem.endswith("_scr"):
        return "sf"
    if stem.startswith("face"):
        return "f"
    raise ValueError(f"Cannot infer stimulus category for {stimulus!r}")


def _build_pool(stimuli):
    pool = {}
    for stimulus in stimuli:
        category = _infer_category(stimulus)
        if category == "l":
            continue
        pool.setdefault(category, []).append(stimulus)
    for category in pool:
        pool[category].sort(key=str)
    return pool


def _attempt_sequence(pool, categories, trial_count, go_count, go_quota, rng):
    sequence = []
    remaining_go_total = go_count
    remaining_go_quota = dict(go_quota)
    prev_category = None
    prev_stimulus = None
    last_was_go = False

    for trial in range(1, trial_count + 1):
        remaining_trials_left = trial_count - trial + 1
        can_go = (
            trial > 1
            and not last_was_go
            and remaining_go_total > 0
            and remaining_go_quota[prev_category] > 0
        )
        is_go = can_go and rng.random() < (remaining_go_total / remaining_trials_left)

        if is_go:
            category = prev_category
            stimulus = prev_stimulus
            remaining_go_total -= 1
            remaining_go_quota[category] -= 1
        else:
            category = rng.choice(categories)
            choices = pool[category]
            if category == prev_category:
                choices = [item for item in choices if item != prev_stimulus]
            stimulus = rng.choice(choices)

        sequence.append(
            {
                "trial": trial,
                "stimulus": stimulus,
                "stimulus_category": category,
                "is_go": is_go,
                "stimulus_trigger": TRIGGER_CODES[(category, is_go)],
            }
        )
        prev_category = category
        prev_stimulus = stimulus
        last_was_go = is_go

    if remaining_go_total != 0 or any(remaining_go_quota.values()):
        return None
    return sequence


def build_one_back_sequence(stimuli, trial_count=12, go_count=4, seed=1):
    """Return trial dictionaries satisfying the protocol's 1-back invariants.

    Letter stimuli are excluded. Go trials are split evenly across the
    non-letter categories present (2 face / 2 scrambled-face for this
    protocol's default of 4 go trials), and no two go trials are adjacent.
    """
    pool = _build_pool(stimuli)
    categories = sorted(pool)
    if not categories:
        raise ValueError("No usable (non-letter) stimuli provided")
    if go_count % len(categories) != 0:
        raise ValueError(
            f"go_count={go_count} does not split evenly across categories {categories}"
        )
    go_quota = {category: go_count // len(categories) for category in categories}

    rng = random.Random(seed)
    for _ in range(_MAX_ATTEMPTS):
        sequence = _attempt_sequence(pool, categories, trial_count, go_count, go_quota, rng)
        if sequence is not None:
            return sequence
    raise RuntimeError("Could not generate a sequence satisfying protocol invariants")
