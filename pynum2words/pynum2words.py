import os
import difflib
import importlib.resources
from typing import Dict, Tuple


def load_pynum2words_dictionary(file_path: str) -> Tuple[Dict[int, str], Dict[str, int]]:
    """
    Load dictionary file into two mappings:
    - number_to_word: {int: str}
    - word_to_number: {str: int} (lowercased)
    """
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

    def get_base_units(self) -> Dict[int, str]:
        """
        Extract scaling units (hundred, thousand, million, etc.) from the dictionary.
        These are numbers that are powers of 10 and >= 100.
        """
        units = {}
        for num, word in self.num2word.items():
            s = str(num)
            if num >= 100 and s.startswith("1") and all(ch == "0" for ch in s[1:]):
                units[num] = word
        return dict(sorted(units.items(), reverse=True))

    def number_to_words(self, number: int) -> str:
        """Convert integer to words using recursive scale-aware logic."""
        num2word = self.num2word  # local binding
        base_units = self.base_units

        if number == 0 and 0 in num2word:
            return num2word[0]
        if number < 0:
            return "Negative " + self.number_to_words(-number)
        if number in num2word:
            return num2word[number]

        # Numbers < 100 (tens + units)
        if number < 100:
            tens, units = divmod(number, 10)
            parts = []
            if tens:
                parts.append(num2word.get(tens * 10, str(tens * 10)))
            if units:
                parts.append(num2word.get(units, str(units)))
            return " ".join(parts)

        for unit, name in base_units.items():
            if number >= unit:
                q, r = divmod(number, unit)
                parts = [self.number_to_words(q), name]
                if r:
                    parts.append(self.number_to_words(r))
                return " ".join(parts)

        return str(number)  # Fallback if dictionary incomplete

    def words_to_number(self, words: str):
        """Convert words back to number with O(n) complexity."""
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

    def get_fuzzy_match(self, word: str, cutoff: float = 0.7) -> str:
        matches = difflib.get_close_matches(word, self.word2num.keys(), n=1, cutoff=cutoff)
        return matches[0] if matches else None