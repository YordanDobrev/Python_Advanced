def team_lineup(*args):
    teams = {}
    result = []
    for name, country in args:

        if country not in teams:
            teams[country] = []

        teams[country].append(name)

    for key, value in sorted(teams.items(), key=lambda k: (-len(k[1]), k[0])):
        result.append(f"{key}:")

        for players in value:
            result.append(f"  -{players}")

    return "\n".join(result)


print(team_lineup(

    ("Lionel Messi", "Argentina"),

    ("Neymar", "Brazil"),

    ("Cristiano Ronaldo", "Portugal"),

    ("Harry Kane", "England"),

    ("Kylian Mbappe", "France"),

    ("Raheem Sterling", "England")))
