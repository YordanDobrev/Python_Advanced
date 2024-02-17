size = int(input())

matrix = []
jet_position = []
enemies = 0
armor = 300

for i in range(size):
    line = list(input())
    if "J" in line:
        jet_position = [i, line.index("J")]
    if "E" in line:
        enemies += line.count("E")
    matrix.append(line)

matrix[jet_position[0]][jet_position[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while True:
    if not armor:
        break
    row, col = jet_position
    row += directions[command][0]
    col += directions[command][1]
    symbol = matrix[row][col]

    if symbol == "-":
        pass
    elif symbol == "E":
        enemies -= 1
        matrix[row][col] = "-"
        if not enemies:
            jet_position = [row, col]
            matrix[row][col] = "J"
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        armor -= 100
        if not armor:
            jet_position = [row, col]
            matrix[row][col] = "J"
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
            break
    elif symbol == "R":
        armor = 300
        matrix[row][col] = "-"

    jet_position = [row, col]
    command = input()

for el in matrix:
    print(*el, sep="")
