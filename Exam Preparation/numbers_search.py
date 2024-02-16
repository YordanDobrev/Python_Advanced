def numbers_searching(*args):
    result = sorted([x for x in set(args)])
    missing = 0
    the_set = sorted(set([el for el in args if args.count(el) > 1]))

    for index in range(len(result)):
        try:
            if abs(result[index] - result[index + 1]) == 2:
                missing = result[index] + 1
        except IndexError:
            pass

    return list([missing, list(the_set)])


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(1, 2, 4, 2, 5, 4))
