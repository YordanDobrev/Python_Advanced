line = int(input())

flat_matrix = []

for _ in range(line):
    row = [int(element) for element in input().split(", ")]
    flat_matrix.extend(row)

print(flat_matrix)
