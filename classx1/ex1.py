import pygame

SCREENWIDTH = 800
SCREENHEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
pygame.display.set_caption("Draw A Circle When Click")

keepGoing = True

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
color =RED
hasDrawn = False
moving = False
radius = 5
x = 250
y = 250
while keepGoing:
    for event in pygame.event.get():
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
        
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONDOWN:          
            moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            moving = False            
        if event.type == pygame.MOUSEMOTION:  
        	if moving ==True:
        	    position = event.pos
        	    pygame.draw.circle(screen,color,position,radius)
    pygame.display.update()
pygame.quit()