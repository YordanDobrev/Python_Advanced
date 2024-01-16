from collections import deque

food = int(input())

the_queue = deque([int(x) for x in input().split()])
max_order = max(the_queue)

while the_queue:
    if the_queue[0] > food:
        break

    food -= the_queue.popleft()

print(max_order)

if the_queue:
    print(f"Orders left:", *the_queue)
else:
    print("Orders complete")
