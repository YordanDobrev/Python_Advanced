from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]

total_time = 0

while taxis and customers:

    person = customers.popleft()
    taxi = taxis.pop()

    if taxi >= person:
        total_time += person
    else:
        customers.appendleft(person)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(num) for num in customers])}")
