def movement(directions, command, matrix, r, c):
    path = directions[command]

    next_row = r + path[0]
    next_col = c + path[1]

    if next_row < 0:
        next_row = len(matrix) - 1
    elif next_row >= len(matrix):
        next_row = 0

    if next_col < 0:
        next_col = len(matrix) - 1
    elif next_col >= len(matrix):
        next_col = 0

    return next_row, next_col


size = int(input())

matrix = []
ship_cords = []

for index in range(size):
    line = list(input())

    if "S" in line:
        ship_cords = [index, line.index("S")]
        line[ship_cords[1]] = "-"
    matrix.append(line)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

fish = 0

command = input()
latest_ship_cords = ship_cords

while command != "collect the nets":
    r, c = latest_ship_cords
    row, col = movement(directions, command, matrix, r, c)
    latest_ship_cords = [row, col]
    next_symbol = matrix[row][col]

    if next_symbol.isdigit():
        fish += int(matrix[row][col])
        matrix[row][col] = "-"
    elif next_symbol == "W":
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
            f"Last coordinates of the ship: [{','.join([str(el)for el in latest_ship_cords])}]")
        exit()
    command = input()

matrix[latest_ship_cords[0]][latest_ship_cords[1]] = "S"

if fish >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish} tons of fish more.")

if fish > 0:
    print(f"Amount of fish caught: {fish} tons.")

for i in matrix:
    print(''.join(i))
