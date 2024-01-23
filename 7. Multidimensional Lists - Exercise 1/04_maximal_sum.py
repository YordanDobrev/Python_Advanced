row, column = [int(num) for num in input().split()]

matrix = [[int(x) for x in input().split()] for element in range(row)]

max_summ = float("-inf")
max_matrix = []

for row_index in range(row - 2):

    for col_index in range(column - 2):
        sub_matrix = []
        sub_matrix.append(
            [matrix[row_index][col_index], matrix[row_index][col_index + 1], matrix[row_index][col_index + 2]])
        sub_matrix.append(
            [matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1], matrix[row_index + 1][
                col_index + 2]])
        sub_matrix.append(
            [matrix[row_index + 2][col_index], matrix[row_index + 2][col_index + 1], matrix[row_index + 2][
                col_index + 2]])

        total = sum([sum(y) for y in sub_matrix])

        if total > max_summ:
            max_summ = total
            max_matrix = sub_matrix

print(f"Sum = {max_summ}")

for index in max_matrix:
    print(*index)
