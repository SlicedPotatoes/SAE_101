import pygame
import ui.spriteLoader as sl
import gameState as gs
import utils

"""
Variable globale lié a l'affichage
"""
screen_size = (1280, 720)

board_offset_x = (screen_size[0] // 2) - ((40 * 6) + 20) // 2
board_offset_y = (screen_size[1] // 2) - ((40 * 16) + 20) // 2

color_picker_offset_x = 120
color_picker_offset_y = 120

color_radius = 15

btn_play_size = (300, 85)
btn_play_center = (screen_size[0] // 2, screen_size[1] // 2)

btn_return_size = (300, 85)
btn_return_center = (200, 85)

btn_restart_size = (300, 85)
btn_restart_center = (screen_size[0] // 2, screen_size[1] // 2)

"""
Fonction d'affichage des différents écrants
"""

# Affiche le background animée
def drawBackground(gameState:gs.gameState):
  gameState.screen.blit(gameState.sc.background[gameState.currentBackgroundIndex], (0, 0))
  gameState.currentBackgroundIndex = (gameState.currentBackgroundIndex + 1) % len(gameState.sc.background)

# Affichage du menu principal
def mainMenu(gameState:gs.gameState):
  def drawBtnPlay(pos:tuple):
    x_left = btn_play_center[0] - (btn_play_size[0] // 2)
    x_right = btn_play_center[0] + (btn_play_size[0] // 2)
    y_top = btn_play_center[1] - (btn_play_size[1] // 2) - 1
    y_bottom = btn_play_center[1] + (btn_play_size[1] // 2) + 1

    if(pos[0] >= x_left and pos[0] <= x_right and pos[1] >= y_top and pos[1] <= y_bottom):
      gameState.screen.blit(gameState.sc.s['sprite_button_play_hover'], (x_left, y_top))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_play'], (x_left, y_top))

  pos = pygame.mouse.get_pos()
  
  # Play button
  drawBtnPlay(pos)
  
  # Credit button
  # Quit button

# Affichage de l'écran de jeu
def gameScreen(gameState:gs.gameState, isEndScreen:bool):
  def drawBtnReturn(pos:tuple):
    x_left = btn_return_center[0] - (btn_return_size[0] // 2)
    x_right = btn_return_center[0] + (btn_return_size[0] // 2)
    y_top = btn_return_center[1] - (btn_return_size[1] // 2) - 1
    y_bottom = btn_return_center[1] + (btn_return_size[1] // 2) + 1

    if(pos[0] >= x_left and pos[0] <= x_right and pos[1] >= y_top and pos[1] <= y_bottom):
      gameState.screen.blit(gameState.sc.s['sprite_button_return_hover'], (x_left, y_top))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_return'], (x_left, y_top))

  pos = pygame.mouse.get_pos()

  showBoard(gameState.screen, gameState.sc)
  showColorPicker(gameState.screen, gameState.sc, gameState.colors)
  showSecret(gameState.screen, gameState.sc, gameState.colors, gameState.secret)
  showProposal(gameState)

  if(not isEndScreen):
    drawBtnReturn(pos)

  i = 0

  while(i < len(gameState.lines)):
    if(len(gameState.lines[i]) == 5):
      showFeedback(gameState.screen, 16 - i, gameState.feedback(i))
    
    i += 1

# Affichage de la modale de fin de jeu
def endGameModal(gameState:gs.gameState):
  def drawBtnReset(pos:tuple):
    hitbox = utils.getHitboxRect(btn_restart_center, btn_restart_size)

    if(pos[0] >= hitbox[0] and pos[0] <= hitbox[1] and pos[1] >= hitbox[2] and pos[1] <= hitbox[3]):
      gameState.screen.blit(gameState.sc.s['sprite_button_restart_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_restart'], (hitbox[0], hitbox[2]))
  pos = pygame.mouse.get_pos()
  
  width = 720
  height = 360

  left = (screen_size[0] // 2) - (width // 2)
  top = (screen_size[1] // 2) - (height // 2)
    
  pygame.draw.rect(gameState.screen, (225,127,0), [left, top, width, height])

  text1 = "GG"
  text2 = "FF"
  text3 = "Nombre d'essais : " + str(len(gameState.lines))

  myfont1 = pygame.font.SysFont("monospace", 70)
  myfont2 = pygame.font.SysFont("monospace", 20)
  label1 = myfont1.render(text1 if gameState.win else text2, 1, (0,0,0))
  left = (screen_size[0] // 2) - label1.get_size()[0] // 2
  top = (screen_size[1] // 2) - label1.get_size()[1] // 2
  gameState.screen.blit(label1, (left, top))

  if(gameState.win):
    label2 = myfont2.render(text3, 1, (0,0,0))
    leftTry = (screen_size[0] // 2) - (2 * label1.get_size()[0]) + 40
    topTry = (screen_size[1] // 2) + label1.get_size()[1] // 2
    gameState.screen.blit(label2, (leftTry, topTry))

  drawBtnReset(pos)

"""
Sous probleme des fonction d'affichage des différents écrants
"""

# Dessiner une couleur dans le plateau
def drawColor(f:pygame.Surface, sc:sl.sprite_collection, colors:list, colorIndex:int, row, col):
  f.blit(sc.s[colors[colorIndex]], [board_offset_x + 5 + 40 * col, board_offset_y + 23 + 40 * row])

# Enlever une couleur du plateau
def removeColor(f:pygame.Surface, sc:sl.sprite_collection, row, col):
  f.blit(sc.s['sprite_case_color'], (board_offset_x + 40 * col, board_offset_y + 60 + 40 * row))

# Afficher le plateau
def showBoard(f:pygame.Surface, sc:sl.sprite_collection):
  # Affichage des cases pour la combinaison secrete
  for col in range(5):
    f.blit(sc.s['sprite_case_color'], (board_offset_x + 40 * col, board_offset_y))

  # Affichage des cases pour les propositions du joueur et du feedback
  for row in range(15):
    for col in range(5):
      f.blit(sc.s['sprite_case_color'], (board_offset_x + 40 * col, board_offset_y + 60 + 40 * row)) # Case proposition joueur
      f.blit(sc.s['sprite_case_color'], (board_offset_x + 220, board_offset_y + 60 + 40 * row))  # Case feedback

# Afficher les buttons de choix de couleur
def showColorPicker(f:pygame.Surface, sc:sl.sprite_collection, colors:list):
  # Button choix couleur
  for i in range(len(colors)):
     f.blit(sc.s[colors[i]], [color_picker_offset_x, color_picker_offset_y + 40 * i])

  # Button remove
  pygame.draw.circle(f, (128, 128, 128), [color_picker_offset_x + 15, color_picker_offset_y + 20 + 40 * 9], 15)
  pygame.draw.circle(f, (0, 0, 0), [color_picker_offset_x + 15, color_picker_offset_y + 20 + 40 * 9], 15, 1)

# Afficher le secret
def showSecret(f:pygame.Surface, sc:sl.sprite_collection, colors:list, secret:list):
  for i in range(len(secret)):
    color = colors[secret[i]]
    f.blit(sc.s[color], [board_offset_x + 5 + 40 * i, board_offset_y + 3])

# Afficher les couleurs sur le plateau
def showProposal(gameState:gs.gameState):
  i = 0
  while(i < len(gameState.lines)):
    j = 0
    while(j < len(gameState.lines[i])):
      drawColor(gameState.screen, gameState.sc, gameState.colors, gameState.lines[i][j], 15 - i, j)
      j += 1
    i += 1

# Afficher le feedback
def showFeedback(f:pygame.Surface, row, res):
  x = board_offset_x + 220
  y = board_offset_y + 20 + 40 * (row-1)

  centres = [(x + 6, y + 6), (x + 6, y + 34), (x + 20, y + 20), (x + 34, y + 6), (x + 34, y + 34)]

  i = 0
  while i < res[0]:
    pygame.draw.circle(f, (255, 255, 255), centres[i], 4)
    i = i + 1
  j = 0
  while j < res[1]:
      pygame.draw.circle(f, (0, 0, 0), centres[i], 4)
      i = i + 1
      j = j + 1