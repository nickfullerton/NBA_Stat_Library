from src.PlayerLibrary import *

player = PlayerStats()
players = player.GetPlayer("Bobby boo")


print(players[0].GetName())  # Returns Str, The player's name
print(players[0].GetStats())  # Returns Dict, The player's regular season stats of his career
print(players[0].GetPlayoffStats())  # Returns Dict, The player's playoff stats of his career
print(players[0].GetYears())  # Returns List, The player's years of playing professional basketball
print(players[0].GetPlayoffYears())  # Returns List, the player's years of making the playoffs
print(players[0].GetAchievements())  # Returns List, the player's career achievements
print(players[0].GetInfo())  # Returns List of Lists, the player's personal info
