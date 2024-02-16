def list_manipulator(the_list, action, task, *args):
    result = []
    if action == "remove" and task == "beginning":
        if not args:
            the_list.pop(0)
            result.extend(the_list)
        else:
            temp = []
            temp.extend(args)
            the_list = the_list[temp[0]:]
            result.extend(the_list)

    elif action == "remove" and task == "end":
        if not args:
            the_list.pop()
            result.extend(the_list)
        else:
            temp = []
            temp.extend(args)
            size = len(the_list) - temp[0]
            the_list = the_list[:size]
            result.extend(the_list)

    if action == "add" and task == "beginning":
        result.extend(list(args))
        result.extend(the_list)
    elif action == "add" and task == "end":
        result.extend(the_list)
        result.extend(list(args))

    return result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
