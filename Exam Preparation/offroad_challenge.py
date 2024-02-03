from collections import deque

fuel = [int(fuel) for fuel in input().split()]
consumption = deque([int(consum) for consum in input().split()])
quantity = deque([int(qty) for qty in input().split()])

altitude_reached = 0

while True:

    if fuel[-1] > consumption[0]:
        fuel[-1] -= consumption.popleft()



    if fuel[-1] >= quantity[0]:
        altitude_reached += 1
        fuel.pop()
        quantity.popleft()
        print(f"John has reached: Altitude {altitude_reached}")
    else:

        break