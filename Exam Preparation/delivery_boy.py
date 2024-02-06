class InvalidIndex(Exception):
    pass


ROW, COLUMN = [int(element) for element in input().split()]

matrix = []

for current_row in range(ROW):
    temp_list = []
    action = list(input())
    for current_col in range(COLUMN):
        temp_list.append(action[current_col])
    matrix.append(temp_list)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

boy_coordinates = []

for row in range(ROW):
    for col in range(COLUMN):
        if "B" in matrix[row][col]:
            boy_coordinates.append(row)
            boy_coordinates.append(col)
            break

command = input()
latest_cords = boy_coordinates

while True:
    boy_row, boy_col = latest_cords
    current_coordinates = []
    try:
        if command == "up":
            boy_row = boy_row + directions[command][0]
            boy_col = boy_col + directions[command][1]

        elif command == "down":
            boy_row = boy_row + directions[command][0]
            boy_col = boy_col + directions[command][1]

        elif command == "left":
            boy_row = boy_row + directions[command][0]
            boy_col = boy_col + directions[command][1]

        elif command == "right":
            boy_row = boy_row + directions[command][0]
            boy_col = boy_col + directions[command][1]

        current_position = matrix[boy_row][boy_col]

        if current_position == "-":
            matrix[boy_row][boy_col] = "."
            current_position = matrix[boy_row][boy_col]
        elif current_position == "P":
            matrix[boy_row][boy_col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")
        elif current_position == "A":
            matrix[boy_row][boy_col] = "P"
            print("Pizza is delivered on time! Next order...")
            break
        elif current_position == "*":
            command = input()
            continue

        latest_cords = [boy_row, boy_col]
    except IndexError:
        print("The delivery is late. Order is canceled.")
        matrix[boy_coordinates[0]][boy_coordinates[1]] = " "
        break
    command = input()

for index in matrix:
    print("".join(index))