cars = int(input())

parking = set()

for _ in range(cars):
    action, plate_num = input().split(", ")

    if action == "IN":
        parking.add(plate_num)
    elif action == "OUT":
        parking.remove(plate_num)

if parking:
    for i in parking:
        print(i)
else:
    print("Parking Lot is Empty")