from pathlib import Path
import unittest

from src.randomization import build_one_back_sequence


class RandomizationAcceptanceTests(unittest.TestCase):
    def test_protocol_invariants(self):
        stimuli = [Path(f"face_{index}.wav") for index in range(1, 6)]
        first = build_one_back_sequence(stimuli, 12, 4, 42)
        self.assertEqual(first, build_one_back_sequence(stimuli, 12, 4, 42))
        self.assertFalse(first[0]["is_go"])
        self.assertEqual(sum(item["is_go"] for item in first), 4)
        for index, item in enumerate(first[1:], 1):
            self.assertEqual(item["is_go"], item["stimulus"] == first[index - 1]["stimulus"])
