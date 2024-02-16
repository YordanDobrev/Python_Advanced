def the_move(action, all_directions, latest_position, the_matrix):
    row, col = latest_position
    row += all_directions[action][0]
    col += all_directions[action][1]

    if row < 0 and row >= len(the_matrix) and col < 0 and col >= len(the_matrix[0]):
        return "NEXT"
    elif matrix[row][col] == "O":
        return "NEXT"

    return [row, col]


the_r, the_c = [int(el) for el in input().split()]

matrix = []
position = []
moves = 0
touched = 0

for i in range(the_r):
    line = input().split()
    if "B" in line:
        position = [i, int(line.index("B"))]
    matrix.append(line)

matrix[position[0]][position[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "Finish":
    if touched == 3:
        break
    next_move = the_move(command, directions, position, matrix)

    if next_move == "NEXT":
        command = input()
        continue

    row, col = next_move
    symbol = matrix[row][col]

    if symbol == "-":
        moves += 1
    elif symbol == "P":
        moves += 1
        touched += 1
        matrix[row][col] = "-"

    position = [row, col]
    command = input()

print("Game over!")
print(f"Touched opponents: {touched} Moves made: {moves}")