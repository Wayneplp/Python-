import pygame

SCREENWIDTH = 700
SCREENHEIGHT = 800
pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
keepGoing = True
lmoving = False
rmoving = False
dmoving = False
umoving = False

radius = 10
RED = (255, 0, 0)
BLACK = (0,0,0)
x = 500
y = 200
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                umoving = True
            elif event.key == pygame.K_DOWN:
                dmoving = True
            elif event.key == pygame.K_RIGHT:
                rmoving = True
            elif event.key == pygame.K_LEFT:
                lmoving = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                lmoving = False
            if event.key == pygame.K_RIGHT:
                rmoving = False
            if event.key == pygame.K_UP:
                umoving = False
            if event.key ==pygame.K_DOWN:
                dmoving = False
    if lmoving:
        x = x-1
    if rmoving:
        x = x+1
    if dmoving:
        y = y+1
    if umoving:
        y = y-1
        
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.update()

pygame.quit()