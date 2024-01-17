elements = int(input())

periodic_table = set()

for _ in range(elements):
    action = input().split()

    for i in action:
        periodic_table.add(i)

print(*periodic_table, sep="\n")
