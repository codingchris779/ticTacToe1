from oWinner import won
from xWinner import xWin
import multiprocessing

xPos = []
oPos = []
open = [1,2,3,4,5,6,7,8,9]
class TicTacToeBrain :
    xPos = []
    oPos = []
    open = [1,2,3,4,5,6,7,8,9]
    def __init__(self, player = "x") :
        self._squares = {}
        self._copySquares = {}

    def getAvailableMoves(self,open) :
        return open

    def makeMove(self, position, player) :
        open.remove(position)
        if player == 'x':
            xPos.append(position)
        else:
            oPos.append(position)
    def undoMove(self, position, player) :
        open.append(position)
        if player == 'x':
            xPos.remove(position)
        else:
            oPos.remove(position)
    def complete(self,open) :
        # *** see above
        if len(open)==0:
            return True
        if self.getWinner(xPos,oPos,open) != None :
            return True
        return False

    def getWinner(self,xPos,oPos,open) :
        if won(xPos):
            return 'x'
        if won(oPos):
            return 'o'
        # *** see above
        if len(open) == 0:
            return "tie"
        return None

    def getEnemyPlayer(self, player) :
        if player == "x" :
            return "o"
        return "x"

    def minimax(self, player,open,xPos,oPos, depth = 0):
        if player == "o":
            best = -30
        else:
            best = 30
        if self.complete(open) :
            if self.getWinner(open,xPos,oPos) == "x" :

                return -30 + depth, None
            elif self.getWinner(open,xPos,oPos) == "tie" :

                return 0, None
            elif self.getWinner(open,xPos,oPos) == "o" :

                return 30 - depth, None

        bestMove = None
        for move in self.getAvailableMoves(open) :
            self.makeMove(move, player)
            val, _ = self.minimax(self.getEnemyPlayer(player),open,xPos,oPos, depth+1)
            #print(val)
            # *** undo last move
            self.undoMove(move, player)
            if player == "o" :
                if val > best :
                    # *** Also keep track of the actual move
                    best, bestMove = val, move
            else :
                if val < best :
                    # *** Also keep track of the actual move
                    best, bestMove = val, move
        bestMove = bestMove
        return best, bestMove

    def printCopy(self) :
        print(self._copySquares)
game = TicTacToeBrain()
# val, bestMove = game.minimax("o",open,xPos,oPos)
# print ("best move", bestMove )
while game.complete:
    userInput = int(input())
    game.makeMove(userInput, 'x')
    val, bestMove = game.minimax("o",open,xPos,oPos)
    game.makeMove(bestMove, 'o')
    print (bestMove)
