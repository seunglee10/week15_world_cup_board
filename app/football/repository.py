from app.football.data import PLAYERS
from app.football.match_data import MATCHES
from app.football import external_api


def get_players() -> list[dict]:
    return PLAYERS


def get_matches() -> list[dict]:
    try:
        return external_api.fetch_worldcup_matches()
    except Exception:
        return MATCHES
    

def search_players(name: str) -> list[dict]:
    try:
        return external_api.fetch_players_by_name(name)
    except Exception:
        return get_players()