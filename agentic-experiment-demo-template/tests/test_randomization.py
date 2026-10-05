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


class RandomizationCategoryTests(unittest.TestCase):
    def setUp(self):
        self.stimuli = (
            [Path(f"face_{index}.wav") for index in range(1, 11)]
            + [Path(f"face_{index}_scr.wav") for index in range(1, 11)]
            + [Path(f"letter_{index}_x.wav") for index in range(1, 11)]
        )

    def test_go_trials_split_two_per_category(self):
        for seed in (1, 2, 3, 42, 99):
            sequence = build_one_back_sequence(self.stimuli, 12, 4, seed)
            go_categories = [item["stimulus_category"] for item in sequence if item["is_go"]]
            self.assertEqual(go_categories.count("f"), 2)
            self.assertEqual(go_categories.count("sf"), 2)

    def test_letter_stimuli_never_selected(self):
        sequence = build_one_back_sequence(self.stimuli, 12, 4, 7)
        categories = {item["stimulus_category"] for item in sequence}
        self.assertNotIn("l", categories)
        self.assertTrue(all("letter" not in str(item["stimulus"]) for item in sequence))

    def test_no_two_consecutive_go_trials(self):
        sequence = build_one_back_sequence(self.stimuli, 12, 4, 7)
        for previous, current in zip(sequence, sequence[1:]):
            self.assertFalse(previous["is_go"] and current["is_go"])

    def test_no_go_trials_differ_from_preceding_stimulus(self):
        sequence = build_one_back_sequence(self.stimuli, 12, 4, 7)
        for index, item in enumerate(sequence[1:], 1):
            if not item["is_go"]:
                self.assertNotEqual(item["stimulus"], sequence[index - 1]["stimulus"])

    def test_trigger_codes_match_protocol_table(self):
        sequence = build_one_back_sequence(self.stimuli, 12, 4, 7)
        expected = {
            ("f", True): 6,
            ("sf", True): 7,
            ("f", False): 9,
            ("sf", False): 10,
        }
        for item in sequence:
            key = (item["stimulus_category"], item["is_go"])
            self.assertEqual(item["stimulus_trigger"], expected[key])

    def test_same_seed_is_reproducible_with_categories(self):
        first = build_one_back_sequence(self.stimuli, 12, 4, 123)
        second = build_one_back_sequence(self.stimuli, 12, 4, 123)
        self.assertEqual(first, second)
