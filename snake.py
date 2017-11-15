import pygame
from random import *
count_1 = 0
count_2 = 0
class Player:
  def __init__(self, color, coords, size, speed):
    self.color = color
    self.initial_coords = list(coords)
    self.coords = coords
    self.size = size
    self.speed = speed

  def move(self, direction):
    if direction == 'up':
      self.coords[1] -= self.speed
    elif direction == 'down':
      self.coords[1] += self.speed
    elif direction == 'left':
      self.coords[0] -= self.speed
    else:
      self.coords[0] += self.speed

  def draw(self, window):
    pygame.draw.rect(window, self.color, (self.coords, self.size))

  def check_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.coords[i] < 0):
        self.speed = 0
        self.color = pygame.Color("cyan")
      elif (self.coords[i] >= screen_size[i] - self.size[i]):
        self.speed = 0
        self.color = pygame.Color("cyan")

  def chaser_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.coords[i] < 0):
        self.coords[i] = 0
      elif (self.coords[i] >= screen_size[i] - self.size[i]):
        self.coords[i] = screen_size[i] - self.size[i]


  def has_collided(self, player):
    return ((self.coords[0] < player.coords[0] + player.size[0]) and
            (player.coords[0] < self.coords[0] + self.size[0]) and
            (self.coords[1] < player.coords[1] + player.size[1]) and
            (player.coords[1] < self.coords[1] + self.size[1]))

  def reset(self):
    self.coords = list(self.initial_coords)
  def random_reset(self):
    self.coords = [randint(0, 700), 680]

WINDOW_SIZE = [1000, 700]
PLAYER_SIZE = [20, 20]
ran_pos_1 = randint(0, 700)
ran_pos_2 = randint(500, 700)
player1 = Player(
  pygame.Color('red'),
  [950, 0],
  [50, 50],
  11
)
player2 = Player(
  pygame.Color('blue'),
  [ran_pos_1, ran_pos_2],
  PLAYER_SIZE,
  2
)
player3 = Player(
  pygame.Color("purple"),
  [0, 0],
  [50, 50],
  11
)

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Red player's score is:")
      print(count_1)
      print("Purple player's score is:")
      print(count_2)
      exit()
  player2.move('up')

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    player1.move('right')
  elif keys[pygame.K_LEFT]:
    player1.move('left')
  if keys[pygame.K_UP]:
    player1.move('up')
  elif keys[pygame.K_DOWN]:
    player1.move('down')

  if keys[pygame.K_d]:
    player3.move('right')
  elif keys[pygame.K_a]:
    player3.move('left')
  if keys[pygame.K_w]:
    player3.move('up')
  elif keys[pygame.K_s]:
    player3.move('down')

  player1.chaser_boundaries(WINDOW_SIZE)
  player2.check_boundaries(WINDOW_SIZE)
  player3.chaser_boundaries(WINDOW_SIZE)

  if player1.has_collided(player2):
    player2.random_reset()
    count_1 = count_1 + 1
    player2.speed = player2.speed + 0.2
  if player3.has_collided(player2):
    player2.random_reset()
    count_2 = count_2 + 1
    player2.speed = player2.speed + 0.1
  window.fill(pygame.Color('cyan'))

  player1.draw(window)
  player2.draw(window)
  player3.draw(window)

  pygame.display.update()
  clock.tick(60)
