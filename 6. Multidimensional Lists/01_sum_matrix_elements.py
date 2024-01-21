rows, columns = [int(x) for x in input().split(", ")]

matrix_elements = []
total = 0

for _ in range(rows):
    action = [int(element) for element in input().split(", ")]
    total += sum(action)
    matrix_elements.append(action)

print(total)
print(matrix_elements)
