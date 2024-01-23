nums = int(input())

matrix = [[int(el) for el in input().split()] for element in range(nums)]

primary_diagonal = [matrix[element][element] for element in range(nums)]
secondary_diagonal = []

for row_index in range(len(matrix)):
    current_index = nums - row_index - 1
    secondary_diagonal.append(matrix[row_index][current_index])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))