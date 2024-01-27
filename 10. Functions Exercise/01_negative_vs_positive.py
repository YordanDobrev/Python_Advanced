def check(*num):
    positive = sum([element for element in num if element > 0])
    negative = sum([element for element in num if element < 0])

    print(negative)
    print(positive)

    if abs(negative) > abs(positive):
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


elements = [int(i) for i in input().split()]

print(check(*elements))
