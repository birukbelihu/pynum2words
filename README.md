# pynum2words

![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/pynum2words)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/pynum2words)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/pynum2words)
![GitHub license](https://img.shields.io/github/license/BirukBelihu/pynum2words)

**pynum2words** is a Python package for converting numbers to their word representation and vice versa, using a built-in or custom dictionary.

---

## ✨ Features

- 🔧 Highly Customizable  
- 🔢 Convert numbers to words without upper limit  
- 🌍 Supports custom multilingual dictionaries (`.n2w`)  
- 🔁 Two-way conversion: number ➜ word and word ➜ number  
- 📦 CLI & Python API support

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

More dictionaries can be added by creating a `.n2w` file with the required format.

## 🧠 Example Usage

### Python

```python
from pynum2words import PyNum2Words
from pynum2words.builtin_dictionaries import amharic_dictionary

# Use built-in English dictionary
converter = PyNum2Words(amharic_dictionary())
print(converter.number_to_words(25))         # Twenty Five
print(converter.words_to_number("Twenty"))   # 20

# Use a custom Amharic dictionary
converter = PyNum2Words()
print(converter.number_to_words(5)) # አምስት
```

### CLI

```bash
# Convert number to words
pyn2w 12345
# Output: Twelve Thousand Three Hundred Forty Five

# Convert words to number with custom dictionary
pyn2w አምስት --dictionary dictionaries/amharic.n2w
# Output: 5
```

---

## 📢 Social Media

- 📺 [YouTube: @pythondevs](https://youtube.com/@pythondevs?si=_CZxaEBwDkQEj4je)  
- 💬 [Telegram: @pythondevstutorials](https://t.me/pythondevstutorials)

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.