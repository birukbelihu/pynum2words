from pynum2words.pynum2words import PyNum2Words
from pynum2words.builtin_dictionaries import (afrikaans_dictionary,
                                              amharic_dictionary,
                                              english_dictionary)

# Initialize converters for each language

afrikaans_converter = PyNum2Words(afrikaans_dictionary(), auto_correct=True, format_number=False)
amharic_converter = PyNum2Words(amharic_dictionary(), auto_correct=True)
english_converter = PyNum2Words(english_dictionary(), auto_correct=True)

# Number to words(Afrikaans)
print(afrikaans_converter.number_to_words(41081510))  # Output: ሁለት መቶ አርባ ስምንት ሺህ ዘጠኝ መቶ አስር አራት
# Words to number(Afrikaans)
print(afrikaans_converter.words_to_number("twee Honderd Vyftig Sewe Duisend Vyf Honderd Dertig Drie"))  # Output: 257533

# Number to words(Amharic)
print(amharic_converter.number_to_words(248914))  # Output: ሁለት መቶ አርባ ስምንት ሺህ ዘጠኝ መቶ አስር አራት
# Words to number(Amharic)
print(amharic_converter.words_to_number("ሁለት መቶ ሀbምሳ ሰባት ሺህ አምስት መቶ ሰላሳ ሶቂስት"))  # Output: 257533

# Number to words(English)
print(english_converter.number_to_words(49285294))  # Output: Forty Nine Million Two Hundred Eighty Five Thousand Two Hundred Ninety Four
# Words to number(English)
print(english_converter.words_to_number("Two Hundred Foy fivr Thousand Eight Huvndjred Forty One"))  # Output: 241841