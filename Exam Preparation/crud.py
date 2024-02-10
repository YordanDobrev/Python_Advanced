def create(current_direction, r, c, value_to_use):
    rows = directions[current_direction][0] + r
    cols = directions[current_direction][1] + c

    if matrix[rows][cols] == ".":
        matrix[rows][cols] = value_to_use

    return [rows, cols]


def update(current_direction, r, c, value_to_use):
    rows = directions[current_direction][0] + r
    cols = directions[current_direction][1] + c

    if matrix[rows][cols].isdigit() or matrix[rows][cols].isalpha():
        matrix[rows][cols] = value_to_use

    return [rows, cols]


def delete(current_direction, r, c):
    rows = directions[current_direction][0] + r
    cols = directions[current_direction][1] + c

    if matrix[rows][cols].isdigit() or matrix[rows][cols].isalpha():
        matrix[rows][cols] = "."

    return [rows, cols]


def read(current_direction, r, c):
    rows = directions[current_direction][0] + r
    cols = directions[current_direction][1] + c

    if matrix[rows][cols].isdigit() or matrix[rows][cols].isalpha():
        print(matrix[rows][cols])
        return [rows, cols]
    return [rows, cols]


SIZE = 6

matrix = [list(input().split()) for el in range(SIZE)]

crds = input()
start_coordinates = []

for i in range(len(crds)):
    if crds[i].isdigit():
        start_coordinates.append(int(crds[i]))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()
latest_cords = start_coordinates

while command != "Stop":
    current_command = command.split(", ")
    action = current_command[0]
    direction = current_command[1]
    row, col = latest_cords

    if action == "Create":
        value = current_command[2]
        latest_cords = create(direction, row, col, value)
    elif action == "Update":
        value = current_command[2]
        latest_cords = update(direction, row, col, value)

    elif action == "Delete":
        latest_cords = delete(direction, row, col)

    elif action == "Read":
        latest_cords = read(direction, row, col)

    command = input()

for row in range(SIZE):
    for col in range(SIZE):
        print(matrix[row][col], end=" ")
    print()
