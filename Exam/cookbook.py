def cookbook(*args):
    result = []
    cookbook = {}

    for recipe, cuisine, products in args:
        if cuisine not in cookbook:
            cookbook[cuisine] = {}

        cookbook[cuisine][recipe] = ', '.join(products)

    for key, value in sorted(cookbook.items(), key=lambda k: (-len(k[1]), k[0])):
        result.append(f"{key} cuisine contains {len(value)} recipes:")
        for element in sorted(value):
            result.append(f"  * {element} -> Ingredients: {value[element]}")

    return "\n".join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

