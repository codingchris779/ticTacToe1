import time
open = [3,4,5,6,7,9,10,11,12,13,14,16,17,18,21,22,23,24,25,26,27]
open = [3,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
xPos=[2,7]
oPos=[1,4]
count = 0

def all(open, xPos, oPos):
    board = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    count = 0
    for number in xPos:
        #print number
        board.remove(xPos[count])
        board.insert(xPos[count], 'x')
        #print board
        count +=1
    oCount = 0
    for number in oPos:
        board.remove(oPos[oCount])
        board.insert(oPos[oCount], 'o')
        #print number
        #print board
        oCount += 1



    return board
#print all(open, xPos, oPos)
