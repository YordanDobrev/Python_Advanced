def valid_cords(row_to_check, col_to_check):
    valid = True
    if 0 > row_to_check > rows:
        valid = False
    if 0 > col_to_check > cols:
        valid = False
    return valid


rows, cols = [int(i) for i in input().split(",")]

matrix = []

for row in range(rows):
    matrix.append(list(input()))

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

mouse_cords = []
cheese = 0
trap = False

for r in range(rows):
    for c in range(cols):
        if "M" in matrix[r][c]:
            mouse_cords = [r, c]
            matrix[r][c] = "*"
        if "C" in matrix[r][c]:
            cheese += 1

command = input()
latest_mouse_cords = mouse_cords
previous_cords = []

while command != "danger":

    try:
        m_row, m_col = latest_mouse_cords
        previous_cords = latest_mouse_cords
        if command == "up":
            m_row += directions[command][0]
            m_col += directions[command][1]

        elif command == "down":
            m_row += directions[command][0]
            m_col += directions[command][1]

        elif command == "right":
            m_row += directions[command][0]
            m_col += directions[command][1]

        elif command == "left":
            m_row += directions[command][0]
            m_col += directions[command][1]

        if valid_cords(m_row, m_col):
            latest_mouse_cords = [m_row, m_col]
            current_symbol = matrix[m_row][m_col]

            if current_symbol == "C":
                matrix[m_row][m_col] = "*"
                cheese -= 1
                if cheese == 0:
                    matrix[m_row][m_col] = "M"
                    break
            elif current_symbol == "*":
                pass
            elif current_symbol == "@":
                latest_mouse_cords = previous_cords
            elif current_symbol == "T":
                matrix[m_row][m_col] = "M"
                trap = True
                break
        command = input()

    except IndexError:
        print("No more cheese for tonight!")
        matrix[previous_cords[0]][previous_cords[1]] = "M"
        break

if cheese == 0:
    print("Happy mouse! All the cheese is eaten, good night!")
elif trap:
    print("Mouse is trapped!")
elif command == "danger":
    print("Mouse will come back later!")

for i in matrix:
    print(''.join(i))
