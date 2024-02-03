import os

path = os.path.join("resources", "file_to_delete.txt")

try:
    os.remove(path)
    print("File Deleted")
except FileNotFoundError:
    print("File not found !!!")
