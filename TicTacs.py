import time
from xWinner import xWin
from oWinner import oWin
from position import all
from outputboard import go
import os
clear = lambda: os.system('cls')
clear()

wantToPlay = 'n'
while wantToPlay != 'y':
    wantToPlay = input(" Do you want to play a game (y/n)")
time.sleep(1)
print ("How bout a nice game of Tic Tac Toe")

open = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
xPos =[]
oPos =[]

def isGameOver(moves,xPos,oPos):
    if  xWin(xPos) == True or oWin(oPos) == True or moves == 27:
        return True
    else:
        return False

def newUser(user):
    if user == 'x':
        return 'o'
    else:
        return 'x'
moves = 0
user = ''
while user != "x" and user != "o":
    user = input('Player two: What letter do you want to be?')
while isGameOver(moves,xPos,oPos) == False:
    clear()
    print (go(open, xPos,oPos))
    user = newUser(user)
    print ("It is %s's turn" % (user))
    if user == 'x':
        placeholder = (int(input("Where do you want to go??")))
        try:
            open.remove(placeholder)
        except:
            xMove()
        xPos.append(placeholder)
        print (xPos)

    else:
        placeholder = (int(input("Where do you want to go??")))
        oPos.append(placeholder)
        open.remove(placeholder)
        print (oPos)
    moves += 1
clear()
print (go(open, xPos,oPos))
if xWin(xPos) == True:
    print ("X WINS :(")
elif oWin(oPos) == True:
    print ("O WINS ")
else:
    print("TIE TIE TIE THE BEST MOVE IS NOT TO PLAY")
