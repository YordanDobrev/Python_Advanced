first_player, second_player = input().split(", ")

maze = [list(input().split()) for element in range(6)]

player_one_rest = False
player_two_rest = False

while True:
    cords_one = input()

    # first player
    if not player_one_rest:
        player_one_cords = []

        for i in range(len(cords_one)):
            if cords_one[i].isdigit():
                player_one_cords.append((int(cords_one[i])))

        row, col = player_one_cords

        if maze[row][col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif maze[row][col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif maze[row][col] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            player_one_rest = True
        elif maze[row][col] == ".":
            pass
    else:
        player_one_rest = False

    cords_two = input()
    # second player
    if not player_two_rest:
        player_two_cords = []
        for i in range(len(cords_two)):
            if cords_two[i].isdigit():
                player_two_cords.append((int(cords_two[i])))

        row2, col2 = player_two_cords

        if maze[row2][col2] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif maze[row2][col2] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif maze[row2][col2] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            player_two_rest = True
        elif maze[row2][col2] == ".":
            pass
    else:
        player_two_rest = False
