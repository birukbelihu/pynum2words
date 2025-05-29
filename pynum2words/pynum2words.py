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

import math
from typing import Dict, Tuple


def load_num2words_dictionary(file_path: str) -> Tuple[Dict[int, str], Dict[str, int]]:
    number_to_word = {}
    comments = ['#', '//', '/*', '*/', ';']

    with open(file_path, encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line or any(line.startswith(prefix) for prefix in comments):
                continue

            if '=' not in line:
                raise ValueError(f"Line {i} Invalid Format: {line} — expected 'number = word'")

            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()

            if not key.isdigit() or not value:
                raise ValueError(f"Invalid entry: {line} — left must be number, right non-empty")

            number_to_word[int(key)] = value

    word_to_number = {v.lower(): k for k, v in number_to_word.items()}
    return dict(sorted(number_to_word.items())), word_to_number


class PyNum2Words:
    def __init__(self, dict_file_path: str):
        self.num2word, self.word2num = load_num2words_dictionary(dict_file_path)
        self.base_units = self.get_base_units()

    def get_base_units(self) -> Dict[int, str]:
        units = {}
        for num in self.num2word:
            if num >= 100 and (math.log10(num) % 3 == 0 or num == 100):
                units[num] = self.num2word[num]
        return dict(sorted(units.items(), reverse=True))

    def number_to_words(self, number: int) -> str:
        if number == 0 and 0 in self.num2word:
            return self.num2word[0]
        if number < 0:
            return "Negative " + self.number_to_words(-number)

        if number in self.num2word:
            return self.num2word[number]

        result = []
        if number < 100:
            tens = number - number % 10
            units = number % 10
            if tens:
                result.append(self.num2word.get(tens, str(tens)))
            if units:
                result.append(self.num2word.get(units, str(units)))
        elif number < 1000:
            hundreds = number // 100
            remainder = number % 100
            result.append(self.num2word.get(hundreds, str(hundreds)))
            result.append(self.num2word[100])
            if remainder:
                result.append(self.number_to_words(remainder))
        else:
            for unit, name in self.base_units.items():
                if number >= unit:
                    quotient = number // unit
                    remainder = number % unit
                    result.append(self.number_to_words(quotient))
                    result.append(name)
                    if remainder:
                        result.append(self.number_to_words(remainder))
                    break
        return " ".join(result)

    def words_to_number(self, words: str) -> int:
        words = ' '.join(words.strip().lower().split())
        if words.startswith("negative"):
            return -self.words_to_number(words[8:].strip())

        tokens = words.split()
        total = 0
        current = 0
        ignore_words = {'e'}

        for token in tokens:
            if token in ignore_words:
                continue
            value = self.word2num.get(token)
            if value is None:
                raise ValueError(f"Invalid Word: {token}")
            if value == 100:
                if current == 0:
                    current = 1
                current *= value
            elif value >= 1000:
                if current == 0:
                    current = 1
                current *= value
                total += current
                current = 0
            else:
                current += value

        return total + current
