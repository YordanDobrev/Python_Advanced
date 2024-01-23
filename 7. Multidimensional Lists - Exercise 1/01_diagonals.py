nums = int(input())

matrix = []

for _ in range(nums):
    current_element = input().split(", ")
    matrix.append(current_element)

primary_diagonal = [int(matrix[right][right]) for right in range(len(matrix))]
secondary_diagonal = []

for row in range(len(matrix)):
    diagonal_index = nums - row - 1
    secondary_diagonal.append(int(matrix[row][diagonal_index]))

formated_primary = [str(x) for x in primary_diagonal]
secondary_primary = [str(x) for x in secondary_diagonal]

print(f"Primary diagonal: {', '.join(formated_primary)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(secondary_primary)}. Sum: {sum(secondary_diagonal)}")

