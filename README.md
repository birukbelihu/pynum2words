# pynum2words

![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/pynum2words)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/pynum2words)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/pynum2words)
[![PyPI Downloads](https://static.pepy.tech/badge/pynum2words)](https://pepy.tech/projects/pynum2words)

**pynum2words** is a Python package for converting numbers to their word representation and vice versa, using a built-in or custom dictionary.

---

## ✨ Features

- 🔧 Highly Customizable
- 🔢 Convert numbers to words without upper limit
- 🌍 Supports custom multilingual dictionaries (`.n2w`)
- 🚀 Support Comment On The Dictionaries(.n2w). 
- 🔁 Two-way conversion: number ➜ word and word ➜ number  
- 📦 Command Line & Python API support

---

## 📦 Installation

```
pip install pynum2words
```

You can also install pynum2words from source code. source code may not be stable, but it will have the latest features and bug fixes.

Clone The Repository:

```
git clone https://github.com/birukbelihu/pynum2words.git
```

Go Inside The Project Directory:

```
cd pynum2words
```

Install The Package:

```
pip install -e .
```

---

## Builtin Dictionaries

- **Amharic**: `pynum2words.builtin_dictionaries.amharic_dictionary()`
- **Arabic**: `pynum2words.builtin_dictionaries.arabic_dictionary()`
- **Chinese**: `pynum2words.builtin_dictionaries.chinese_dictionary()`
- **Dutch**: `pynum2words.builtin_dictionaries.dutch_dictionary()`
- **English**: `pynum2words.builtin_dictionaries.english_dictionary()`
- **French**: `pynum2words.builtin_dictionaries.french_dictionary()`
- **German**: `pynum2words.builtin_dictionaries.german_dictionary()`
- **Greek**: `pynum2words.builtin_dictionaries.greek_dictionary()`
- **Hindi**: `pynum2words.builtin_dictionaries.hindi_dictionary()`
- **Italian**: `pynum2words.builtin_dictionaries.italian_dictionary()`
- **Japanese**: `pynum2words.builtin_dictionaries.japanese_dictionary()`
- **Korean**: `pynum2words.builtin_dictionaries.korean_dictionary()`
- **Portuguese**: `pynum2words.builtin_dictionaries.portuguese_dictionary()`
- **Romanian**: `pynum2words.builtin_dictionaries.romanian_dictionary()`
- **Russian**: `pynum2words.builtin_dictionaries.russian_dictionary()`
- **Spanish**: `pynum2words.builtin_dictionaries.spanish_dictionary()`
- **Swahili**: `pynum2words.builtin_dictionaries.swahili_dictionary()`
- **Tigrinya**: `pynum2words.builtin_dictionaries.tigrinya_dictionary()`
- **Turkish**: `pynum2words.builtin_dictionaries.turkish_dictionary()`

**N.B:-** You Can Get More Language Dictionaries From [Here](https://github.com/birukbelihu/pynum2words-language-packs).

If Your Language Is Not Listed Here You Can Create Your Own Dictionary By Following This [Guide](https://github.com/birukbelihu/pynum2words-language-packs?tab=readme-ov-file#how-to-create-a-language-dictionary)

## 🧠 Example Usage

### CLI

```bash
# Convert number to words
pyn2w --number 12345
# Output: Twelve Thousand Three Hundred Forty Five

# Convert words to number with custom dictionary
pyn2w --word "አምስት" --dict dictionaries/amharic.n2w
# Output: 5
```

### Python

```python
from pynum2words.builtin_dictionaries import amharic_dictionary, english_dictionary
from pynum2words.pynum2words import PyNum2Words

# Initialize converters for each language
amharic = PyNum2Words(amharic_dictionary())
english = PyNum2Words(english_dictionary())

# Number to words
print(amharic.number_to_words(248914))  # Output: ሁለት መቶ አምስት አስር ሰባት ሺ አምስት መቶ ሦስት አስር ሦስት
# Words to number
print(amharic.words_to_number("ሁለት መቶ አርባ ስምንት ሺህ ዘጠኝ መቶ አስር አራት"))  # Output: 257533
```

---

## 📢 Social Media

- 📺 [YouTube: @pythondevs](https://youtube.com/@pythondevs?si=_CZxaEBwDkQEj4je)

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.