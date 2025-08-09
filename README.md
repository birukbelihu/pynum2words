# pynum2words

![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/pynum2words)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/pynum2words)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/pynum2words)
[![PyPI Downloads](https://static.pepy.tech/badge/pynum2words)](https://pepy.tech/projects/pynum2words)
![Python](https://img.shields.io/pypi/pyversions/pynum2words)

**pynum2words** is a Python library for converting numbers to their word representation and vice versa, using a built-in or custom dictionary.

---
GitHub: [pynum2words](https://github.com/BirukBelihu/pynum2words)
---

## ✨ Features

- 🔧 Highly customizable
- 🔢 Convert number ➜ word and word ➜ number without an upper limit
- 🌐 25+ Built-in Language dictionaries out of the box
- 🌍 Supports custom language dictionaries (`.n2w`)
- 🚀 Support comments on the dictionaries(#, //, /*, */, ;).  
- 📦 Command line & python API support
- ✅ Autocorrect words with typo in words to number converter (**Preview feature**)
- 📐 Format numbers in word to number conversion (**Preview feature**)

---

## 📦 Installation

```
pip install pynum2words
```

You can also install pynum2words from source code. source code may not be stable, but it will have the latest features and bug fixes.

Clone the repository:

```
git clone https://github.com/birukbelihu/pynum2words.git
```

Go inside the project directory:

```
cd pynum2words
```

### Set up Python virtual environment(I recommend using [uv](https://github.com/astral-sh/uv) for lightning speed)

### With uv

```bash
uv venv .venv
```

### With Python

```bash
python -m venv .venv
```

# Activate virtual environment

```bash
.venv\Scripts\activate # On Windows
```

```bash
source .venv/bin/activate # On Linux, WSL & macOS
```

# Install required dependencies

### With uv

```bash
uv pip install -r requirements.txt
```

### With Python

```bash
pip install -r requirements.txt
```

Install pynum2words:

```
pip install -e .
```

---

## 🧠 Example Usage

### CLI

```bash
# Convert number to words
pyn2w --number 12345
# Output: Twelve Thousand Three Hundred Forty Five

# Convert words to number with custom dictionary(You can also add autocorrect(--ac) flag if you're using the preview version(1.3.5)
pyn2w --word "ሁለት መቶ ሀምሳ ሰባት ሺህ አምስት መቶ ሰላሳ ሶስት" --dict dictionaries/amharic.n2w
# Output: 257533
```

### Python

```python
from pynum2words.builtin_dictionaries import english_dictionary
from pynum2words.pynum2words import PyNum2Words

# Initialize converter

english_converter = PyNum2Words(english_dictionary(), auto_correct=True)

# Number to words(English)
print(english_converter.number_to_words(49285294))  # Output: Forty Nine Million Two Hundred Eighty Five Thousand Two Hundred Ninety Four
# Words to number(English)
print(english_converter.words_to_number("Two Hundred Forty One Thousand Eight Hundred Forty One"))  # Output: 241841
```

## Builtin Dictionaries

- **Afrikaans**: `pynum2words.builtin_dictionaries.afrikaans_dictionary()`
- **Amharic**: `pynum2words.builtin_dictionaries.amharic_dictionary()`
- **Arabic**: `pynum2words.builtin_dictionaries.arabic_dictionary()`
- **Armenian**: `pynum2words.builtin_dictionaries.armenian_dictionary()`
- **Bengali**: `pynum2words.builtin_dictionaries.bengali_dictionary()`
- **Chinese**: `pynum2words.builtin_dictionaries.chinese_dictionary()`
- **Dutch**: `pynum2words.builtin_dictionaries.dutch_dictionary()`
- **English**: `pynum2words.builtin_dictionaries.english_dictionary()`
- **Finnish**: `pynum2words.builtin_dictionaries.finnish_dictionary()`
- **French**: `pynum2words.builtin_dictionaries.french_dictionary()`
- **German**: `pynum2words.builtin_dictionaries.german_dictionary()`
- **Greek**: `pynum2words.builtin_dictionaries.greek_dictionary()`
- **Hebrew**: `pynum2words.builtin_dictionaries.hebrew_dictionary()`
- **Hindi**: `pynum2words.builtin_dictionaries.hindi_dictionary()`
- **Hungarian**: `pynum2words.builtin_dictionaries.hungarian_dictionary()`
- **Italian**: `pynum2words.builtin_dictionaries.italian_dictionary()`
- **Japanese**: `pynum2words.builtin_dictionaries.japanese_dictionary()`
- **Kannada**: `pynum2words.builtin_dictionaries.kannada_dictionary()`
- **Korean**: `pynum2words.builtin_dictionaries.korean_dictionary()`
- **Malay**: `pynum2words.builtin_dictionaries.malay_dictionary()`
- **Oromo**: `pynum2words.builtin_dictionaries.oromo_dictionary()`
- **Persian**: `pynum2words.builtin_dictionaries.persian_dictionary()`
- **Portuguese**: `pynum2words.builtin_dictionaries.portuguese_dictionary()`
- **Romanian**: `pynum2words.builtin_dictionaries.romanian_dictionary()`
- **Russian**: `pynum2words.builtin_dictionaries.russian_dictionary()`
- **Spanish**: `pynum2words.builtin_dictionaries.spanish_dictionary()`
- **Swahili**: `pynum2words.builtin_dictionaries.swahili_dictionary()`
- **Tigrinya**: `pynum2words.builtin_dictionaries.tigrinya_dictionary()`
- **Turkish**: `pynum2words.builtin_dictionaries.turkish_dictionary()`
- **Ukrainian**: `pynum2words.builtin_dictionaries.ukrainian_dictionary()`
- **Urdu**: `pynum2words.builtin_dictionaries.urdu_dictionary()`
- **Zulu**: `pynum2words.builtin_dictionaries.zulu_dictionary()`

**N.B:-** You can also get more language dictionaries from [Here](https://github.com/birukbelihu/pynum2words-dictionaries)

If your language dictionary is not listed here you can create your own dictionary easily using this [guide](https://github.com/birukbelihu/pynum2words-language-packs?tab=readme-ov-file#how-to-create-a-language-dictionary)

---

## 📢 Social Media

- 📺 [YouTube: @pythondevs](https://youtube.com/@pythondevs?si=_CZxaEBwDkQEj4je)

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.