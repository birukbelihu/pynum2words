import os
import difflib
import importlib.resources
from typing import Dict, Tuple


def load_pynum2words_dictionary(file_path: str) -> Tuple[Dict[int, str], Dict[str, int]]:
    number_to_word = {}
    comments = ('#', '//', '/*', '*/', ';')
    lines = []

    if os.path.isfile(file_path):
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
    else:
        try:
            file_name = os.path.basename(file_path)
            with importlib.resources.open_text("pynum2words.dictionaries", file_name, encoding="utf-8") as f:
                lines = f.readlines()
        except (ModuleNotFoundError, FileNotFoundError):
            raise FileNotFoundError(f"Dictionary file not found: {file_path}")

    for i, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith(comments):
            continue
        if '=' not in line:
            raise ValueError(f"Line {i}: Invalid format — expected 'number = word'")

        key, value = map(str.strip, line.split('=', 1))
        if not key.isdigit() or not value:
            raise ValueError(f"Line {i}: Invalid entry — left must be number, right non-empty")

        number_to_word[int(key)] = value

    word_to_number = {v.lower(): k for k, v in number_to_word.items()}
    return dict(sorted(number_to_word.items())), word_to_number

class PyNum2Words:
    def __init__(self, dict_file_path: str, auto_correct: bool = False, format_number: bool = True):
        self.num2word, self.word2num = load_pynum2words_dictionary(dict_file_path)
        self.auto_correct = auto_correct
        self.format_number = format_number
        self.base_units = self.get_base_units()

    def get_base_units(self) -> dict[int, str]:
        """Return base units >=100 for grouping (100, 1000, 1000000...)."""
        units = {}
        for num, word in self.num2word.items():
            s = str(num)
            if num >= 100 and s.startswith("1") and all(ch == "0" for ch in s[1:]):
                units[num] = word
        return dict(sorted(units.items(), reverse=True))

    def number_to_words(self, number: int) -> str:
        if number == 0 and 0 in self.num2word:
            return self.num2word[0]
        if number < 0:
            return "Negative " + self.number_to_words(-number)
        if number in self.num2word:
            return self.num2word[number]

        parts = []
        remainder = number
        scales_sorted = sorted(self.base_units.keys())

        for scale in reversed(scales_sorted):
            if remainder >= scale:
                group = remainder // scale
                remainder %= scale
                if scale >= 1000:
                    parts.append(f"{self.number_to_words(group)} {self.base_units[scale]}")
                else:
                    parts.append(self._convert_hundreds(group * scale))

        if remainder > 0:
            parts.append(self._convert_hundreds(remainder))

        return " ".join(parts).strip()

    def _convert_hundreds(self, number: int) -> str:
        """Convert numbers < 1000 to words."""
        if number >= 1000:
            raise ValueError(f"_convert_hundreds expects number < 1000, got {number}")

        if number in self.num2word:
            return self.num2word[number]

        parts = []
        hundreds = number // 100
        remainder = number % 100

        if hundreds > 0:
            parts.append(f"{self.num2word[hundreds]} {self.num2word[100]}")

        if remainder > 0:
            if remainder in self.num2word:
                parts.append(self.num2word[remainder])
            else:
                tens = remainder - remainder % 10
                units = remainder % 10
                if tens > 0:
                    parts.append(self.num2word.get(tens, str(tens)))
                if units > 0:
                    parts.append(self.num2word.get(units, str(units)))

        return " ".join(parts)

    def words_to_number(self, words: str):
        """Convert words back to integer with optional formatting."""
        words = " ".join(words.strip().replace("-", " ").lower().split())
        if words.startswith("negative"):
            return f"-{self.words_to_number(words[8:].strip())}"

        tokens = words.split()
        total = 0
        current = 0
        word2num = self.word2num
        ignore_words = {"and"}

        for token in tokens:
            if token in ignore_words:
                continue

            value = word2num.get(token)
            if value is None:
                if self.auto_correct:
                    suggestion = self.get_fuzzy_match(token)
                    if suggestion:
                        value = word2num[suggestion]
                    else:
                        raise ValueError(f"Invalid word: {token}")
                elif self.get_fuzzy_match(token) is not None:
                    raise ValueError(f"Invalid word: {token}, Did you mean {self.get_fuzzy_match(token)}?")
                else:
                    raise ValueError(f"Invalid word: {token}. No match found.")

            if value >= 1000:
                if current == 0:
                    current = 1
                current *= value
                total += current
                current = 0
            elif value == 100:
                if current == 0:
                    current = 1
                current *= value
            else:
                current += value

        number = total + current
        return f"{number:,}" if self.format_number else number

    def get_fuzzy_match(self, word: str, cutoff: float = 0.7):
        matches = difflib.get_close_matches(word, self.word2num.keys(), n=1, cutoff=cutoff)
        return matches[0] if matches else None