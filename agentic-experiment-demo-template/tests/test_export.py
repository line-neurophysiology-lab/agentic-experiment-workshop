import csv
import tempfile
import unittest
from pathlib import Path

from src.export import COLUMNS, export_results


def _trial(trial, is_go, responded, reaction_time_ms=None, category="f"):
    stimulus_trigger = {("f", True): 6, ("sf", True): 7, ("f", False): 9, ("sf", False): 10}[
        (category, is_go)
    ]
    return {
        "seed": 42,
        "trial": trial,
        "stimulus": Path(f"face_{trial}.wav"),
        "stimulus_category": category,
        "is_go": is_go,
        "stimulus_trigger": stimulus_trigger,
        "responded": responded,
        "reaction_time_ms": reaction_time_ms,
    }


class ExportAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)
        self.output_dir = Path(self._tmpdir.name)

    def _read_csv(self, path):
        with open(path, newline="") as handle:
            return list(csv.DictReader(handle))

    def test_csv_header_matches_data_dictionary(self):
        rows = [_trial(1, is_go=False, responded=False)]
        path = export_results(rows, "P01", self.output_dir)
        with open(path, newline="") as handle:
            header = next(csv.reader(handle))
        self.assertEqual(header, COLUMNS)

    def test_one_row_per_completed_trial(self):
        rows = [
            _trial(1, is_go=False, responded=False),
            _trial(2, is_go=True, responded=True, reaction_time_ms=350),
            _trial(3, is_go=False, responded=False),
        ]
        path = export_results(rows, "P01", self.output_dir)
        self.assertEqual(len(self._read_csv(path)), 3)

    def test_go_trial_with_response_is_correct(self):
        rows = [_trial(2, is_go=True, responded=True, reaction_time_ms=350)]
        path = export_results(rows, "P01", self.output_dir)
        row = self._read_csv(path)[0]
        self.assertEqual(row["correct"], "True")
        self.assertEqual(row["response_trigger"], "12")
        self.assertEqual(row["reaction_time_ms"], "350")

    def test_go_trial_without_response_is_incorrect(self):
        rows = [_trial(2, is_go=True, responded=False)]
        path = export_results(rows, "P01", self.output_dir)
        row = self._read_csv(path)[0]
        self.assertEqual(row["correct"], "False")

    def test_nogo_trial_without_response_is_correct(self):
        rows = [_trial(1, is_go=False, responded=False)]
        path = export_results(rows, "P01", self.output_dir)
        row = self._read_csv(path)[0]
        self.assertEqual(row["correct"], "True")

    def test_nogo_trial_with_response_is_incorrect(self):
        rows = [_trial(1, is_go=False, responded=True, reaction_time_ms=400)]
        path = export_results(rows, "P01", self.output_dir)
        row = self._read_csv(path)[0]
        self.assertEqual(row["correct"], "False")

    def test_missing_response_fields_are_blank_not_zero(self):
        rows = [_trial(1, is_go=False, responded=False)]
        path = export_results(rows, "P01", self.output_dir)
        row = self._read_csv(path)[0]
        self.assertEqual(row["response_trigger"], "")
        self.assertEqual(row["reaction_time_ms"], "")

    def test_missing_required_field_raises(self):
        incomplete = _trial(1, is_go=False, responded=False)
        del incomplete["reaction_time_ms"]
        with self.assertRaises(ValueError):
            export_results([incomplete], "P01", self.output_dir)


if __name__ == "__main__":
    unittest.main()
