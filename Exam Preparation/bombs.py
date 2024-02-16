from collections import deque

bomb_effect = deque([int(el) for el in input().split(", ")])
casing = [int(el) for el in input().split(", ")]

pouch = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
success = False

while bomb_effect and casing:
    if pouch["Datura Bombs"] >= 3 and \
            pouch["Cherry Bombs"] >= 3 and \
            pouch["Smoke Decoy Bombs"] >= 3:
        success = True
        break
    current_effect = bomb_effect[0]
    the_casing = casing[-1]
    check = current_effect + the_casing
    temp_bomb = ""

    if check == 40:
        temp_bomb = "Datura Bombs"
        bomb_effect.popleft()
        casing.pop()
        pouch[temp_bomb] += 1
        continue
    elif check == 60:
        temp_bomb = "Cherry Bombs"
        bomb_effect.popleft()
        casing.pop()
        pouch[temp_bomb] += 1
        continue
    elif check == 120:
        temp_bomb = "Smoke Decoy Bombs"
        bomb_effect.popleft()
        casing.pop()
        pouch[temp_bomb] += 1
    else:
        casing[-1] -= 5
        continue

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effect])}")

if not casing:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(el) for el in casing])}")

if pouch:
    for key, value in sorted(pouch.items()):
        print(f"{key}: {value}")
