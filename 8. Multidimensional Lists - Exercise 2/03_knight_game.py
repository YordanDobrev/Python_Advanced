board = int(input())

matrix = [[x for x in input()] for element in range(board)]

knight_removed = 0

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
while True:
    max_attacks = 0
    knight_max_pos = []

    for row_index in range(board):
        for col_index in range(board):
            if matrix[row_index][col_index] == "K":
                attacks = 0

                for pos in positions:
                    position_r = row_index + pos[0]
                    position_c = col_index + pos[1]

                    if 0 <= position_r < board and 0 <= position_c < board:
                        if matrix[position_r][position_c] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_max_pos = [row_index, col_index]

    if knight_max_pos:
        row, col = knight_max_pos
        matrix[row][col] = "0"
        knight_removed += 1
    else:
        break

print(knight_removed)
