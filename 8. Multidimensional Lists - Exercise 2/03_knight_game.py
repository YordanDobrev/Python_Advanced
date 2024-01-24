board = int(input())

matrix = [[x for x in input()] for element in range(board)]

knight_score = 0

positions = (
    (-2, -1),  # up -2, left -1
    (-1, -2),  # up -1, left -2
    (-2, 1),  # up 2, right 1
    (-1, 2),  # up -1, right 2
    (1, -2),  # down 1, left -2
    (2, -1),  # down 2, left -1
    (1, 2),  # down 1, right 2
    (2, 1),  # down 2, right 1
)





[print(*index, sep="") for index in matrix]
