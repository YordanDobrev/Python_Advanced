first_part, second_part = [int(x) for x in input().split()]

first_elements = set()
second_elements = set()

for i in range(first_part):
    current_num = int(input())
    first_elements.add(current_num)

for j in range(second_part):
    action = int(input())
    second_elements.add(action)

unique_elements = first_elements.intersection(second_elements)

print(*unique_elements, sep="\n")
