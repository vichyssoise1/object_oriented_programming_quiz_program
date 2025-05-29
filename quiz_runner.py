#!/usr/bin/env python3
# quiz_runner.py

import random
from quiz_base import QuizBase
from colorama import init, Fore
from pyfiglet import figlet_format
from inputimeout import inputimeout, TimeoutOccurred

class QuizRunner(QuizBase):
    """
    Interactive quiz runner that selects random questions,
    enforces a time limit, and tracks score.
    """
    def __init__(self, filename="questions.txt", timeout_seconds=10):
        super().__init__(filename)
        init(autoreset=True)
        self.timeout_seconds = timeout_seconds

    def run(self):
        """
        Load questions, then run through them randomly.
        Each question has a time limit; tracks total and correct answers.
        """
        # Banner
        print(Fore.BLUE + figlet_format("Quiz Time!", font="slant"))
        print(Fore.MAGENTA + "Type 'exit' anytime to quit.\n")

        questions = self.load_data()
        if not questions:
            print(Fore.RED + "❌ No questions found.")
            return

        asked_ids = set()
        total_questions = 0
        correct_answers = 0

        while len(asked_ids) < len(questions):
            question = random.choice(questions)
            qid = id(question)
            if qid in asked_ids:
                continue
            asked_ids.add(qid)

            # Display
            print(Fore.CYAN + "\n🧠 " + question["question"])
            for key, text in question["options"].items():
                print(Fore.YELLOW + f"  {key}) {text}")

            # Prompt with timeout, validating non‐blank
            user_input = None
            try:
                raw = inputimeout(
                    prompt=Fore.MAGENTA + f"⏱️ Your answer ({self.timeout_seconds}s): ",
                    timeout=self.timeout_seconds
                ).strip().lower()

                # Reprompt while blank or not in valid commands
                valid_choices = set(question["options"].keys()) | {"exit"}
                while raw not in valid_choices:
                    print(Fore.RED + "Invalid choice. Enter a/b/c/d or 'exit'.")
                    raw = inputimeout(
                        prompt=Fore.MAGENTA + f"⏱️ Your answer ({self.timeout_seconds}s): ",
                        timeout=self.timeout_seconds
                    ).strip().lower()

                user_input = raw

            except TimeoutOccurred:
                print(Fore.RED + "\n⏰ Time's up!")
                # user_input stays None

            # Handle exit
            if user_input == "exit":
                break

            total_questions += 1

            # Scoring
            if user_input == question["answer"]:
                correct_answers += 1
                print(Fore.GREEN + "✅ Correct!")
            elif user_input is None:
                correct = question["options"][question["answer"]]
                print(Fore.RED + f"❌ No answer. Correct was {question['answer']}) {correct}")
            else:
                correct = question["options"][question["answer"]]
                print(Fore.RED + f"❌ Wrong. Correct was {question['answer']}) {correct}")

        # Summary
        print(Fore.MAGENTA + "\n📊 Quiz Summary")
        print(Fore.MAGENTA + f"You got {correct_answers} out of {total_questions} correct.")
        if total_questions > 0:
            if correct_answers == total_questions:
                print(Fore.GREEN + "🔥 Perfect score!")
            elif correct_answers >= total_questions / 2:
                print(Fore.YELLOW + "💪 Nice job!")
            else:
                print(Fore.RED + "📚 Keep practicing!")
