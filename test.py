from oWinner import oWin
from xWinner import xWin
import multiprocessing
def chooseRandomMoveFromList(open, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if i in open:
             possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
         return None


def getComputerMove(open,oPos,xPos):
    oposcopy=oPos
    xposcopy=xPos
    for i in open:
        oposcopy.append(i)
        if oWin(oposcopy):
            return i
        else:
            oposcopy.remove(i)
    for i in open:
        xposcopy.append(i)
        if xWin(xposcopy):
            return i
        else:
            xposcopy.remove(i)

    move = chooseRandomMoveFromList(open, [1, 3, 7, 9,10,19,12,21,16,25,18,27])
    if move != None:
            return move
    else:
        move = chooseRandomMoveFromList()
    if move != None:
        return move
    else:
        return chooseRandomMoveFromList(board, [2,11,20,13,22,15,24,17,26,1, 4, 6, 8])
open=[1,2,3,4,5,7]
xPos=[6]
oPos=[8,9]
print (getComputerMove(open,oPos,xPos))
