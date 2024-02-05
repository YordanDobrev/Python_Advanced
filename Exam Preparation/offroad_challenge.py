from collections import deque

fuel = [int(fuel) for fuel in input().split()]
consumption = deque([int(consume) for consume in input().split()])
quantity = deque([int(qty) for qty in input().split()])

altitude_reached = 0

while True:
    if not quantity:
        print("John has reached all the altitudes and managed to reach the top!")
        break

    if fuel[-1] > consumption[0]:
        fuel[-1] -= consumption.popleft()

    if fuel[-1] >= quantity[0]:
        altitude_reached += 1
        fuel.pop()
        quantity.popleft()
        print(f"John has reached: Altitude {altitude_reached}")
    else:
        print(f"John did not reach: Altitude {altitude_reached + 1}")
        break

if fuel:
    print(f"John failed to reach the top.")

    not_reached = []
    for index in range(1, altitude_reached + 1):
        not_reached.append(f"Altitude {index}")
    if not not_reached:
        print(f"John didn't reach any altitude.")
    else:
        print(f"Reached altitudes:", ', '.join(not_reached))
