import pygame

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	window.fill(pygame.Color("white"))
	pygame.display.update()
	clock.tick(60)