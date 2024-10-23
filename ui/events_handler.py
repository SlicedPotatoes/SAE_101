import pygame
import gameState as gs
import math
import ui.design_function as df

def distance(a:list,b:list)->float:
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

# Gestion des clicks en fonction de l'écran actuellement afficher
def mouse_click(gameState: gs.gameState):
  if(gameState.currentScreen == 'main_menu'):
    mainMenuClick(gameState)
  elif gameState.currentScreen == 'game_screen':
    gameScreenClick(gameState)
  elif gameState.currentScreen == 'end_screen':
    pass
  else:
    print("Problème avec currentScreen:", gameState.currentScreen)

def mainMenuClick(gameState:gs.gameState):
  pos = pygame.mouse.get_pos()

  play_btn_hitbox = (df.btn_play_center[0] - (df.btn_play_size[0] // 2), df.btn_play_center[0] + (df.btn_play_size[0] // 2), df.btn_play_center[1] - (df.btn_play_size[1] // 2) - 1, df.btn_play_center[1] + (df.btn_play_size[1] // 2) + 1)

  # Click btn jouer
  if(pos[0] >= play_btn_hitbox[0] and pos[0] <= play_btn_hitbox[1] and pos[1] >= play_btn_hitbox[2] and pos[1] <= play_btn_hitbox[3]):
    gameState.currentScreen = 'game_screen'
    gameState.isStaticElementsDisplayed = False

def gameScreenClick(gameState:gs.gameState):
  pos = pygame.mouse.get_pos()

  if distance(pos, [75, 80 + 40 * 9]) < 15:
    if(len(gameState.lines[-1]) > 0):
      #col = len(gameState.line) - 1
      #row = 16 - gameState.currentLine - 2
      #df.removeColor(gameState.screen, gameState.sc, row, col)

      del gameState.lines[-1][-1]

      

  if(len(gameState.lines[-1]) < 5):
    for i in range(len(gameState.colors)) :
      if distance(pos, [75, 80 + 40 * i]) < 15:
        gameState.lines[-1].append(i)

        #col = len(gameState.lines[-1]) - 1
        #row = 16 - len(gameState.lines) - 1
        #df.drawColor(gameState.screen, gameState.sc, gameState.colors, i, row, col)
        
