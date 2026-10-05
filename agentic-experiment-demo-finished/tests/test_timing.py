import unittest

from src.timing import trial_hold_seconds


class TimingTests(unittest.TestCase):
    def test_long_sound_controls_trial_end(self):
        self.assertEqual(trial_hold_seconds(1.2, 1.57), 1.57)

    def test_long_response_window_controls_trial_end(self):
        self.assertEqual(trial_hold_seconds(2.0, 1.57), 2.0)
