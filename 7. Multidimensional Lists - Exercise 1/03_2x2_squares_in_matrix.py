rows, columns = [int(x) for x in input().split()]

matrix = [[current_element for current_element in input().split()] for element in range(rows)]

squares = 0

for current_row in range(rows - 1):
    for current_column in range(columns - 1):
        main = matrix[current_row][current_column]
        bottom = matrix[current_row + 1][current_column]
        right = matrix[current_row][current_column + 1]
        diagonal = matrix[current_row + 1][current_column + 1]

        if main == bottom and main == right and main == diagonal:
            squares += 1

print(squares)
