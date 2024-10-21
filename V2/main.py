import pygame
import ui.design_function as df
import ui.spriteLoader as sl

# pygame setup
pygame.init()

sprite_collection = sl.sprite_collection()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

colors = [
  'sprite_color_black', 
  'sprite_color_white',
  'sprite_color_gray',
  'sprite_color_blue',
  'sprite_color_red',
  'sprite_color_green',
  'sprite_color_orange', 
  'sprite_color_pink',
]

# static display
screen.fill("white")
df.showBoard(screen, sprite_collection)
df.showColorPicker(screen, sprite_collection, colors)

while running:
  # poll for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()
  clock.tick(60)