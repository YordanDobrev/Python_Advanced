def accommodate_new_pets(capacity: int, weight: float, *args):
    hotel = {}
    result = []

    for pet, current_weight in args:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if current_weight > weight:
            continue
        if pet not in hotel:
            hotel[pet] = 0
        hotel[pet] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")

    [result.append(f"{key}: {value}") for key, value in sorted(hotel.items())]

    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
