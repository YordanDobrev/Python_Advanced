parentheses = input()

the_list = []

for index in range(len(parentheses)):

    if parentheses[index] == ")" and the_list[-1] == "(":
        the_list.pop()
    elif parentheses[index] == "}" and the_list[-1] == "{":
        the_list.pop()
    elif parentheses[index] == "]" and the_list[-1] == "[":
        the_list.pop()
    else:
        the_list.append(parentheses[index])

if the_list:
    print("NO")
else:
    print("YES")
