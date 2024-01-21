rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    current_line = [int(element) for element in input().split()]
    matrix.append(current_line)

for col_index in range(columns):
    temp_total = 0

    for row_index in range(rows):
        number = matrix[row_index][col_index]
        temp_total += number

    print(temp_total)
