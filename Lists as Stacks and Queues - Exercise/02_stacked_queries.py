from collections import deque

nums = int(input())
the_stack = []

for i in range(nums):
    action = input().split()
    if action[0] == "1":
        the_stack.append(int(action[1]))
    elif action[0] == "2":
        if the_stack:
            the_stack.pop()
    elif action[0] == "3":
        print(max(the_stack))
    elif action[0] == "4":
        print(min(the_stack))

the_stack.reverse()

print(*the_stack, sep=", ")
