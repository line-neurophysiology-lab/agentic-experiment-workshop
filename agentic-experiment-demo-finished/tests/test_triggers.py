from pathlib import Path
import unittest

from src.config import TRIGGERS
from src.triggers import trial_trigger


class TriggerTests(unittest.TestCase):
    def test_active_trigger_codes(self):
        self.assertEqual(trial_trigger(True, Path("face_1.wav"), TRIGGERS), 6)
        self.assertEqual(trial_trigger(True, Path("face_1_scr.wav"), TRIGGERS), 7)
        self.assertEqual(trial_trigger(False, Path("face_1.wav"), TRIGGERS), 9)
        self.assertEqual(trial_trigger(False, Path("face_1_scr.wav"), TRIGGERS), 10)
        self.assertEqual(TRIGGERS["button_press"], 12)
