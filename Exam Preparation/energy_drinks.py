from collections import deque

caffeine = [int(el) for el in input().split(", ")]
drinks = deque([int(el) for el in input().split(", ")])

max_caffeine = 300

while caffeine and drinks:
    milligrams = caffeine.pop()
    current_drink = drinks.popleft()

    total = milligrams * current_drink

    if total <= max_caffeine:
        max_caffeine -= total
    else:
        drinks.append(current_drink)
        if max_caffeine - 30 < 0:
            break
        max_caffeine -= 30
