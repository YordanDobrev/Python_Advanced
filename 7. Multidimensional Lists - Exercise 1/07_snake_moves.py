from collections import deque

rows, columns = [int(nums) for nums in input().split()]
line = list(input())

matrix_copy = deque(line)

for row in range(rows):
    while len(matrix_copy) < columns:
        matrix_copy.extend(line)

    if row % 2 == 0:
        print(*[matrix_copy.popleft() for el in range(columns)], sep="")
    else:
        print(*[matrix_copy.popleft() for el in range(columns)][::-1], sep="")
