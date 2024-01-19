from collections import deque
from math import floor

expression = deque(input().split())

index = 0

while index < len(expression):
    current_element = expression[index]

    if current_element == "*":
        for i in range(index - 1):
            expression.appendleft(str(int(expression.popleft()) * int(expression.popleft())))
    elif current_element == "+":
        for i in range(index - 1):
            expression.appendleft(str(int(expression.popleft()) + int(expression.popleft())))
    elif current_element == "-":
        for i in range(index - 1):
            expression.appendleft(str(int(expression.popleft()) - int(expression.popleft())))
    elif current_element == "/":
        for i in range(index - 1):
            expression.appendleft(str(floor(int(expression.popleft()) / int(expression.popleft()))))

    if current_element in "*+-/":
        del expression[1]
        index = 1

    index += 1

print(int(expression[0]))
