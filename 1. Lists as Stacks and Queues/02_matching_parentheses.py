expression = input()

parentheses_index = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses_index.append(i)
    elif expression[i] == ")":
        start_parenth = int(parentheses_index.pop())
        end_parenth = i + 1
        print(expression[start_parenth:end_parenth])