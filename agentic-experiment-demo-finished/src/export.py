import csv
from datetime import datetime


COLUMNS = [
    "participant_id", "seed", "trial", "stimulus", "stimulus_category",
    "is_go", "stimulus_trigger", "responded", "response_trigger",
    "correct", "reaction_time_ms",
]


def export_results(rows, participant_id, output_dir, timestamp=None):
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = timestamp or datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_id = "".join(character for character in participant_id if character.isalnum() or character in "-_")
    if not safe_id:
        raise ValueError("participant_id must contain a letter, number, hyphen, or underscore")
    output = output_dir / f"{safe_id}_{timestamp}.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return output
