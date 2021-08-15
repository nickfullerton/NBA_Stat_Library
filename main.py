from src.PlayerLibrary import *

player = PlayerStats()
players = player.GetPlayer("James Harden")

print(players[0].GetName())
print(players[0].GetStats())
print(players[0].GetPlayoffStats())
print(players[0].GetYears())
print(players[0].GetPlayoffYears())
