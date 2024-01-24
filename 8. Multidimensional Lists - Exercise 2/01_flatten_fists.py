line = [element.split() for element in input().split("|")]

print(*[" ".join(el) for el in line[::-1] if el])
