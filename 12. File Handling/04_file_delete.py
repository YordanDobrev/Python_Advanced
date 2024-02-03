import os

path = os.path.join("resources/file_to_delete.txt")

with open(path) as file:
    file.flush()