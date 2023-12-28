import requests

def main(API_KEY, match_id):
    # Dota 2 Match Details
    match_details_url = f'http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?key={API_KEY}&match_id={match_id}'
    match_details_response = requests.get(match_details_url)
    print('Match Details:', match_details_response.json())

# # Dota 2 Match History
# match_history_url = f'http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?key={API_KEY}'
# match_history_response = requests.get(match_history_url)
# print('Match History:', match_history_response.json())
#
# # Dota 2 Player Statistics
# steam_id = 'STEAM_ID'
# player_summaries_url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={API_KEY}&steamids={steam_id}'
# player_summaries_response = requests.get(player_summaries_url)
# print('Player Summaries:', player_summaries_response.json())
#
# # Dota 2 Friend List
# friend_list_url = f'http://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={API_KEY}&steamid={steam_id}'
# friend_list_response = requests.get(friend_list_url)
# print('Friend List:', friend_list_response.json())
#
# # Dota 2 Team Information
# team_id = 'TEAM_ID'
# team_info_url = f'http://api.steampowered.com/IDOTA2Teams_570/GetTeamInfoByTeamID/v1/?key={API_KEY}&start_at_team_id={team_id}&teams_requested=1'
# team_info_response = requests.get(team_info_url)
# print('Team Information:', team_info_response.json())
#
# # Dota 2 Pro Player List
# pro_player_list_url = f'http://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key={API_KEY}'
# pro_player_list_response = requests.get(pro_player_list_url)
# print('Pro Player List:', pro_player_list_response.json())
#
# # Dota 2 Hero List
# heroes_url = 'http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key={API_KEY}'
# heroes_response = requests.get(heroes_url)
# print('Hero List:', heroes_response.json())
#
# # Dota 2 Item List
# items_url = 'http://api.steampowered.com/IEconDOTA2_570/GetGameItems/v1/?key={API_KEY}'
# items_response = requests.get(items_url)
# print('Item List:', items_response.json())
#
# # Dota 2 Tournament Information
# tournament_id = 'TOURNAMENT_ID'
# tournament_player_stats_url = f'http://api.steampowered.com/IDOTA2MatchStats_570/GetTournamentPlayerStats/v1/?key={API_KEY}&account_id={steam_id}&league_id={tournament_id}'
# tournament_player_stats_response = requests.get(tournament_player_stats_url)
# print('Tournament Player Stats:', tournament_player_stats_response.json())
#
# # Dota 2 Live League Games
# live_league_games_url = f'http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key={API_KEY}'
# live_league_games_response = requests.get(live_league_games_url)
# print('Live League Games:', live_league_games_response.json())
#
# # Dota 2 Scheduled League Games
# scheduled_league_games_url = f'http://api.steampowered.com/IDOTA2Match_570/GetScheduledLeagueGames/v1/?key={API_KEY}'
# scheduled_league_games_response = requests.get(scheduled_league_games_url)
# print('Scheduled League Games:', scheduled_league_games_response.json())