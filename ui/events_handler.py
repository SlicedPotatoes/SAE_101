import pygame
import gameState as gs
import utils
import ui.design_function as df

# Fonction qui retourne vrai dans le cas ou un click de la souris ce trouve dans la hitbox d'un rectangle
def clickRect(pos, hitbox):
  return pos[0] >= hitbox[0] and pos[0] <= hitbox[1] and pos[1] >= hitbox[2] and pos[1] <= hitbox[3]

# Gestion des clicks en fonction de l'écran actuellement afficher
def mouse_click(gameState: gs.gameState):
  if(gameState.currentScreen == 'main_menu'):
    mainMenuClick(gameState)
  elif gameState.currentScreen == 'game_screen':
    gameScreenClick(gameState)
  elif gameState.currentScreen == 'end_screen':
    gameEndClick(gameState)
  else:
    print("Problème avec currentScreen:", gameState.currentScreen)

# Gestion des clicks sur l'ecran principal
def mainMenuClick(gameState:gs.gameState):
  pos = pygame.mouse.get_pos()

  play_btn_hitbox = utils.getHitboxRect(df.btn_play_center, df.btn_play_size)

  # Click btn jouer
  if(clickRect(pos, play_btn_hitbox)):
    gameState.reset('game_screen')

# Gestion des clicks dans le jeu
def gameScreenClick(gameState:gs.gameState):
  pos = pygame.mouse.get_pos()
  return_btn_hitbox = utils.getHitboxRect(df.btn_return_center, df.btn_return_size)

  # Click btn retour
  if(clickRect(pos, return_btn_hitbox)):
    gameState.reset('main_menu')

  # Click enlever couleur du plateau
  elif utils.distance(pos, [df.color_picker_offset_x + df.color_radius, df.color_picker_offset_y + df.color_radius + 40 * 9]) < df.color_radius:
    if(len(gameState.lines[-1]) > 0):
      del gameState.lines[-1][-1]

  # Click ajouter couleur plateau
  elif(len(gameState.lines[-1]) < 5 and len(gameState.lines) <= 15):
    for i in range(len(gameState.colors)) :
      if utils.distance(pos, [df.color_picker_offset_x + df.color_radius, df.color_picker_offset_y + df.color_radius + 40 * i]) < df.color_radius:
        gameState.lines[-1].append(i)

# Gestion des clicks de la modal de fin
def gameEndClick(gameState:gs.gameState):
  pos = pygame.mouse.get_pos()
  restart_btn_hitbox = utils.getHitboxRect(df.btn_restart_center, df.btn_restart_size)

  if(clickRect(pos, restart_btn_hitbox)):
    gameState.reset('game_screen')