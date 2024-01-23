rows, columns = [int(nums) for nums in input().split()]

matrix = [[current_element for current_element in input().split()] for elements in range(rows)]

command = input()

while command != "END":
    if "swap" not in command:
        print(f"Invalid input!")
        command = input()
        continue

    current_line = command.split()
    action = current_line[0]
    row1 = int(current_line[1])
    col1 = int(current_line[2])
    row2 = int(current_line[3])
    col2 = int(current_line[4])

    if 0 <= row1 < len(matrix) or 0 <= row2 < len(matrix) or 0 <= col1 < len(matrix) or 0 <= col2 < len(matrix):
        temp_swap = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = temp_swap

        for index in matrix:
            print(" ".join(index))

        command = input()

    else:
        print(f"Invalid input!")
        command = input()
        continue
