lines = int(input())

odd_num = set()
even_num = set()

for index in range(1, lines + 1):
    name = input()

    current_name = int(sum([ord(x) for x in name]) / index)

    if current_name % 2 == 0:
        even_num.add(current_name)
    else:
        odd_num.add(current_name)

if sum(odd_num) == sum(even_num):
    print(*odd_num.union(even_num), sep=", ")
elif sum(odd_num) > sum(even_num):
    print(*odd_num, sep=", ")
elif sum(even_num) > sum(odd_num):
    print(*even_num.symmetric_difference(odd_num), sep=", ")
