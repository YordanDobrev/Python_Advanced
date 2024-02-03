import os

the_file = open("resources/numbers.txt")

to_read = the_file.readlines()

total = 0

for i in to_read:
    total += int(i)

print(total)
