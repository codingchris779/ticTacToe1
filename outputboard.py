from position import all
open = [3,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
xPos=[2,7]
oPos=[1,4]
def go(open,xPos,oPos):
    board = all(open, xPos, oPos)
    print('    |    |')
    print(' ' + str(board[25]) + ' | ' + str(board[26]) + ' | ' + str(board[27]))
    print('    |    |')
    print('-------------')
    print('    |    |')
    print(' ' + str(board[22]) + ' | ' + str(board[23]) + ' | ' + str(board[24]))
    print('    |    |')
    print('-------------')
    print('    |    |          |    |')
    print(' ' + str(board[19]) + ' | ' + str(board[20]) + ' | ' + str(board[21])+'    '+ str(board[16]) + ' | ' + str(board[17]) + ' | ' + str(board[18]))
    print('    |    |          |    |' )
    print('                -------------')
    print('                    |    |')
    print('                 ' + str(board[13]) + ' | ' + str(board[14]) + ' | ' + str(board[15]))
    print('                    |    |')
    print('                -------------')
    print('                    |    |          |    |')
    print('                 ' + str(board[10]) + ' | ' + str(board[11]) + ' | ' + str(board[12])+'     ' + str(board[7]) + ' | ' + str(board[8]) + '  |  ' + str(board[9]))
    print('                    |    |          |    |')
    print('                                 ------------')
    print('                                    |    |')
    print('                                  ' + str(board[4]) + ' | ' + str(board[5]) + '  | ' + str(board[6]))
    print('                                    |    |')
    print('                                 ------------')
    print('                                    |    |')
    print('                                  ' + str(board[1]) + ' | ' + str(board[2]) + '  | ' + str(board[3]))
    print('                                    |    |')
go(open,xPos,oPos)
