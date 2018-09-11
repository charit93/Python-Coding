#!/bin/python3

from random import randint

player = input('rock(r),paper(p) or scissors(s)?')
if player == 'r':
   print('0',end=' ')
elif player == 'p':
    print('--',end=' ')
else:
   print('>8',end= ' ')
print(player,'vs',end=' ')
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
  computer = 'r'
  print('0')
elif chosen == 2:
    computer = 'p'
    print('---')
else:
      computer = 's'
      print('>8')
print(computer)
if player == computer :
  print('Draw!')
elif player == 'r' and computer  == 's':
 print ('P wins')

elif player == 'r' and computer  == 'p':
 print ('C wins')

elif player == 'r' and computer  == 's':
 print ('P wins')

elif player == 'r' and computer  == 'p':
 print ('C wins')

elif player == 'p' and computer  == 'r':
 print ('P wins')

elif player == 'p' and computer  == 's':
 print ('C wins')