from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
STIMULI_DIR = PROJECT_DIR / "stimuli"
DATA_DIR = PROJECT_DIR / "data" / "synthetic"
TRIAL_COUNT = 12
GO_COUNT = 4
RESPONSE_WINDOW_SECONDS = 1.2
INTER_TRIAL_SECONDS = 0.4
USE_PARALLEL_PORT = False
PARALLEL_PORT_ADDRESS = 0x0378
TRIGGER_PULSE_SECONDS = 0.002

TRIGGERS = {
    "passive_start": 1, "passive_f": 2, "passive_sf": 3, "passive_l": 4,
    "one_back_start": 5, "go_f": 6, "go_sf": 7, "go_l": 8,
    "nogo_f": 9, "nogo_sf": 10, "nogo_l": 11, "button_press": 12,
}
