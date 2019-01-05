SCREENWIDTH = 800
SCREENHEIGHT = 600
import pygame
pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
pygame.display.set_caption("Draw A Circle When Click")

keepGoing = True
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
color =RED
hasDrawn = False
moving = False
radius = 5
x = 250
y = 250
lmoving = False
rmoving = False
umoving = False
dmoving = False
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_g:
                color = GREEN      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                radius = radius + 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y-=5
                umoving = True
            elif event.key == pygame.K_DOWN:
                y+=5
            elif event.key == pygame.K_RIGHT:
                x+=5
            elif event.key == pygame.K_LEFT:
                x-=5
        if event.type == pygame.KEYDOWN:
            if rmoving == True:
                screen.fill(WHITE)
                pygame.draw.circle(screen,color,(x,y),radius)
    pygame.display.update()
pygame.quit()
