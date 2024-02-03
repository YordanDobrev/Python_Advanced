from string import punctuation

with open("resources/text_even_lines.txt", "r") as base_file:
    file = base_file.readlines()

output_file = open("resources/line_numbers_output.txt", "a")

for current_row in range(len(file)):
    letters = 0
    marks = 0
    for index in file[current_row]:
        if index.isalpha():
            letters += 1
        elif index in punctuation:
            marks += 1

    output_file.write(f"Line {current_row + 1}: {file[current_row][:-1]} ({letters})({marks})\n")

output_file.close()
