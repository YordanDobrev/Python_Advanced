from collections import deque


def calculator(current_bee, current_nectar, symbol):
    result = 0

    if symbol == "+":
        result = current_bee + current_nectar
    elif symbol == "-":
        result = abs(current_bee - current_nectar)
    elif symbol == "*":
        result = current_bee * current_nectar

    return result


bees = deque([int(bee) for bee in input().split()])
nectar = [int(element) for element in input().split()]
math_symbol = deque(input().split())

total_honey = 0

while True:

    if not bees or not nectar:
        break

    if bees[0] <= nectar[-1]:
        if math_symbol[0] == "/":
            nectar.pop()
            bees.popleft()
            math_symbol.popleft()
            continue
        current_nectar = nectar.pop()
        current_bee = bees.popleft()
        total_honey += abs(calculator(current_bee, current_nectar, math_symbol.popleft()))

    elif bees[0] > nectar[-1]:
        nectar.pop()

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(nec) for nec in nectar])}")
