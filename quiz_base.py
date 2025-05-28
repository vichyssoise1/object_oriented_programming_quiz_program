#!/usr/bin/env python3
# quiz_base.py

from pathlib import Path

class QuizBase:
    def __init__(self, filename="questions.txt"):
        """
        Base class for quiz programs.
        Ensures the data file exists and stores its path.
        """
        self.file_path = Path(filename)
        # Create the file if it doesn't exist
        self.file_path.touch(exist_ok=True)
