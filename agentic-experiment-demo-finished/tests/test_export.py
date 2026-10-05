import csv
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from src.export import COLUMNS, export_results


class ExportTests(unittest.TestCase):
    def test_export_has_stable_columns_and_one_row_per_trial(self):
        row = {column: "" for column in COLUMNS}
        row.update({"participant_id": "demo-001", "seed": 42, "trial": 1})
        with TemporaryDirectory() as directory:
            output = export_results([row], "demo-001", Path(directory), timestamp="fixed")
            with output.open(newline="", encoding="utf-8") as handle:
                records = list(csv.DictReader(handle))
            self.assertEqual(records[0]["participant_id"], "demo-001")
            self.assertEqual(list(records[0]), COLUMNS)
            self.assertEqual(len(records), 1)
