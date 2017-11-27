import pygame
import time
from xWinner import xWin
from oWinner import oWin
from position import all
from outputboard import go
import os
clear = lambda: os.system('cls')
clear()

pygame.init()

display_width = 800
display_height = 900

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('3d tic tac toe')

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
user = 'x'

clock = pygame.time.Clock()
gameOver = False
tictac = pygame.image.load('tic tac toe 2.JPG')
oWon = pygame.image.load('oWon.JPG')
xWon = pygame.image.load('xWon.JPG')

def isGameOver(moves,xPos,oPos):
    if  xWin(xPos) == True or oWin(oPos) == True or moves == 27:
        return True
    else:
        return False


def image(x,y,image):
    gameDisplay.blit(image, (x,y))

x =  (display_width * 0.045)
y = (display_height * 0.08)
def xDisplay(xPos,green):
    for number in xPos:
        pygame.draw.rect(gameDisplay, green,(posButtons[number][0],posButtons[number][1],55,55))
def oDisplay(oPos,red):
    for number in oPos:
        pygame.draw.rect(gameDisplay, red,(posButtons[number][0],posButtons[number][1],55,55))


black = (0,0,0)

pygame.init()
#defines list of the button positions upper left in xy cordinates
posButtons=[[],[157,79],[208,79],[260,79],[157,131],[208,131],[259,131],[157,186],[208,186],[259,186],[321,188],[373,188],[421,188],[321,240],[373,240],[421,240],
[321,292],[373,292],[421,292],[483,296],[535,296],[588,296],[483,347],[535,347],[588,347],[483,399],[535,399],[588,399]]

open = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
xPos=[]
oPos=[]



def button(msg,x,y,w,h,ic,ac,id):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global user
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1:
             index = id
             open.remove(index)
             if user == 'x':
                 xPos.append(index)
                 user = 'o'
             else:
                 oPos.append(index)
                 user = 'x'

        else:
            pass
    else:
        pass


def boardButtons(open,black,white):

    click = pygame.mouse.get_pressed()
    for number in open:
        index = button('',posButtons[number][0],posButtons[number][1],55,55,white,black,number)






quit = False
while not quit:
    click = pygame.mouse.get_pressed()
    if gameOver==False:
        for event in pygame.event.get():
            if click[0] == 1:
                print (event)

            if event.type == pygame.QUIT:
                gameOver=True

        gameDisplay.fill(white)
        image(x,y,tictac)
        click = pygame.mouse.get_pressed()
        boardButtons(open,black,white)
        xDisplay(xPos,green)
        oDisplay(oPos,red)
        moves=0
        quit = False
        gameOver = isGameOver(moves,xPos,oPos)
        pygame.display.update()
        clock.tick(60)
    else:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameOver=True
        if xWin(xPos) == True:
            image(x,y,xWon)
        else:
            image(x,y,oWon)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit=True
        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()
