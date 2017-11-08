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

	def move(self, direction):
		if direction == "up":
			self.coords[1] -= speed
		if direction == "down":
			self.coords[1] += speed
		if direction == "right":
			self.coords[0] += speed
		if direction == "up":
			self.coords[0] -= speed

	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.coords, self.size))

player_size = [25, 25]

bob = Player(
	pygame.Color("blue"),
	[0, 0],
	player_size,
	5
)

carpet = Player(
	pygame.Color("black"),
	[275,275],
	player_size,
	5
)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		bob.move('right')
	elif keys[pygame.K_LEFT]:
		bob.move('left')
	if keys[pygame.K_UP]:
 		bob.move('up')
	elif keys[pygame.K_DOWN]:
 		bob.move('down')


	window.fill(pygame.Color("white"))
	bob.draw(window)
	carpet.draw(window)
	pygame.display.update()
	clock.tick(60)