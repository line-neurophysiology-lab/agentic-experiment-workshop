def trial_hold_seconds(response_window_seconds, sound_duration_seconds):
    """Keep a trial open until its response window and audio have both ended."""
    if response_window_seconds <= 0 or sound_duration_seconds < 0:
        raise ValueError("Trial timing values must be positive")
    return max(response_window_seconds, sound_duration_seconds)
