from app.football.data import FOOTBALL_TEAMS


def list_teams():
    return FOOTBALL_TEAMS


def get_team(team_id: int):
    return next((team for team in FOOTBALL_TEAMS if team["id"] == team_id), None)
