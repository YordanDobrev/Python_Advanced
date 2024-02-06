number = int(input())

matrix = [list(input().split()) for element in range(number)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

bunny_position = []

max_eggs = 0
direction = float("-inf")
best_path = ""

for row in range(number):
    for col in range(number):
        if "B" in matrix[row][col]:
            bunny_position = [row, col]

for key, value in directions.items():
    bunny_row, bunny_col = [bunny_position[0] + value[0], bunny_position[1] + value[1]]

    current_route = []
    eggs = 0

    while 0 <= bunny_row < number and 0 <= bunny_col < number:
        if matrix[bunny_row][bunny_col] == "X":
            break
        eggs += int(matrix[bunny_row][bunny_col])
        current_route.append([bunny_row, bunny_col])

        bunny_row += value[0]
        bunny_col += value[1]

    if eggs >= max_eggs:
        max_eggs = eggs
        direction = current_route
        best_path = key

print(best_path)
print(*direction, sep="\n")
print(max_eggs)
