from collections import deque

init_fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

altitude_reached = 0
max_altitude = len(fuel_needed)

while init_fuel and consumption and fuel_needed:

    fuel = init_fuel.pop()
    consume = consumption.popleft()
    f_needed = fuel_needed.popleft()

    if (fuel - consume) >= f_needed:
        altitude_reached += 1
        print(f"John has reached: Altitude {altitude_reached}")
    else:
        print(f"John did not reach: Altitude {altitude_reached + 1}")
        break

if max_altitude > altitude_reached and altitude_reached:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([str(f'Altitude {el}') for el in range(1, altitude_reached + 1)])}")

if max_altitude > altitude_reached and not altitude_reached:
    print(f"John failed to reach the top.")
    print("John didn't reach any altitude.")

if altitude_reached == max_altitude:
    print("John has reached all the altitudes and managed to reach the top!")
