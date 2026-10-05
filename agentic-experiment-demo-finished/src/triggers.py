from .randomization import stimulus_category


def trial_trigger(is_go, stimulus, trigger_map):
    condition = "go" if is_go else "nogo"
    return trigger_map[f"{condition}_{stimulus_category(stimulus)}"]


class TriggerOutput:
    def __init__(self, enabled, address, pulse_seconds):
        self.pulse_seconds = pulse_seconds
        self.port = None
        if enabled:
            from psychopy import parallel
            self.port = parallel.ParallelPort(address=address)
            self.port.setData(0)

    def send(self, code, label):
        print(f"trigger {code}: {label}")
        if self.port is not None:
            from psychopy import core
            self.port.setData(code)
            core.wait(self.pulse_seconds)
            self.port.setData(0)

    def close(self):
        if self.port is not None:
            self.port.setData(0)
