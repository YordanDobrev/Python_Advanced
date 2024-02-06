from collections import deque

monster = deque([int(i) for i in input().split(",")])
soldier = [int(x) for x in input().split(",")]

total_monsters_killed = 0

while monster and soldier:

    current_monster = monster.popleft()
    current_soldier_strike = soldier.pop()

    if current_soldier_strike >= current_monster:
        current_soldier_strike -= current_monster
        total_monsters_killed += 1
        if soldier:
            soldier[-1] += current_soldier_strike
        elif not soldier and current_soldier_strike > 0:
            soldier.append(current_soldier_strike)

    elif current_soldier_strike < current_monster:
        current_monster -= current_soldier_strike
        monster.append(current_monster)

if not monster:
    print("All monsters have been killed!")
if not soldier:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_monsters_killed}")
