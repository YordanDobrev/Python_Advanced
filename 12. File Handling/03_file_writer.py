import os

file = open("my_first_file.txt", "w")
file.write("I just created my first file!\n")
file.write("Finally it is working\n")
file.write("Top work!!!\n")
file.close()

[print(el, end="") for el in open("my_first_file.txt")]
