#!/usr/bin/env python3
# quiz_runner.py

from quiz_base import QuizBase

class QuizRunner(QuizBase):
    """
    Interactive quiz runner that selects random questions,
    enforces a time limit, and tracks score.
    """
    def __init__(self, filename="questions.txt", timeout_seconds=10):
        super().__init__(filename)
        self.timeout_seconds = timeout_seconds

    def run(self):
        """
        Stub for quiz loop.
        Will load questions, prompt user, enforce timer, and track score.
        """
        # TODO: implement quiz loop here
        pass
