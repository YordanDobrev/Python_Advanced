from collections import deque

SIZE = int(input())


def movement(r, c, path):
    if path == "up":
        r += directions[action][0]
        c += directions[action][1]
    elif path == "down":
        r += directions[action][0]
        c += directions[action][1]
    elif path == "left":
        r += directions[action][0]
        c += directions[action][1]
    elif path == "right":
        r += directions[action][0]
        c += directions[action][1]

    return r, c


commands = input().split(", ")
field = [list(input()) for elem in range(SIZE)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

squirrel_cords = []
hazelnuts = 0
trapped = False
out_of_field = False

for i in range(SIZE):
    if "s" in field[i]:
        squirrel_cords = [i, field[i].index("s")]
        field[i][field[i].index("s")] = "*"
        break

for action in commands:
    the_row, the_col = squirrel_cords

    try:
        row, col = movement(the_row, the_col, action)

        if field[row][col] == "h":
            hazelnuts += 1
            if hazelnuts == 3:
                break
            field[row][col] = "*"
            squirrel_cords = [row, col]

        elif field[row][col] == "*":
            squirrel_cords = [row, col]
            continue
        elif field[row][col] == "t":
            trapped = True
            break
    except IndexError:
        out_of_field = True
        break

if out_of_field:
    print("The squirrel is out of the field.")
elif trapped:
    print("Unfortunately, the squirrel stepped on a trap...")
elif hazelnuts <= 2:
    print("There are more hazelnuts to collect.")
elif hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {hazelnuts}")
