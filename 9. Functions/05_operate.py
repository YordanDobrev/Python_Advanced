from functools import reduce


def operate(operand, *args):
    def add():
        return reduce(lambda x, y: x + y, args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def divide():
        return reduce(lambda x, y: x / y, args)

    if operand == "+":
        return add()
    elif operand == "-":
        return subtract()
    elif operand == "*":
        return multiply()
    elif operand == "/":
        return divide()


print(operate("*", 3, 4))
