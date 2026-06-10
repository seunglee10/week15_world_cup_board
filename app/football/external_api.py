import requests

from app.core.config import settings


BASE_URL = "https://v3.football.api-sports.io"


# API 호출
def fetch_worldcup_matches() -> list[dict]:
    url = f"{BASE_URL}/fixtures"

    headers = {
        "x-apisports-key": settings.API_FOOTBALL_KEY
    }

    params = {
        "league": 1,
        "season": 2022
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    return [parse_match(raw_match) for raw_match in data["response"]]


# 원본 데이터를 원하는 형식으로 변환
def parse_match(raw_match: dict) -> dict:
    fixture = raw_match["fixture"]
    teams = raw_match["teams"]

    match_datetime = fixture["date"]

    return {
        "id": fixture["id"],
        "date": match_datetime[:10],
        "time": match_datetime[11:16],
        "home_team": teams["home"]["name"],
        "away_team": teams["away"]["name"],
        "stadium": fixture["venue"]["name"],
    }