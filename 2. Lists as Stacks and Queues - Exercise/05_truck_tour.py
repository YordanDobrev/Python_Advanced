from collections import deque

gas_station = int(input())

station_number = 0

truck = 0
distance = 0


for _ in range(gas_station):

    action = [int(x) for x in input().split()]
    petrol = action[0]
    distance = action[1]

