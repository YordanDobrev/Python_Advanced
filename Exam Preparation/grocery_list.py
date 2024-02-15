def shop_from_grocery_list(budget, the_list, *args):
    products = []
    successful_shopping = len(the_list)
    good_to_go = False

    for item, price in args:
        if not the_list:
            break
        if item in products:
            continue
        if item not in the_list:
            continue
        if budget - float(price) < 0:
            break

        products.append(item)
        the_list.remove(item)
        budget -= float(price)

        if successful_shopping == len(products):
            good_to_go = True
            break

    if good_to_go:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(the_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

