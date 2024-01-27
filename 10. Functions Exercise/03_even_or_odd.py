def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [element for element in args[:-1] if element % 2 == 0]
    else:
        return [el for el in args[:-1] if el % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
