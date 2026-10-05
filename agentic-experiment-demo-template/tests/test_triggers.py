from pathlib import Path
import unittest

from src.triggers import TRIGGERS, TriggerEmitter, trial_trigger


class TrialTriggerTests(unittest.TestCase):
    def test_go_face(self):
        self.assertEqual(trial_trigger(True, Path("face_1.wav")), 6)

    def test_go_scrambled_face(self):
        self.assertEqual(trial_trigger(True, Path("face_1_scr.wav")), 7)

    def test_nogo_face(self):
        self.assertEqual(trial_trigger(False, Path("face_2.wav")), 9)

    def test_nogo_scrambled_face(self):
        self.assertEqual(trial_trigger(False, Path("face_2_scr.wav")), 10)

    def test_button_press_and_block_start_codes(self):
        self.assertEqual(TRIGGERS["button_press"], 12)
        self.assertEqual(TRIGGERS["one_back_start"], 5)


class TriggerEmitterTests(unittest.TestCase):
    def test_hardware_disabled_by_default(self):
        emitter = TriggerEmitter()
        self.assertFalse(emitter.hardware_enabled)

    def test_simulated_event_recorded_when_hardware_off(self):
        emitter = TriggerEmitter()
        emitter.send(6)
        self.assertEqual(emitter.sent_events, [6])

    def test_hardware_sender_not_called_when_disabled(self):
        calls = []
        emitter = TriggerEmitter(hardware_enabled=False, hardware_sender=calls.append)
        emitter.send(6)
        self.assertEqual(calls, [])
        self.assertEqual(emitter.sent_events, [6])

    def test_hardware_sender_called_when_explicitly_enabled(self):
        calls = []
        emitter = TriggerEmitter(hardware_enabled=True, hardware_sender=calls.append)
        emitter.send(6)
        self.assertEqual(calls, [6])
        self.assertEqual(emitter.sent_events, [6])

    def test_hardware_enabled_without_sender_raises(self):
        emitter = TriggerEmitter(hardware_enabled=True)
        with self.assertRaises(RuntimeError):
            emitter.send(6)


if __name__ == "__main__":
    unittest.main()
