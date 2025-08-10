import argparse
import os

from colorama import init, Fore, Style
from pynum2words import PyNum2Words

init(autoreset=True)

def main():
    default_english_dictionary_file_path = os.path.join(
        os.path.dirname(__file__),
        "dictionaries",
        "english.n2w"
    )

    parser = argparse.ArgumentParser(
        description="Convert numbers to their word representation and vice versa "
                    "using a built-in or custom dictionary."
    )

    parser.add_argument(
        "--number",
        type=int,
        help="The number you want to convert to words"
    )

    parser.add_argument(
        "--words",
        type=str,
        help="The words you want to convert to a number"
    )

    parser.add_argument(
        "--dict",
        default=default_english_dictionary_file_path,
        help="Path to your custom dictionary (.n2w) file [default: English]"
    )

    parser.add_argument(
        "--ac",
        action="store_true",
        help="Enable auto correction in words with typo if available"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="pyn2w Version 1.2",
        help="Show program's version number and exit."
    )

    arguments = parser.parse_args()

    if arguments.ac:
        converter = PyNum2Words(arguments.dict, auto_correct=True)
    else:
        converter = PyNum2Words(arguments.dict)

    if arguments.number is not None:
        result = converter.number_to_words(arguments.number)
        print(f"{Fore.GREEN + Style.BRIGHT}Result: {Style.RESET_ALL}{result}")
    elif arguments.words:
        result = converter.words_to_number(arguments.words)
        print(f"{Fore.GREEN + Style.BRIGHT}Result: {Style.RESET_ALL}{result}")
    else:
        print(f"{Fore.RED + Style.BRIGHT}📘 Usage Help{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Either --number or --words must be provided.\n")
        print("Examples:")
        print(f"  {Fore.CYAN}pyn2w --number 123{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}pyn2w --words 'One Hundred Twenty Three'{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}pyn2w --dict path/to/your/custom/dictionary --number 5{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}pyn2w --dict path/to/your/custom/dictionary --word 'One Hundred Twenty Three' {Style.RESET_ALL}")

if __name__ == "__main__":
    main()
