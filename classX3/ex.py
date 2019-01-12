import pygame

SCREENWIDTH = 800
SCREENHEIGHT = 800

pygame.init()
pygame.display.set_caption("贪吃蛇小游戏")
screen = pygame.display.set_mode([SCREENHEIGHT,SCREENWIDTH])
keepGoing = True
while keepGoing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT():
			keepGoing = False
		if event.key == pygame.K_UP:
		 
