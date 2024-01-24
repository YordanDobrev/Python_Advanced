num = int(input())

matrix = [[int(x) for x in input().split()] for element in range(num)]

command = input().split()

while command[0] != "END":
    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < num and 0 <= col < num):
        print("Invalid coordinates")
        command = input().split()
        continue

    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

    command = input().split()

[print(*index) for index in matrix]
