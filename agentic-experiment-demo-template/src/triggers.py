TRIGGERS = {
    "one_back_start": 5,
    "go_f": 6,
    "go_sf": 7,
    "nogo_f": 9,
    "nogo_sf": 10,
    "button_press": 12,
}


def trial_trigger(is_go, stimulus):
    """Map a trial condition and filename to the protocol trigger code."""
    raise NotImplementedError("Workshop task: implement and test trigger mapping")
