import pygame
import ui.spriteLoader as sl
import ui.events_handler as eh
import ui.design_function as df
import gameState as gs

# pygame setup
sprite_collection = sl.sprite_collection()

pygame.init()
pygame.display.set_caption('Mastermind')
pygame.display.set_icon(sprite_collection.s['icon'])

clock = pygame.time.Clock()

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
while gameState.running:
  gameState.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameState.running = False
    elif event.type == pygame.MOUSEBUTTONUP:
      eh.mouse_click(gameState)

  df.drawBackground(gameState)

  # Afficher le bon écran
  if gameState.currentScreen == 'main_menu':
    df.mainMenu(gameState)
  elif gameState.currentScreen == 'game_screen':
    df.gameScreen(gameState, False)
  elif gameState.currentScreen == 'end_screen':
    df.gameScreen(gameState, True)
    df.endGameModal(gameState)
  elif gameState.currentScreen == 'credits_screen':
    df.creditsScreen(gameState)
  else:
    print("Error: Screen not found")
    gameState.reset('main_menu')

  pygame.display.flip()
  clock.tick(10)