rows, columns = [int(element) for element in input().split(", ")]

matrx = []

for _ in range(rows):
    current_line = [int(x) for x in input().split(", ")]
    matrx.append(current_line)

max_num = float('-inf')
max_matrix = []

for row_index in range(rows - 1):

    for col_index in range(columns - 1):
        sub_matrix = []

        main = matrx[row_index][col_index]
        right = matrx[row_index][col_index + 1]
        bottom = matrx[row_index + 1][col_index]
        right_diagonal = matrx[row_index + 1][col_index + 1]

        current_total = main + right + bottom + right_diagonal
        sub_matrix.append([main, right])
        sub_matrix.append([bottom, right_diagonal])

        if current_total > max_num:
            max_num = current_total
            max_matrix = sub_matrix

for index in range(2):
    print(*max_matrix[index], sep=" ")

print(max_num)
