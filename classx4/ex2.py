

import pygame
from pygame.locals import *

keepGoing = True

# window setting
SCREENSIZE = 800

pygame.init()
screen = pygame.display.set_mode([SCREENSIZE, SCREENSIZE])
pygame.display.set_caption("Snake")

############
RED = [255, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

# about snake
SNAKEBODY = 20
SNAKECOLOR = RED

img = pygame.Surface((SNAKEBODY, SNAKEBODY))  #
img.fill(SNAKECOLOR)

xs = [300, 300, 300, 300, 300]
ys = [280, 260, 240, 220, 200]
dire = "DOWN"

clock=pygame.time.Clock()

def die():
    global keepGoing
    screen.fill(WHITE)
    f=pygame.font.SysFont("Arial",50)
    t=f.render("Game Over",True,BLACK)
    screen.blit(t,(10,270))
    pygame.time.wait(2000)
    keepGoing=False

    
while keepGoing:
    # set the key controller
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and dire != "DOWN":
                dire = "UP"
            elif event.key == K_DOWN and dire != "UP":
                dire = "DOWN"
            elif event.key == K_LEFT and dire != "RIGHT":
                dire = "LEFT"
            elif event.key == K_RIGHT and dire != "LEFT":
                dire = "RIGHT"

    # update body
    i = len(xs) - 1
    if xs[0]<=0 or 800-xs[0]<=SNAKEBODY or ys[0]<=0 or 600-ys[0]<=SNAKEBODY:
            die()
    i=len(xs)-1
    while i >= 1: 
        xs[i] = xs[i - 1]
        ys[i] = ys[i - 1]
        i -= 1

    # new head
    if dire == "UP":
        ys[0] -= SNAKEBODY
    elif dire == "DOWN":
        ys[0] += SNAKEBODY
    elif dire == "LEFT":
        xs[0] -= SNAKEBODY
    elif dire == "RIGHT":
        xs[0] += SNAKEBODY

    screen.fill(BLACK)
    for i in range(0, len(xs)):
        screen.blit(img,(xs[i], ys[i]))

    pygame.display.update()

pygame.quit()