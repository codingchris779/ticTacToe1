# this is a testing comment for git
import pygame
import time
from xWinner import xWin
from oWinner import oWin
from position import all
from outputboard import go
from test import getComputerMove
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
tictac = pygame.image.load('tictactoe.png')
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
        pygame.draw.rect(gameDisplay, green,(posButtons[number][0],posButtons[number][1],100,50))
def oDisplay(oPos,red):
    for number in oPos:
        pygame.draw.rect(gameDisplay, red,(posButtons[number][0],posButtons[number][1],100,50))


black = (0,0,0)

pygame.init()
#defines list of the button positions upper left in xy cordinates
posButtons=[[],[56,679],[170,680],[360,679],[72,617],[188,621],[350,611],[87,557],[191,557],[339,544],[57,440],[161,438],[360,435],[73,378],[177,370],[354,375],[86,315],[184,306],
            [346,303],[56,196],[164,200],[358,198],[71,127],[179,131],[352,131],[82,65],[189,74],[342,71]]

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
        index = button('',posButtons[number][0],posButtons[number][1],100,60,white,black,number)






quit = False
while not quit:
    if gameOver==False:
        if user == 'x':
            for event in pygame.event.get():

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
            move = getComputerMove(open,oPos,xPos)
            user = 'x'
            open.remove(move)
            oPos.append(move)
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
