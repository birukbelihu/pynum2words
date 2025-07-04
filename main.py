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

from pynum2words.builtin_dictionaries import amharic_dictionary, english_dictionary
from pynum2words.pynum2words import PyNum2Words

# Initialize converters for each language
amharic = PyNum2Words(amharic_dictionary())
english = PyNum2Words(english_dictionary())

# Number to words
print(amharic.number_to_words(248914))  # Output: ሁለት መቶ አምስት አስር ሰባት ሺ አምስት መቶ ሦስት አስር ሦስት
# Words to number
print(amharic.words_to_number("ሁለት መቶ ሀምሳ ሰባት ሺህ አምስት መቶ ሰላሳ ሶስት"))  # Output: 257533