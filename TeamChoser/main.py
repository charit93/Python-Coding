#!/bin/python3

from random import choice
players = []
file = open('players.txt','r')
players = file.read().splitlines()
print(players)
#print(choice(players))


teamNames= []
file = open('teamNames.txt','r')
teamNames = file.read().splitlines()
print('Team names:', teamNames)

teamA=[]
teamB=[]
teamC=[]

while len(players) > 0:
 playerA = choice(players)
 teamA.append(playerA)
 players.remove(playerA)
 
 if players == []:
    break 

 playerB = choice(players)
 teamB.append(playerB)
 players.remove(playerB)
 

 
#print('teamA :', teamA)
#print('teamB :', teamB)

leadplayerA = choice(teamNames)
leadplayerB = choice(teamNames)


print('\nHere are your teams:\n')

print(leadplayerA,teamA)
print(leadplayerB,teamB)
