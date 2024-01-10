from collections import deque

dispenser = int(input())
command = input()
current_queue = deque()

while command != "Start":
    current_queue.append(command)
    command = input()

action = input()

while action != "End":
    current_action = action.split()
    if len(current_action) == 1:
        if int(current_action[0]) <= dispenser:
            dispenser -= int(current_action[0])
            print(f"{current_queue.popleft()} got water")
        else:
            print(f"{current_queue.popleft()} must wait")
    else:
        dispenser += int(current_action[1])
    action = input()

print(f"{dispenser} liters left")