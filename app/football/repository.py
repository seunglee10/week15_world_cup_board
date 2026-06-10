from app.football.data import PLAYERS
from app.football.match_data import MATCHES


def get_players() -> list[dict]:
    return PLAYERS


def get_matches() -> list[dict]:
    return MATCHES