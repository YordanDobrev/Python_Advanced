def shopping_cart(*args):
    meals = {
        "Dessert": [],
        "Pizza": [],
        "Soup": []
    }

    result = []
    to_print = False

    for cart in args:
        if cart == "Stop":
            break

        current_meal = cart[0]
        product = cart[1]

        if product in meals[current_meal]:
            continue

        if len(meals[current_meal]) == 3 and current_meal == "Soup" \
                or len(meals[current_meal]) == 4 and current_meal == "Pizza" \
                or len(meals[current_meal]) == 2 and current_meal == "Dessert":
            continue

        meals[current_meal].append(product)
        to_print = True

    for key, value in sorted(meals.items(), key=lambda k: (-len(k[1]), k[0])):
        result.append(f"{key}:")
        for items in sorted(value):
            result.append(f" - {items}")

    if to_print:
        return "\n".join(result)
    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),nation
    ('Pizza', 'ham'),
    'Stop',
))



