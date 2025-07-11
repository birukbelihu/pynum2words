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

dictionaries_file_path = "pynum2words/dictionaries/"

def get_dictionary_file_path(dictionary_name):
    return f"{dictionaries_file_path}{dictionary_name}.n2w"

def amharic_dictionary():
    return get_dictionary_file_path("amharic")

def arabic_dictionary():
    return get_dictionary_file_path("arabic")

def chinese_dictionary():
    return get_dictionary_file_path("chinese")

def english_dictionary():
    return get_dictionary_file_path("english")

def french_dictionary():
    return get_dictionary_file_path("french")

def german_dictionary():
    return get_dictionary_file_path("german")

def greek_dictionary():
    return get_dictionary_file_path("greek")

def hindi_dictionary():
    return get_dictionary_file_path("hindi")

def italian_dictionary():
    return get_dictionary_file_path("italian")

def japanese_dictionary():
    return get_dictionary_file_path("japanese")

def korean_dictionary():
    return get_dictionary_file_path("korean")

def portuguese_dictionary():
    return get_dictionary_file_path("portuguese")

def romanian_dictionary():
    return get_dictionary_file_path("romanian")

def russian_dictionary():
    return get_dictionary_file_path("russian")

def spanish_dictionary():
    return get_dictionary_file_path("spanish")

def swahili_dictionary():
    return get_dictionary_file_path("swahili")

def tigrinya_dictionary():
    return get_dictionary_file_path("tigrinya")

def turkish_dictionary():
    return get_dictionary_file_path("turkish")
