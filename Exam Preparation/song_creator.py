def add_songs(*args):
    songs = {}

    result = []

    for index in args:
        current_song = index[0]
        lyrics = index[1]

        if current_song not in songs:
            songs[current_song] = []

        for text in lyrics:
            songs[current_song].append(text)

    for key, value in songs.items():
        result.append(f"- {key}")
        for i in value:
            result.append(i)

    return "\n".join(result)


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
