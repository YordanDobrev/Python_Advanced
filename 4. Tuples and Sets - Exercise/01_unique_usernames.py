names = int(input())

unique_names = set()

for _ in range(names):
    current_name = input()
    unique_names.add(current_name)

print(*unique_names, sep="\n")
