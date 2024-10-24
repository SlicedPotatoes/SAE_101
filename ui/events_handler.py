import pygame
import gameState as gs
import utils
import ui.design_function as df

# Gestion des clicks en fonction de l'écran actuellement affiché
def mouse_click(gameState: gs.gameState)->None:
  if(gameState.currentScreen == 'main_menu'):
    mainMenuClick(gameState)
  elif gameState.currentScreen == 'game_screen':
    gameScreenClick(gameState)
  elif gameState.currentScreen == 'end_screen':
    gameEndClick(gameState)
  elif gameState.currentScreen == 'credits_screen':
    creditsClick(gameState)
  else:
    print("Problème avec currentScreen:", gameState.currentScreen)

# Gestion des clicks sur l'écran principal
def mainMenuClick(gameState:gs.gameState)->None:
  pos = pygame.mouse.get_pos()

  # Récuperer les hitbox des différents boutons
  play_btn_hitbox = utils.getHitboxRect(df.btn_play_center, df.btn_play_size)
  credit_btn_hitbox = utils.getHitboxRect(df.btn_credit_center, df.btn_credit_size)
  quit_btn_hitbox = utils.getHitboxRect(df.btn_quit_center, df.btn_quit_size)

  # Click btn jouer
  if(utils.inRectHitbox(pos, play_btn_hitbox)):
    gameState.reset('game_screen')
  
  # Click btn credit
  elif(utils.inRectHitbox(pos, credit_btn_hitbox)):
    gameState.reset('credits_screen')
  
  # Click btn quitter
  elif(utils.inRectHitbox(pos, quit_btn_hitbox)):
    gameState.running = False

# Gestion des clicks dans le jeu
def gameScreenClick(gameState:gs.gameState)->None:
  pos = pygame.mouse.get_pos()
  return_btn_hitbox = utils.getHitboxRect(df.btn_return_center, df.btn_return_size)
  restart_btn_hitbox = utils.getHitboxRect(df.btn_restart_center_gs, df.btn_return_size)
  remove_btn_hitbox = utils.getHitboxRect(df.btn_remove_center, df.btn_remove_size)

  # Click btn retour
  if(utils.inRectHitbox(pos, return_btn_hitbox)):
    gameState.reset('main_menu')

  # Click btn restart
  elif(utils.inRectHitbox(pos, restart_btn_hitbox)):
    gameState.reset('game_screen')

  # Click enlever couleur du plateau
  elif(utils.inRectHitbox(pos, remove_btn_hitbox)):
    if(len(gameState.lines[-1]) > 0):
      del gameState.lines[-1][-1]

  # Click ajouter couleur plateau
  elif(len(gameState.lines[-1]) < 5 and len(gameState.lines) <= 15):
    for i in range(len(gameState.colors)) :
      if utils.distance(pos, [df.color_picker_offset_x + df.color_radius, df.color_picker_offset_y + df.color_radius + 40 * i]) < df.color_radius:
        gameState.lines[-1].append(i)

# Gestion des clicks de la modal de fin
def gameEndClick(gameState:gs.gameState)->None:
  pos = pygame.mouse.get_pos()
  restart_btn_hitbox = utils.getHitboxRect(df.btn_restart_center_es_win if gameState.win else df.btn_restart_center_es_loose, df.btn_restart_size)

  # Click btn restart
  if(utils.inRectHitbox(pos, restart_btn_hitbox)):
    gameState.reset('game_screen')

# Gestion des clicks de l'écran credits
def creditsClick(gameState:gs.gameState)->None:
  pos = pygame.mouse.get_pos()
  return_btn_hitbox = utils.getHitboxRect(df.btn_return_center, df.btn_return_size)

  # Click btn return
  if(utils.inRectHitbox(pos, return_btn_hitbox)):
    gameState.reset('main_menu')