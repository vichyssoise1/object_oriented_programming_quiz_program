#!/usr/bin/env python3
# quiz_base.py

import json
from pathlib import Path

class QuizBase:
    def __init__(self, filename="questions.txt"):
        """
        Base class for quiz programs.
        Ensures the data file exists and stores its path.
        """
        self.file_path = Path(filename)
        self.file_path.touch(exist_ok=True)

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
                    # Skip any malformed lines
                    continue
        return question_records
