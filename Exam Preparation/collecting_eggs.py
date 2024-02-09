from collections import deque

eggs_size = deque([int(el) for el in input().split(", ")])
paper_size = deque([int(el) for el in input().split(", ")])
BOX_SIZE = 50

filled_boxes = 0

while True:
    if not eggs_size or not paper_size:
        break

    if eggs_size[0] <= 0:
        egg = eggs_size.popleft()
        continue
    else:
        egg = eggs_size.popleft()
        paper = paper_size.pop()

    if egg == 13:
        lucky_paper = paper_size.popleft()
        paper_size.append(lucky_paper)
        paper_size.appendleft(paper)
        continue

    total = egg + paper

    if total <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes >= 1:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(el) for el in eggs_size])}")
if paper_size:
    print(f"Pieces of paper left: {', '.join([str(el) for el in paper_size])}")
