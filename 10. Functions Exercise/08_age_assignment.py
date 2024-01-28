def age_assignment(*args, **kwargs):
    result = []

    for word in args:
        for key, value in kwargs.items():
            if word.startswith(key):
                result.append(f"{word} is {value} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
