names = int(input())

unique_names = set()

for _ in range(names):
    action = input()

    if action not in unique_names:
        unique_names.add(action)
        print(action)