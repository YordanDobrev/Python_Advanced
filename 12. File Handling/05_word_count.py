import os
import re

path_words = os.path.join("resources", "words.txt")
path_input = os.path.join("resources", "input.txt")
path_output = os.path.join("resources", "output.txt")

with open(path_words) as searched_words:
    text = searched_words.read()
    the_list = [el.lower() for el in text.split()]

with open(path_input) as the_input:
    lines = the_input.read().lower()

words_counter = {}

for word in the_list:
    pattern = re.compile(rf"\b{word}\b")
    the_used_patern = re.findall(pattern, lines)
    words_counter[word] = the_used_patern.count(word)

some_sort = sorted(words_counter.items(), key=lambda kvp: -kvp[1])

for key, value in some_sort:
    print(f"{key} - {value}")
    with open(path_output, "a") as new_file:
        new_file.write(f"{key} - {value}\n")


