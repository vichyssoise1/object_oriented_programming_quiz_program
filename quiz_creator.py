#!/usr/bin/env python3
# quiz_creator.py

from quiz_base import QuizBase
from colorama import init, Fore
from pyfiglet import figlet_format

class QuizCreator(QuizBase):
    """
    Interactive quiz question creator.
    Inherits file I/O methods from QuizBase.
    """
    def __init__(self, filename="questions.txt"):
        super().__init__(filename)
        init(autoreset=True)

    def run(self):
        """
        Prompt user to enter questions with four options and the correct answer.
        Each entry is saved immediately to the JSONL file.
        """
        # Display ASCII banner
        banner_text = figlet_format("Quiz Creator", font="slant")
        print(Fore.CYAN + banner_text)
        print(Fore.MAGENTA + f"Questions will be saved to {self.file_path}\n")

        while True:
            # Prompt for question text
            print(Fore.YELLOW + "Enter your question (or type 'exit' to finish):")
            question_text = input("> ").strip()
            if question_text.lower() == "exit":
                print(Fore.CYAN + "All questions saved. Goodbye!")
                break

            # Prompt for four options a–d
            options = {}
            for option_key in ["a", "b", "c", "d"]:
                print(Fore.YELLOW + f"Option {option_key}:", end=" ")
                option_text = input().strip()
                options[option_key] = option_text

            # Prompt for correct answer
            correct_choice = ""
            while correct_choice not in options:
                print(Fore.YELLOW + "Correct answer (a/b/c/d):", end=" ")
                correct_choice = input().strip().lower()
                if correct_choice not in options:
                    print(Fore.RED + "Invalid choice. Please enter a, b, c, or d.")

            # Build the record and save
            record = {
                "question": question_text,
                "options": options,
                "answer": correct_choice
            }
            self.save_data(record)
            print(Fore.GREEN + "✔ Question saved!\n")
