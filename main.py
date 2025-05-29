#!/usr/bin/env python3
# main.py

from colorama import init, Fore
from pyfiglet import figlet_format
from quiz_creator import QuizCreator
from quiz_runner import QuizRunner

def main():
    init(autoreset=True)
    # Show banner
    print(Fore.CYAN + figlet_format("Quiz App", font="slant"))

    # Menu loop
    while True:
        print(Fore.MAGENTA + "1) Create Questions")
        print(Fore.MAGENTA + "2) Take Quiz")
        print(Fore.MAGENTA + "3) Exit\n")

        choice = input(Fore.YELLOW + "Select an option: ").strip()
        if choice == "1":
            QuizCreator().run()
        elif choice == "2":
            QuizRunner().run()
        elif choice == "3":
            print(Fore.CYAN + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice – please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
