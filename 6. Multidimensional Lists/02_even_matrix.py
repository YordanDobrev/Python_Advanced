lines = int(input())

even_matrix = []

for _ in range(lines):
    current_line = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    even_matrix.append(current_line)

print(even_matrix)
