import pygame
#import position.py

black = (0,0,0)

pygame.init()
#defines list of the button positions upper left in xy cordinates
open = [1,2,3]
posButtons=[[200,100],[56,679],[170,680],[360,679],[72,612]]
def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            print ("hi")
    else:
        pass

def boardButtons(open,black):
    for number in open:
        index = number
        button('',200,200,200,200,black,black)
        button('',posButtons[index][0],posButtons[index][0],100,100,black,black)
boardButtons(open,black)
