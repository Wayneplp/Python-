import pygame
from pygame.locals import *
RED = (255,0,0)
BLACK = (0,0,0)
keepGoing = True  
SNAKEBODY = 20
SNAKECOLOR = RED
xs = [300,300,300,300,300]
ys = [280,260,240,220,200]
SCREENWIDTH = 1000
SCREENHEIGHT = 1000
img = pygame.Surface((SNAKEBODY,SNAKEBODY))
img.fill(SNAKEBODY)
dire = "DOWN"
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
xspeend = 1
yspeend = 1
while keepGoing:
	for event in pygame.event.get():
		if event.type == QUIT:
			keepGoing = False
		elif event.type == KEYDOWN:
		    if event.key == K_UP and dire != "DOWN":
				dire = "UP"
				yspeend +=1
				elif event.key == K_DOWN and dire != "UP":
		    	dire = "DOWN"
		    	yspeend -=1
		    elif event.key == K_RIGHT and dire != "LEFT":
		        dire = "RIGHT"
		        xspeend -=1
		    elif event.key == K_LEFT and dire != "RIGHT":
		    	dire = "LEFT"
		    	xspeend +=1
	
    # draw snakebody
	i = len(xs) -1
	while i>=1:
		xs[i] = xs[i-1]
		ys[i] = ys[i-1]
		i -=1
	
    #draw snakehead 
	if dire == 'UP':
		ys[0] = ys[0] + SNAKEBODY
	elif dire == 'DOWN':
		ys[0] = ys[0] - SNAKEBODY
	elif dire == 'LEFT':
		xs[0] = xs[0]- SNAKEBODY
	elif dire == 'RIGHT':
		xs[0] = xs[0] - SNAKEBODY
	screen.fill(BLACK)
	for i in range(0,len(xs)):
		screen.blit(img,(xs[i],ys[i]))
		pygame.display.update()

pygame.quit()



		




