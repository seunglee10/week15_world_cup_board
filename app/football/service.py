from app.football.repository import get_players, get_matches
from app.football import external_api

def normalize_text(text: str) -> str:
    return text.lower().replace(" ", "").replace("-", "")


def search_players(name: str) -> list[dict]:
    try:
        api_players = external_api.fetch_players_by_name(name)

        if api_players:
            return api_players

    except Exception:
        pass

    normalized_search_name = normalize_text(name)

    results = []

    for player in get_players():
        normalized_player_name = normalize_text(player["name"])

        if normalized_search_name in normalized_player_name:
            results.append(player)

    return results

def get_team_players(country: str) -> list[dict]:
    normalized_country = normalize_text(country)

    results = []

    for player in get_players():
        normalized_player_country = normalize_text(player["country"])

        if normalized_country in normalized_player_country:
            results.append(player)

    return results


def get_match_schedule(country: str) -> list[dict]:
    normalized_country = normalize_text(country)

    results = []

    for match in get_matches():
        normalized_home_team = normalize_text(match["home_team"])
        normalized_away_team = normalize_text(match["away_team"])

        if (
            normalized_country in normalized_home_team
            or normalized_country in normalized_away_team
        ):
            results.append(match)

    return results