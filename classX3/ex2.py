import pygame
import random
SCREENWIDTH = 800
SCREENHEIGHT = 800

pygame.init()

screen = pygame.display.set_mode([SCREENHEIGHT, SCREENWIDTH])
keepGoing = True
umoving = False
dmoving = False
rmoving = False
lmoving = False
x1 = 500
y1 = 200
x2 = 200
y2 = 500
BLACK = (0,0,0)
RED = (255,0,0)
WHITE =(255,255,255)
radius = 10
y1speed = 0
y2speed = random.randint(-5,5)
x1speed = 0
x2speed = random.randint(-5,5)
acc = 1
while x2speed == 0 :
    x2speed = random.randint(-5,5)
while y2speed ==0:
    y2speed =random.randint(-5,5)

ballmoving = False
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y1speed -= acc
                x1speed = 0
            if event.key == pygame.K_DOWN:
                y1speed += acc
                x1speed = 0
            if event.key == pygame.K_RIGHT:
                x1speed += acc
                y1speed = 0
            if event.key == pygame.K_LEFT:
                x1speed -= acc
                y1speed = 0
            if event.key ==pygame.K_w:
                y2speed -=1
                x2speed = 0
            if event.key == pygame.K_s:
                y2speed +=1
                x2speed = 0
            if event.key ==pygame.K_a:
                x2speed -=1
                y2speed =0
            if event.key ==pygame.K_d:
                x2speed +=1
                y2speed = 0
    if x1+radius <= 0 or x1+radius >=SCREENWIDTH:
        x1speed *= -1
    if y1+radius <= 0 or y1+radius>=SCREENHEIGHT:
        y1speed *= -1
    if x2+radius <= 0 or x2+radius >=SCREENWIDTH:
        x2speed *= -1
    if y2+radius <= 0 or y2+radius>=SCREENHEIGHT:
        y2speed *= -1
    x1 += x1speed
    y1 += y1speed
    x2 += x2speed
    y2 += y2speed
    if (x1 - x2)**2 + (y1 -y2)**2 <= (2*radius)**2:
        ballmoving = True

    screen.fill(BLACK)
    pygame.draw.circle(screen,WHITE,(x1,y1),radius)
    pygame.draw.circle(screen, RED, (x2, y2), radius)
    if not ballmoving :
        pygame.display.update()

pygame.quit()

