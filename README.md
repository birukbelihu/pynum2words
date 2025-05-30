# pynum2words

![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/pynum2words)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/pynum2words)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/pynum2words)

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

```bash
pip install pynum2words
```

---

## Builtin Dictionaries

- **Amharic**: `pynum2words.builtin_dictionaries.amharic_dictionary()`
- **Tigrinya**: `pynum2words.builtin_dictionaries.tigrinya_dictionary()`
- **English**: `pynum2words.builtin_dictionaries.english_dictionary()`
- **Portuguese**: `pynum2words.builtin_dictionaries.portuguese_dictionary()`
- **Russian**: `pynum2words.builtin_dictionaries.russian_dictionary()`

**N.B:-** You Can Get More Language Packs From [Here](https://github.com/birukbelihu/pynum2words-language-packs).

More dictionaries can be added by creating a `.n2w` file with the required format.

## 🧠 Example Usage

### Python

```python
from pynum2words.builtin_dictionaries import amharic_dictionary, english_dictionary
from pynum2words.pynum2words import PyNum2Words

# Initialize converters for each language
amharic = PyNum2Words(amharic_dictionary())
english = PyNum2Words(english_dictionary())

# Number to words
print(amharic.number_to_words(257533))  # Output: ሁለት መቶ አምስት አስር ሰባት ሺ አምስት መቶ ሦስት አስር ሦስት
print(english.number_to_words(257533))  # Output: two hundred fifty-seven thousand five hundred thirty-three

# Words to number
print(amharic.words_to_number("ሁለት መቶ ሀምሳ ሰባት ሺህ አምስት መቶ ሰላሳ ሶስት"))  # Output: 257533
print(english.words_to_number("two hundred fifty seven thousand five hundred thirty three"))  # Output: 257533

```

### CLI

```bash
# Convert number to words
pyn2w --number 12345
# Output: Twelve Thousand Three Hundred Forty Five

# Convert words to number with custom dictionary
pyn2w --word "አምስት" --dict dictionaries/amharic.n2w
# Output: 5
```

---

## 📢 Social Media

- 📺 [YouTube: @pythondevs](https://youtube.com/@pythondevs?si=_CZxaEBwDkQEj4je)  
- 💬 [Telegram: @pythondevstutorials](https://t.me/pythondevstutorials)

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.