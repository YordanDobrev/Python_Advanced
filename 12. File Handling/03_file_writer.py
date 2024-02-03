import os

file = open("resources/my_first_file.txt", "w")
file.write("I just created my first file!\n")
file.write("Finally it is working\n")
file.write("Top work!!!\n")
file.close()

[print(el, end="") for el in open("resources/my_first_file.txt")]

with open("resources/my_next_file.txt", "a") as file:
    file.write("Another one ??")

[print(el, end="") for el in open("resources/my_next_file.txt")]