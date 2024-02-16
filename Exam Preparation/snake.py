size = int(input())

matrix = []
lair = []
snake_position = []
food = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for line in range(size):
    token = list(input())
    if "S" in token:
        snake_position = [line, token.index("S")]
    if "B" in token:
        lair.append([line, token.index("B")])
    matrix.append(token)

matrix[snake_position[0]][snake_position[1]] = "."
fail = False

while food != 10:
    command = input()

    try:
        the_row, the_col = snake_position
        the_row = the_row + directions[command][0]
        the_col = the_col + directions[command][1]

        symbol = matrix[the_row][the_col]

        if symbol == "*":
            food += 1
            matrix[the_row][the_col] = "."
        elif symbol == "-":
            matrix[the_row][the_col] = "."
        elif symbol == "B":
            for el in lair:
                r, c = el
                if r == the_row and c == the_col:
                    lair.remove(el)
            matrix[the_row][the_col] = "."
            snake_position = lair[0]
            matrix[snake_position[0]][snake_position[1]] = "."
            continue

        snake_position = [the_row, the_col]

    except IndexError:
        fail = True
        break

if fail:
    print(f"Game over!")

if food == 10:
    print("You won! You fed the snake.")
    matrix[snake_position[0]][snake_position[1]] = "S"

print(f"Food eaten: {food}")

[print(*line, sep="") for line in matrix]