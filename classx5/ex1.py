# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random

keepGoing = True

# window setting
SCREENSIZE = 600

pygame.init()
screen = pygame.display.set_mode([SCREENSIZE, SCREENSIZE])
pygame.display.set_caption("Snake")

RED = [255, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
point = 0
# about snake
SNAKEBODY = 20
SNAKECOLOR = RED

# about food
FOODBODY = 20
FOODCOLOR = WHITE
foodx =[]
foody =[]
for i in range (3):
    foodx.append(random.randint(0, (SCREENSIZE - 20) / 20) * 20)
    foody.append(random.randint(0, (SCREENSIZE - 20) / 20) * 20)





#img snake
img = pygame.Surface((SNAKEBODY, SNAKEBODY))
img.fill(SNAKECOLOR)
xs = [300, 300, 300, 300, 300]
ys = [280, 260, 240, 220, 200]
dire = "DOWN"


#img food
imgfood = pygame.Surface((FOODBODY,FOODBODY))
imgfood.fill(FOODCOLOR)

# other elements in the game
clock = pygame.time.Clock()


# collide
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
        return True
    else:
        return False


# end of the game
def die():
    global keepGoing
    global point
    screen.fill(WHITE)
    f = pygame.font.SysFont("Arial", 50)
    t = f.render("You score was "+str(point), True, BLACK)
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(2000)
    keepGoing = False


while keepGoing:
    clock.tick(10)
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

    # touch the wall
    if xs[0] < 0 or xs[0] > SCREENSIZE - SNAKEBODY or ys[0] < 0 or ys[0] > SCREENSIZE - SNAKEBODY:
        die()



    #eat food
    for i in range (len(foodx)):
        if collide(xs[0],foodx[i],ys[0],foody[i],FOODBODY,FOODBODY,FOODBODY,FOODBODY):
            print 'eat food'
            point+= 1
            #接入蛇身体
            xs.append(SCREENSIZE)
            ys.append(SCREENSIZE)
            #生成新的食物坐标
        
            foodx[i]=random.randint(0, (SCREENSIZE - 20) / 20) * 20
            foody[i]=random.randint(0, (SCREENSIZE - 20) / 20) * 20


    # touch the body
    i = len(xs) - 1
    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], SNAKEBODY, SNAKEBODY, SNAKEBODY, SNAKEBODY):
            pygame.time.wait(2000)
            die()
        i -= 1

    # update body
    i = len(xs) - 1
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

    for i in range(3):
        screen.blit(imgfood,(foodx[i], foody[i]))

    # foodx = random.randint(0, (SCREENSIZE - 20) / 20) * 20
    # foody = random.randint(0, (SCREENSIZE - 20) / 20) * 20


    pygam.display.update()

pygame.quit()