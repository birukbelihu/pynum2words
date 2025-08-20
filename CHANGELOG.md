## [1.3.8] - 2025-08-10 
 
### Fixed 
- Critical bug when the number exceeds the maximum number defined in the specific dictionary. 
 
### Added 
- Autocorrection feature for words-to-number conversion that suggests corrections for typos based on the provided dictionary. Enable it by setting the `auto_correct` parameter to `True`. 
 
**Example:**

```python 
from pynum2words.dictionaries import english_dictionary
from pynum2words.pynum2words import PyNum2Words

english_converter = PyNum2Words(english_dictionary(), auto_correct=True)

# Words to number (English) 
print(
  english_converter.words_to_number("Two Hungdred Forty One Tbhousand Ebight Hunvdred Forty One"))  # Output: 241841 
 ```
 
- Added 12 new language dictionaries: 
  - Czech: `pynum2words.builtin_dictionaries.czech_dictionary()` 
  - Slovak: `pynum2words.builtin_dictionaries.slovak_dictionary()` 
  - Swedish: `pynum2words.builtin_dictionaries.swedish_dictionary()` 
  - Norwegian: `pynum2words.builtin_dictionaries.norwegian_dictionary()` 
  - Danish: `pynum2words.builtin_dictionaries.danish_dictionary()` 
  - Filipino / Tagalog: `pynum2words.builtin_dictionaries.filipino_dictionary()` 
  - Nepali: `pynum2words.builtin_dictionaries.nepali_dictionary()` 
  - Somali: `pynum2words.builtin_dictionaries.somali_dictionary()` 
  - Khmer: `pynum2words.builtin_dictionaries.khmer_dictionary()` 
  - Lao: `pynum2words.builtin_dictionaries.lao_dictionary()` 
  - Thai: `pynum2words.builtin_dictionaries.thai_dictionary()` 
  - Vietnamese: `pynum2words.builtin_dictionaries.vietnamese_dictionary()` 
 
  
- Added a number formatter option for words to number conversion. Enabled by default, but you can disable by setting `format_number` to `False`. 
 
  **Example:**

```python 
from pynum2words.dictionaries import english_dictionary
from pynum2words.pynum2words import PyNum2Words

english_converter = PyNum2Words(english_dictionary(), format_number=False)

# Words to number (English) 
print(english_converter.words_to_number("Two Hundred Forty One Thousand Eight Hundred Forty One"))  # Output: 241841 
```

## [1.4.0] - 2025-08-20

### Fixed
- Fixes bug with the convert hundred function
- Fixes issue with some dictionaries.

### Changes
- Migrated to more modern & flexible console text formatter library([**pyglowx**](https://github.com/birukbelihu/pyglowx)) for the pyn2w CLI.
