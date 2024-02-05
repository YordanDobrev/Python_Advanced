from collections import deque


def calculator(total_magic):
    result = ""

    if total_magic == 150:
        result = "Doll"
    elif total_magic == 250:
        result = "Wooden train"
    elif total_magic == 300:
        result = "Teddy bear"
    elif total_magic == 400:
        result = "Bicycle"

    if result == "":
        return "Not enough magic"
    return result


materials = [int(x) for x in input().split()]
magic = deque(int(y) for y in input().split())

presents = {}

while True:
    if len(materials) == 0 or len(magic) == 0:
        break

    if materials[-1] == 0:
        current_material = materials.pop()
        continue

    if magic[0] == 0:
        current_magic = magic.popleft()
        continue

    current_material = materials.pop()
    current_magic = magic.popleft()
    total = current_material * current_magic

    if total < 0:
        positive_calc = current_magic + current_material
        materials.append(positive_calc)
        total = materials.pop() * magic.popleft()
    elif total > 0 and total != 150 and total != 250 and total != 300 and total != 400:

        materials.append(current_material + 15)

    if calculator(total) == "Not enough magic":
        continue
    else:
        if calculator(total) not in presents.keys():
            presents[calculator(total)] = 0
        presents[calculator(total)] += 1

crafted = []

for key, value in presents.items():
    crafted.append(key)

if "Doll" and "Wooden train" in crafted:
    print("The presents are crafted! Merry Christmas!")
elif "Teddy bear" and "Bicycle" in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(element) for element in materials][::-1])}")
if magic:
    print(f"Materials left: {', '.join([str(x) for x in magic])}")

for current_present, quantity in presents.items():
    print(f"{current_present}: {quantity}")

# all(k for k in ["Doll", "Wooden train"])
