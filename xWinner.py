import time
def xWin(xPos):

    # Checks for across matches
    x= 1
    y= 1
    while x in range(1, 28):

        if  x in xPos and x + y in xPos and x + (y*2) in xPos:
            #print "o wins yay"
            x+=2002002
            time.sleep(2)
            #print"win"
            return True
            break
        else:
            x+=3
    #up down
    x= 1
    y= 3
    while x in range(1, 28):
        if x in range(1,4) or x in range(10,14) or x in range(19,24):
            if  x in xPos and x + y in xPos and x + (y*2) in xPos:
                #print "o wins yay"
                x+=2002002
                time.sleep(2)

                return True
                break
            else:

                x+=1
        else:

            x+=1
    #vertical
    x= 1
    y= 9
    while x in range(1, 28):
        if  x in xPos and x + y in xPos and x + (y*2) in xPos:
            #print "o wins yay"
            time.sleep(2)
            #print"win"
            x+=2002002
            return True
        else:
            x+=1
    x= 3
    y= 2
    while x in range(1, 28):
        if  x in xPos and x + y in xPos and x + (y*2) in xPos:
            #print "o wins yay"
            time.sleep(2)
            x+=2002002
            return True
        else:
            x+=9
    x= 1
    y= 4
    while x in range(1, 28):
        if  x in xPos and x + y in xPos and x + (y*2) in xPos:
            #print "o wins yay"
            time.sleep(2)
            x+=2002002
            return True
        else:
            x+=9
    x= 1
    y= 13
    while x in range (1,4):
        if  x in xPos and x + y in xPos and x + (y*2) in xPos:
            x+=900
            return True
        else:
            x+=2
            y-=2
    #DIAGONAL DIAGONAL VERTICAL

    x= 1
    y= 13
    x1=7
    y1=7
    while x in range (1,4):
        if  (x in xPos and x + y in xPos and x + (y*2) in xPos)or(x1 in xPos and x1 + y1 in xPos and x1 + (y1*2) in xPos):
            x+=900
            return True
        else:
            x+=2
            y-=2
            y1-=2
            x1+=2

    #ACROSS DIAGONAL VERTICAL

    x= 1
    y= 10

    while x in range (1,8):
        if  (x in xPos and x + y in xPos and x + (y*2) in xPos):
            x+=900
            return True
        else:
            x+=3
    x= 3
    y= 7
#above but compressed
    while x in range (3,10):
        if  (x in xPos and x + y in xPos and x + (y*2) in xPos):
            x+=900
            return True
        else:
            x+=3
    count = 1
    x=1
    y=12

    while x <= 3:
        if  (x in xPos and x + y in xPos and x + (y*2) in xPos):
            x+=900
            return True
        else:
            x+=1
    x=7
    y=6
    while x <= 9:
        if  (x in xPos and x + y in xPos and x + (y*2) in xPos):
            x+=900
            return True
        else:
            x+=1


    return False
