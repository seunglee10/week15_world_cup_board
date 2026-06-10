from app.football.service import search_players
from app.football.service import get_team_players

print(search_players("son"))
print(search_players("SON"))
print(search_players("heung"))
print(search_players("sonheungmin"))
print(search_players("ronaldo"))
print(get_team_players("korea"))
print(get_team_players("KOREA REPUBLIC"))
print(get_team_players("korearepublic"))
print(get_team_players("brazil"))