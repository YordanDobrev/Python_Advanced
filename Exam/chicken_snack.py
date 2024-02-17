from collections import deque

money = [int(el) for el in input().split()]
food_price = deque([int(el) for el in input().split()])
eaten_food = 0
food_size = len(food_price)

while money and food_price:

    amount = money.pop()
    price = food_price.popleft()

    if amount == price:
        eaten_food += 1
    elif amount > price:
        change = amount - price
        eaten_food += 1
        if money:
            money[-1] += change
    elif amount < price:
        continue

if not eaten_food:
    print("Henry remained hungry. He will try next weekend again.")
elif eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")
elif 1 < eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")
if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
