from fastapi import APIRouter, HTTPException

from app.football.service import get_team, list_teams

router = APIRouter(prefix="/football", tags=["football"])


@router.get("/teams")
def read_teams():
    return list_teams()


@router.get("/teams/{team_id}")
def read_team(team_id: int):
    team = get_team(team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
