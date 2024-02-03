import os

file = "resources/text.txt"

to_open = (open(file))

current_file = to_open.readlines()

[print(el, end="") for el in current_file]
