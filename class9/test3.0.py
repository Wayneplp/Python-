import pygame

pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("First Pygame Canvas")

keepGoing = True
Red = (255,0,0)

while keepGoing:
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        keepGoing = False
	pygame.draw.circle(screen,Red,(250,250),50)
	
	pygame.display.update()

pygame.quit() 
	