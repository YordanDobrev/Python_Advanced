size = int(input())

matrix = []
submarine = []
battlecruisers = 0
mines = 0

for line in range(size):
    token = list(input())
    if "S" in token:
        submarine = [line, token.index("S")]
    if "C" in token:
        battlecruisers += token.count("C")
    matrix.append(token)

matrix[submarine[0]][submarine[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    row, col = submarine
    next_row = row + directions[command][0]
    next_col = col + directions[command][1]

    symbol = matrix[next_row][next_col]

    if symbol == "C":
        matrix[next_row][next_col] = "-"
        battlecruisers -= 1
        if not battlecruisers:
            matrix[next_row][next_col] = "S"
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    elif symbol == "*":
        mines -= 1
        matrix[next_row][next_col] = "-"
        if mines == 0:
            matrix[next_row][next_col] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!")
            break
    elif symbol == "-":
        pass

    submarine = [next_row, next_col]

[print(*el, sep="") for el in matrix]
