import pygame

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

class Player:
	def __init__(self, color, coords, size, speed):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.size = size
		self.speed = speed

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.coords, self.size))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	window.fill(pygame.Color("white"))
	pygame.display.update()
	clock.tick(60)