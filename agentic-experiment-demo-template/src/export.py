COLUMNS = [
    "participant_id", "seed", "trial", "stimulus", "stimulus_category",
    "is_go", "stimulus_trigger", "responded", "response_trigger",
    "correct", "reaction_time_ms",
]


def export_results(rows, participant_id, output_dir, timestamp=None):
    """Write one validated row per completed trial using the data dictionary."""
    raise NotImplementedError("Workshop task: implement stable CSV export")
