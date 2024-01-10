from collections import deque

kids = deque(input().split())
rotation = int(input()) - 1

while kids:
    kids.rotate(-rotation)

    if len(kids) > 1:
        print(f"Removed {kids.popleft()}")
    else:
        print(f"Last is {kids.popleft()}")