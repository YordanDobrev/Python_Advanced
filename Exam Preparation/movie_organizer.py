def movie_organizer(*args):
    collection = {}
    result = []

    for movie in args:
        current_movie = movie[0]
        genre = movie[1]

        if genre not in collection:
            collection[genre] = []

        collection[genre].append(current_movie)

    for key, value in sorted(collection.items(), key=lambda k: (-len(k[1]), k[0])):
        result.append(f"{key} - {len(value)}")
        for movie in sorted(value):
            result.append(f"* {movie}")

    return "\n".join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
