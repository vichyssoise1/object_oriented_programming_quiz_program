#!/usr/bin/env python3
# quiz_base.py

import json
from pathlib import Path

class QuizBase:
    def __init__(self, filename="questions.txt"):
        """
        Base class for quiz programs.
        Ensures the data file exists and stores its path relative to this script.
        """
        # Determine the directory where this file resides
        base_directory = Path(__file__).parent
        # Create the data file path relative to the script directory
        self.file_path = base_directory / filename
        # Ensure the data file exists
        self.file_path.touch(exist_ok=True)
        # (Optional) Debug: show where it's creating the file
        print(f"Data file path: {self.file_path.resolve()}")

    def load_data(self):
        """
        Read all lines from the JSONL file, parse each into a dict,
        and return the list of question records.
        """
        question_records = []
        with self.file_path.open("r", encoding="utf-8") as data_file:
            for line in data_file:
                try:
                    record_data = json.loads(line)
                    question_records.append(record_data)
                except json.JSONDecodeError:
                    continue
        return question_records

    def save_data(self, record: dict):
        """
        Append a single question record (dict) to the JSONL file.
        """
        with self.file_path.open("a", encoding="utf-8") as data_file:
            json_line = json.dumps(record, ensure_ascii=False)
            data_file.write(json_line + "\n")
