import argparse
import os
from pyglow.pyglow import PyGlow
from pyglow.styles.foreground import Fore
from pynum2words import PyNum2Words

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
        "--nf",
        action="store_true",
        help="Disable number formatting when converting words to number."
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="pyn2w Version 1.2",
        help="Show program's version number and exit."
    )

    arguments = parser.parse_args()

    if arguments.ac and arguments.nf:
        converter = PyNum2Words(arguments.dict, auto_correct=True, format_number=False)
    elif arguments.ac:
        converter = PyNum2Words(arguments.dict, auto_correct=True)
    elif arguments.nf:
        converter = PyNum2Words(arguments.dict, format_number=False)
    else:
        converter = PyNum2Words(arguments.dict)

    if arguments.number is not None:
        result = converter.number_to_words(arguments.number)
        PyGlow.print(f"[green]Result:[/] {result}")
    elif arguments.words:
        result = converter.words_to_number(arguments.words)
        PyGlow.print(f"[green]Result: [/] {result}")
    else:
        PyGlow.printc(f"{Fore.RED}📘 Usage Help")
        PyGlow.printc(f"{Fore.YELLOW}Either --number or --words must be provided.\n")
        PyGlow.printc("Examples:")
        PyGlow.printc(f"  {Fore.CYAN}pyn2w --number 123")
        PyGlow.printc(f"  {Fore.CYAN}pyn2w --words 'One Hundred Twenty Three'")
        PyGlow.printc(f"  {Fore.CYAN}pyn2w --dict path/to/your/custom/dictionary --number 5")
        PyGlow.printc(f"  {Fore.CYAN}pyn2w --dict path/to/your/custom/dictionary --word 'One Hundred Twenty Three'")

if __name__ == "__main__":
    main()
