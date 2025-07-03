# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Licensed under the Apache License, Version 2.0 (the "License");

import argparse
import os

from rich.console import Console
from rich.panel import Panel

from pynum2words import PyNum2Words

console = Console()


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
        "--dict",
        default=default_english_dictionary_file_path,
        help="Path to your custom dictionary (.n2w) file [default: built-in English]"
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
        "--version",
        action="store_true",
        help="pynum2words CLI Version"
    )

    arguments = parser.parse_args()
    converter = PyNum2Words(arguments.dict)

    if arguments.number is not None:
        console.print(f"[bold green]Result:[/bold green] {converter.number_to_words(arguments.number)}")
    elif arguments.words:
        console.print(f"[bold green]Result:[/bold green] {converter.words_to_number(arguments.words)}")
    elif arguments.version:
        console.print(f"[blue]pynum2words Version 1.1[/blue]")
    else:
        console.print(Panel.fit(
            "[bold yellow]Either --number or --words must be provided.[/bold yellow]\n\n"
            "Examples:\n"
            "  pyn2w --number 123\n"
            "  pyn2w --words 'One Hundred Twenty Three'\n"
            "  pyn2w --dict path/to/your/custom/dictionary --number 5",
            title="📘 Usage Help",
            border_style="red"
        ))


if __name__ == "__main__":
    main()
