from collections import deque

programmer = deque([int(elem) for elem in input().split()])
tasks = [int(elem) for elem in input().split()]

ducky_type = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while True:
    if not programmer:
        break
    elif not tasks:
        break

    person = programmer.popleft()
    current_task = tasks.pop()

    time = person * current_task

    if time >= 181 and time <= 240:
        ducky_type["Small Yellow Rubber Ducky"] += 1
    elif time >= 121 and time <= 180:
        ducky_type["Big Blue Rubber Ducky"] += 1
    elif time >= 61 and time <= 120:
        ducky_type["Thor Ducky"] += 1
    elif time >= 0 and time <= 60:
        ducky_type["Darth Vader Ducky"] += 1
    elif time >= 241:
        current_task -= 2
        tasks.append(current_task)
        programmer.append(person)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key, value in ducky_type.items():
    print(f"{key}: {value}")
