from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(element) for element in input().split()])

fit = len(worms)

idx_holes = 0
match = 0

while True:

    if worms[-1] == holes[0]:
        worms.pop()
        holes.popleft()
        match += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

    if len(worms) == 0 or len(holes) == 0:
        break

if match > 0:
    print(f"Matches: {match}")
else:
    print(f"There are no matches.")

if not worms and fit == match:
    print(f"Every worm found a suitable hole!")
elif not worms and match >= 0:
    print(f"Worms left: none")
elif worms:
    worm_to_print = [str(el) for el in worms]
    print(f"Worms left: {', '.join(worm_to_print)}")

if not holes:
    print(f"Holes left: none")
else:
    hole_to_print = [str(element) for element in holes]
    print(f"Holes left: {', '.join(hole_to_print)}")
