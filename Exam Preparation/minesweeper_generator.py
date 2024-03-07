size = int(input())
number_of_bombs = int(input())

matrix = [[0 for num in range(size)] for el in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}

for bomb in range(number_of_bombs):
    current_line = input().split(", ")
    row = int(current_line[0][1])
    col = int(current_line[1][0])
    matrix[row][col] = "*"
    current_bomb = [row, col]

    for key, value in directions.items():
        row_direction = int(row) + int(value[0])
        col_direction = int(col) + int(value[1])
        try:
            if row_direction < 0 or row_direction >= len(matrix):
                continue
            if col_direction < 0 or col_direction >= len(matrix):
                continue

            matrix[row_direction][col_direction] += 1
        except:
            continue

for el in matrix:
    for current_line in el:
        print(current_line, end=" ")
    print()
