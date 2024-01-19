first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

lines = int(input())

for _ in range(lines):
    command_one, next_command, *data = input().split()

    current_command = command_one + " " + next_command

    if current_command == "Add First":
        for i in data:
            first_sequence.add(int(i))
    elif current_command == "Add Second":
        for j in data:
            second_sequence.add(int(j))
    elif current_command == "Remove First":
        for k in data:
            if int(k) in first_sequence:
                first_sequence.remove(int(k))
    elif current_command == "Remove Second":
        for m in data:
            if int(m) in second_sequence:
                second_sequence.remove(int(m))
    elif current_command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

one = sorted(first_sequence)
two = sorted(second_sequence)
print(*one, sep=", ")
print(*two, sep=", ")
