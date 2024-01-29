num = int(input())

matrix = [[x for x in input()] for element in range(num)]

ship_coordinates = []
fish_amount = 0

for row in matrix:
    for column in row:
        if "S" in column:
            ship_coordinates = [column.index("S"), row.index("S")]
            matrix[ship_coordinates[0]][ship_coordinates[1]] = "-"

print(ship_coordinates)
print(*matrix, sep="\n")

positions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
)

command = input()

while command != "collect the nets":

    for row_index in range(num):
        for col_index in range(num):

            for pos in positions:
                r = row_index + pos[0]
                c = col_index + pos[1]


    command = input()
