from collections import deque

textile = deque([int(elem) for elem in input().split()])
meds = [int(elem) for elem in input().split()]

heal_items = {}

while True:
    if not textile:
        break
    elif not meds:
        break

    item = textile.popleft()
    medicament = meds.pop()
    total = item + medicament

    if total == 30:
        if "Patch" not in heal_items:
            heal_items["Patch"] = 0
        heal_items["Patch"] += 1
    elif total == 40:
        if "Bandage" not in heal_items:
            heal_items["Bandage"] = 0
        heal_items["Bandage"] += 1
    elif total == 100:
        if "MedKit" not in heal_items:
            heal_items["MedKit"] = 0
        heal_items["MedKit"] += 1
    elif total > 100:
        if "MedKit" not in heal_items:
            heal_items["MedKit"] = 0
        heal_items["MedKit"] += 1
        difference = total - 100
        meds[-1] += difference
    else:
        medicament += 10
        meds.append(medicament)

if not textile and not meds:
    print("Textiles and medicaments are both empty.")
elif not meds:
    print("Medicaments are empty.")
elif not textile:
    print("Textiles are empty.")

if heal_items:
    for key, value in sorted(heal_items.items(), key=lambda k: (-k[1], k[0])):
        print(f"{key} - {value}")

if meds:
    print(f"Medicaments left: {', '.join([str(elm) for elm in meds[::-1]])}")
if textile:
    print(f"Textiles left: {', '.join([str(elm) for elm in textile])}")
