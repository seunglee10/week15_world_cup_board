from app.football.data import PLAYERS

def normalize_text(text: str) -> str:
    return text.lower().replace(" ", "").replace("-", "")


def search_players(name: str) -> list[dict]:
    normalized_search_name = normalize_text(name)

    results = []

    for player in PLAYERS:
        normalized_player_name = normalize_text(player["name"])

        if normalized_search_name in normalized_player_name:
            results.append(player)

    return results

def get_team_players(country: str) -> list[dict]:
    normalized_country = normalize_text(country)

    results = []

    for player in PLAYERS:
        normalized_player_country = normalize_text(player["country"])

        if normalized_country in normalized_player_country:
            results.append(player)

    return results
