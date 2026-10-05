from pathlib import Path
import unittest

from src.randomization import build_one_back_sequence


class RandomizationTests(unittest.TestCase):
    def test_sequence_is_reproducible_and_valid(self):
        stimuli = [Path(f"face_{index}.wav") for index in range(1, 6)]
        first = build_one_back_sequence(stimuli, 12, 4, 42)
        self.assertEqual(first, build_one_back_sequence(stimuli, 12, 4, 42))
        self.assertEqual(sum(item["is_go"] for item in first), 4)
        self.assertFalse(first[0]["is_go"])
        for index, item in enumerate(first[1:], 1):
            self.assertEqual(item["is_go"], item["stimulus"] == first[index - 1]["stimulus"])
