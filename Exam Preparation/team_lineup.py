def team_lineup(*args):
    teams = {}

    for player, country in args:
        if country not in teams:
            teams[country] = []
        teams[country].append(player)

    lineup = sorted(teams.items(), key=lambda k: (-len(k[1]), k[0]))

    result = ""

    for key, value in lineup:
        result += f"{key}:\n"
        for player in value:
            result += f"  -{player}\n"

    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
