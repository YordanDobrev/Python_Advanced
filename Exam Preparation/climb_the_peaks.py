from collections import deque

mountains = deque((
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
))

food_portions = [int(el) for el in input().split(", ")]
stamina = deque([int(el) for el in input().split(", ")])

conquered = []

while food_portions and stamina:
    current_food = food_portions.pop()
    current_stamina = stamina.popleft()

    total = current_food + current_stamina

    if total >= mountains[0][1]:
        conquered.append(mountains[0][0])
        mountains.popleft()
        if not mountains:
            break

if not mountains:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print("Conquered peaks:")
    print("\n".join(conquered))
