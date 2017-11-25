from xWinner import xWin
from oWinner import oWin

open=[1,2,3,4,5,6,7,8,9,10]
#Me messing around / experimental code data
def findScore (xPos,oPos,user):
    if user == x:
        if xWin(xPos) == True:
            return 10
        else:
            return 0
    else:
        if oWin(oPos) == True:
            return -10
        else:
            return 0
user = 'x'
def duplicateList(open):
    minmaxopen=[]
    for value in open:
        minmaxopen.append(value)
    return minmaxopen
available = duplicateList(open)
scores = []
pos = []
class TicTacToeAI :
    def minimax(possibleMove, user, depth = 0):
        if user == "o":
            best = -10
        else:
            best = 10
        print (best)
possibleMove = 10

TicTacToeAI.minimax(possibleMove,user,depth = 0)
