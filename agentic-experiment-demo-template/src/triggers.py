from pathlib import Path

TRIGGERS = {
    "one_back_start": 5,
    "go_f": 6,
    "go_sf": 7,
    "nogo_f": 9,
    "nogo_sf": 10,
    "button_press": 12,
}


def _infer_category(stimulus):
    stem = Path(stimulus).stem
    if stem.endswith("_scr"):
        return "sf"
    return "f"


def trial_trigger(is_go, stimulus):
    """Map a trial condition and filename to the protocol trigger code."""
    category = _infer_category(stimulus)
    key = f"{'go' if is_go else 'nogo'}_{category}"
    return TRIGGERS[key]


class TriggerEmitter:
    """Records trigger events and optionally forwards them to hardware.

    Hardware output defaults to off per the protocol's safety boundary.
    Simulated events are always recorded, regardless of hardware state, so
    they remain observable in tests and logs.
    """

    def __init__(self, hardware_enabled=False, hardware_sender=None):
        self.hardware_enabled = hardware_enabled
        self._hardware_sender = hardware_sender
        self.sent_events = []

    def send(self, code):
        self.sent_events.append(code)
        if self.hardware_enabled:
            if self._hardware_sender is None:
                raise RuntimeError("Hardware enabled but no hardware_sender configured")
            self._hardware_sender(code)
        return code
