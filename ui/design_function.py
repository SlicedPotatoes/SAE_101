import pygame
import ui.spriteLoader as sl
import ui.design_function as df
import gameState as gs

"""
Variable globale lié a l'affichage
"""

board_offset_x = 300
board_offset_y = 0

btn_play_size = (300, 85)
btn_play_center = ((1280 // 2), (720 // 2))

"""
Fonction d'affichage des différents écrants
"""

def drawBackground(gameState:gs.gameState):
  gameState.screen.blit(gameState.sc.backgroundMenu[gameState.currentBackgroundIndex], (0, 0))
  gameState.currentBackgroundIndex = (gameState.currentBackgroundIndex + 1) % len(gameState.sc.backgroundMenu)

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
def gameScreen(gameState:gs.gameState):
  df.showBoard(gameState.screen, gameState.sc)
  df.showColorPicker(gameState.screen, gameState.sc, gameState.colors)
  gameState.isStaticElementsDisplayed = True
  showSecret(gameState.screen, gameState.sc, gameState.colors, gameState.secret)
  showProposal(gameState)

  i = 0

  while(i < len(gameState.lines)):
    if(len(gameState.lines[i]) == 5):
      showFeedback(gameState.screen, 16 - i, gameState.feedback(i))
    
    i += 1

"""
Sous probleme des fonction d'affichage des différents écrants
"""

# Dessiner une couleur dans le plateau
def drawColor(f:pygame.Surface, sc:sl.sprite_collection, colors:list, colorIndex:int, row, col):
  f.blit(sc.s[colors[colorIndex]], [board_offset_x + 5 + 40 * col, board_offset_y + 25 + 40 * row])

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
     f.blit(sc.s[colors[i]], [60, 65 + 40 * i])

  # Button remove
  pygame.draw.circle(f, (128, 128, 128), [75, 80 + 40 * 9], 15)
  pygame.draw.circle(f, (0, 0, 0), [75, 80 + 40 * 9], 15, 1)

# Afficher le secret
def showSecret(f:pygame.Surface, sc:sl.sprite_collection, colors:list, secret:list):
  for i in range(len(secret)):
    color = colors[secret[i]]
    f.blit(sc.s[color], [board_offset_x + 5 + 40 * i, board_offset_y + 5])

# Afficher les pionts sur le plateau
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