import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("First Pygame Canvas")
keepGoing = True
Red = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
color = [Red,GREEN,BLUE]
R = 10
hasNotDraw = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if hasNotDraw:
        	for i in range(50):
        		x = random.randint(200,600)
        		y = random.randint(200,600)
        		pygame.draw.circle(screen,color[i%3],(x,y),R)
        	hasNotDraw = False
    pygame.display.update()
pygame.quit()