import csv
from pathlib import Path

COLUMNS = [
    "participant_id", "seed", "trial", "stimulus", "stimulus_category",
    "is_go", "stimulus_trigger", "responded", "response_trigger",
    "correct", "reaction_time_ms",
]

_RAW_FIELDS = [
    "seed", "trial", "stimulus", "stimulus_category",
    "is_go", "stimulus_trigger", "responded", "reaction_time_ms",
]


def _build_row(trial, participant_id):
    missing = [field for field in _RAW_FIELDS if field not in trial]
    if missing:
        raise ValueError(f"Trial record missing required fields: {missing}")

    is_go = trial["is_go"]
    responded = trial["responded"]
    correct = responded if is_go else not responded

    return {
        "participant_id": participant_id,
        "seed": trial["seed"],
        "trial": trial["trial"],
        "stimulus": str(trial["stimulus"]),
        "stimulus_category": trial["stimulus_category"],
        "is_go": is_go,
        "stimulus_trigger": trial["stimulus_trigger"],
        "responded": responded,
        "response_trigger": 12 if responded else "",
        "correct": correct,
        "reaction_time_ms": trial["reaction_time_ms"] if responded else "",
    }


def export_results(rows, participant_id, output_dir, timestamp=None):
    """Write one validated row per completed trial using the data dictionary."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    name_parts = [str(participant_id)]
    if timestamp is not None:
        name_parts.append(str(timestamp))
    output_path = output_dir / ("_".join(name_parts) + ".csv")

    built_rows = [_build_row(trial, participant_id) for trial in rows]

    with output_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(built_rows)

    return output_path
