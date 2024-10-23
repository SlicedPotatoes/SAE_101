import pygame
import ui.spriteLoader as sl
import ui.events_handler as eh
import ui.design_function as df
import gameState as gs

# pygame setup
pygame.init()
pygame.display.set_caption('Mastermind')
#pygame.display.set_icon(Icon_name)

sprite_collection = sl.sprite_collection()
clock = pygame.time.Clock()
running = True

# Mastermind logic setup
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
gameState = gs.gameState(colors, sprite_collection)

# Main loop
while running:
  gameState.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP:
      eh.mouse_click(gameState)

  df.drawBackground(gameState)

  if gameState.currentScreen == 'main_menu':
    df.mainMenu(gameState)
  elif gameState.currentScreen == 'game_screen':
    df.gameScreen(gameState)
  elif gameState.currentScreen == 'end_screen':
    pass
  else:
    pass

  pygame.display.flip()
  clock.tick(10)