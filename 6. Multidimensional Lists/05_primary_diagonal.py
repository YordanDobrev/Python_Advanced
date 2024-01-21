num = int(input())

# square_matrix = []
total = 0

for index in range(num):
    current_line = [int(x) for x in input().split()]
    # square_matrix.append(current_line)
    total += current_line[index]

# print(square_matrix)
print(total)
