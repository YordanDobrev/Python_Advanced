def sorting_cheeses(**kwargs):
    text_to_print = ""

    the_sorted = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese, quantities in the_sorted:
        text_to_print += cheese + "\n"

        for i in sorted(quantities, reverse=True):
            text_to_print += str(i) + "\n"

    return text_to_print

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

