from mcp.server.fastmcp import FastMCP
from app.football import service

# Tool들을 등록하고 관리하는 mcp 서버(llm, agent의 요청을 받고 응답을 돌려줄) 객체
mcp = FastMCP("football-mcp-server")


@mcp.tool()
def search_players(name: str) -> list[dict]:
    """
    선수 이름으로 월드컵 선수 정보를 검색한다.
    사용자가 특정 선수의 국가, 포지션, 등번호, 소속팀, 리그, 생년월일, 키, 몸무게, 사진 정보를 묻는 경우 사용한다.
    부분 검색이 가능하며, 대소문자, 공백, 하이픈 차이는 무시한다.
    """
    return service.search_players(name)


@mcp.tool()
def get_team_players(country: str) -> list[dict]:
    """
    국가명을 기준으로 해당 국가의 월드컵 선수 목록을 조회한다.
    사용자가 특정 국가의 선수 명단, 포지션, 등번호, 소속팀 정보를 묻는 경우 사용한다.
    부분 검색이 가능하며, 대소문자, 공백, 하이픈 차이는 무시한다.
    """
    return service.get_team_players(country)


@mcp.tool()
def get_match_schedule(country: str) -> list[dict]:
    """
    국가명을 기준으로 해당 국가가 포함된 월드컵 경기 일정을 조회한다.
    사용자가 특정 국가의 경기 날짜, 시간, 상대 팀, 경기장 정보를 묻는 경우 사용한다.
    부분 검색이 가능하며, 대소문자, 공백, 하이픈 차이는 무시한다.
    """
    return service.get_match_schedule(country)