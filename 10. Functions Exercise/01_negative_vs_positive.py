def check(*num):
    positive = []
    negative = []

    for index in num:
        if index > 0:
            positive.append(index)
        else:
            negative.append(index)

    print(sum(negative))
    print(sum(positive))

    if abs(sum(negative)) > abs(sum(positive)):
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


elements = [int(i) for i in input().split()]

print(check(*elements))
