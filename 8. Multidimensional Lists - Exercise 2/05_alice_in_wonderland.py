SIZE = int(input())

wonderland = [list(x for x in input().split()) for element in range(SIZE)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

alice_position = []
starting_position = []
for row in range(SIZE):
    for col in range(SIZE):
        if wonderland[row][col] == "A":
            alice_position = [row, col]
            starting_position = [row, col]
            wonderland[row][col] = "*"
tea_bags = 0
fail = False

while True:
    command = input()
    al_row, al_col = alice_position

    al_row += directions[command][0]
    al_col += directions[command][1]

    try:
        if command == "up":
            if wonderland[al_row][al_col].isdigit():
                tea_bags += int(wonderland[al_row][al_col])
                wonderland[alice_position[0]][alice_position[1]] = "*"  # check later
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                if tea_bags >= 10:
                    break
            elif wonderland[al_row][al_col] == ".":
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                continue
            elif wonderland[al_row][al_col] == "*":
                alice_position = [al_row, al_col]
                continue
            elif wonderland[al_row][al_col] == "R":
                wonderland[al_row][al_col] = "*"
                fail = True
                break

        elif command == "down":
            if wonderland[al_row][al_col].isdigit():
                tea_bags += int(wonderland[al_row][al_col])
                wonderland[alice_position[0]][alice_position[1]] = "*"  # check later
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                if tea_bags >= 10:
                    break
            elif wonderland[al_row][al_col] == ".":
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                continue
            elif wonderland[al_row][al_col] == "*":
                alice_position = [al_row, al_col]
                continue
            elif wonderland[al_row][al_col] == "R":
                wonderland[al_row][al_col] = "*"
                fail = True
                break
        elif command == "left":
            if wonderland[al_row][al_col].isdigit():
                tea_bags += int(wonderland[al_row][al_col])
                wonderland[alice_position[0]][alice_position[1]] = "*"  # check later
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                if tea_bags >= 10:
                    break
            elif wonderland[al_row][al_col] == ".":
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                continue
            elif wonderland[al_row][al_col] == "*":
                alice_position = [al_row, al_col]
                continue
            elif wonderland[al_row][al_col] == "R":
                wonderland[al_row][al_col] = "*"
                fail = True
                break
        elif command == "right":
            if wonderland[al_row][al_col].isdigit():
                tea_bags += int(wonderland[al_row][al_col])
                wonderland[alice_position[0]][alice_position[1]] = "*"  # check later
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                if tea_bags >= 10:
                    break
            elif wonderland[al_row][al_col] == ".":
                alice_position = [al_row, al_col]
                wonderland[al_row][al_col] = "*"
                continue
            elif wonderland[al_row][al_col] == "*":
                alice_position = [al_row, al_col]
                continue
            elif wonderland[al_row][al_col] == "R":
                wonderland[al_row][al_col] = "*"
                fail = True
                break
    except IndexError:
        fail = True
        break

if not fail:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for index in wonderland:
    print(' '.join(index))
