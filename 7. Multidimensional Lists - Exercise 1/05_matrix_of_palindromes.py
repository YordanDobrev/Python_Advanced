rows, columns = [int(num) for num in input().split()]

first_letter = ord("a")

matrix = []

for row_index in range(first_letter, first_letter + rows):
    sub_list = []
    for col_index in range(row_index, row_index + columns):
        sub_list.append(chr(row_index) + chr(col_index) + chr(row_index))

    matrix.append(sub_list)

for index in matrix:
    print(" ".join(index))
