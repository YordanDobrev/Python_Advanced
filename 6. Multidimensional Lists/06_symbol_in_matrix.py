rows_to_include = int(input())

the_matrix = []

for i in range(rows_to_include):
    current_row = [i for i in input()]
    the_matrix.append(current_row)

searched_element = input()

for row_index in range(len(the_matrix)):
    for col_index in range(len(the_matrix)):
        current_element = the_matrix[row_index][col_index]
        if searched_element == the_matrix[row_index][col_index]:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searched_element} does not occur in the matrix")
