#!/usr/bin/env python3
# quiz_creator.py

from quiz_base import QuizBase

class QuizCreator(QuizBase):
    """
    Interactive quiz question creator.
    Inherits file I/O methods from QuizBase.
    """
    def __init__(self, filename="questions.txt"):
        super().__init__(filename)

    def run(self):
        """
        Stub for question-entry loop.
        Will prompt user for questions, options, and correct answer,
        then save each record using save_data().
        """
        # TODO: implement interactive loop here
        pass
