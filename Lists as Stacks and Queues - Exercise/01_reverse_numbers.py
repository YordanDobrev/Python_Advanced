from collections import deque

text_to_reverse = deque(input().split())

while text_to_reverse:
    print(text_to_reverse.pop(), end=" ")