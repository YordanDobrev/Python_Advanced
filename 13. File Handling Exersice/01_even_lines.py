symbols = ("-", ",", ".", "!", "?")

with open("resources/text_even_lines.txt", "r") as file:
    text = file.readlines()

for row in range(0, len(text), 2):

    for current_symbol in symbols:
        if current_symbol in text[row]:
            text[row] = text[row].replace(current_symbol, "@")

    print(*text[row].split()[::-1])
