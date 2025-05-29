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

from importlib.resources import files
from typing import Tuple, Dict


def load_num2words_dictionary(dictionary_name: str, suppress_error: bool = False) -> Tuple[
    Dict[int, str], Dict[str, int]]:
    dictionary_file_path = files("pynum2words.dictionaries").joinpath(dictionary_name)
    number_to_word = {}
    comments = ['#', '//', '/*', '*/', ';']

    with dictionary_file_path.open("r", encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            line = line.strip()
            if not line or any(line.startswith(prefix) for prefix in comments):
                continue

            if '=' not in line:
                error_message = f"[Line {i}] Invalid format: '{line}' — expected 'number = word'"
                if suppress_error:
                    print(f"Warning: {error_message}")
                    continue
                else:
                    raise ValueError(error_message)

            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()

            if not key.isdigit() or not value:
                error_message = (f"[Line {i}] Invalid entry: '{line}' — left side must be "
                                 f"a number and right side non-empty")
                if suppress_error:
                    print(f"Warning: {error_message}")
                    continue
                else:
                    raise ValueError(error_message)

            number_to_word[int(key)] = value

    number_to_word = dict(sorted(number_to_word.items(), reverse=True))
    word_to_number = {v.lower(): k for k, v in number_to_word.items()}

    return number_to_word, word_to_number
