import pygame
import ui.spriteLoader as sl
import gameState as gs
import utils

"""
Variable globale lié a l'affichage
"""
screen_size = (1280, 720)

color_radius = 15

board_offset_x = (screen_size[0] // 2) - ((40 * 6) + 20) // 2
board_offset_y = (screen_size[1] // 2) - ((40 * 16) + 20) // 2
background_board_size = (162, 558)

color_picker_offset_x = 447
color_picker_offset_y = 280

btn_remove_size = (56, 61)
btn_remove_center = (color_picker_offset_x + color_radius, color_picker_offset_y + 20 + 40 * 9)

rules_size = (313, 520)
rules_center = (50 + rules_size[0] // 2, 170 + rules_size[1] // 2)

btn_play_size = (300, 85)
btn_play_center = (screen_size[0] // 2, 300)

btn_credit_size = (300, 85)
btn_credit_center = (screen_size[0] // 2, btn_play_center[1] + btn_play_size[1] + 20)

btn_quit_size = (300, 85)
btn_quit_center = (screen_size[0] // 2, btn_credit_center[1] + btn_credit_size[1] + 20)

btn_return_size = (300, 85)
btn_return_center = (200, board_offset_y + btn_return_size[1] // 2)

btn_restart_size = (300, 85)
btn_restart_center_gs = (screen_size[0] - (btn_restart_size[0] // 2) - 50, board_offset_y + btn_return_size[1] // 2)
btn_restart_center_es_loose = (screen_size[0] // 2, screen_size[1] // 2 + 100)
btn_restart_center_es_win = (screen_size[0] // 2, screen_size[1] // 2 + 155)

"""
Fonction d'affichage des différents écrans
"""

# Affiche le background animée
def drawBackground(gameState:gs.gameState)->None:
  gameState.screen.blit(gameState.sc.background[gameState.currentBackgroundIndex], (0, 0))
  gameState.currentBackgroundIndex = (gameState.currentBackgroundIndex + 1) % len(gameState.sc.background)

# Affichage du menu principal
def mainMenu(gameState:gs.gameState)->None:
  def drawBtnPlay(pos:tuple)->None:
    hitbox = utils.getHitboxRect(btn_play_center, btn_play_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_play_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_play'], (hitbox[0], hitbox[2]))
  def drawBtnCredits(pos:tuple)->None:
    hitbox = utils.getHitboxRect(btn_credit_center, btn_credit_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_credits_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_credits'], (hitbox[0], hitbox[2]))
  def drawBtnQuit(pos:tuple)->None:
    hitbox = utils.getHitboxRect(btn_quit_center, btn_quit_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_quit_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_quit'], (hitbox[0], hitbox[2]))
  
  pos = pygame.mouse.get_pos()
  
  left = (screen_size[0] // 2) - (592 // 2)
  top = btn_play_center[1] - (btn_play_size[1] // 2) - 146 - 40

  gameState.screen.blit(gameState.sc.s['sprite_logo'], (left, top))

  drawBtnPlay(pos)
  drawBtnCredits(pos)
  drawBtnQuit(pos)

# Affichage de l'écran de jeu
def gameScreen(gameState:gs.gameState, isEndScreen:bool):
  def drawBtnReturn(pos:tuple)->None:
    hitbox = utils.getHitboxRect(btn_return_center, btn_return_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_return_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_return'], (hitbox[0], hitbox[2]))
  def drawBtnRestart(pos:tuple)->None:
    hitbox = utils.getHitboxRect(btn_restart_center_gs, btn_return_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_restart_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_restart'], (hitbox[0], hitbox[2]))
  
  pos = pygame.mouse.get_pos()

  showBoard(gameState.screen, gameState.sc)
  showRules(gameState.screen, gameState.sc)
  showColorPicker(gameState)
  if(gameState.isGameEnd):
    showSecret(gameState.screen, gameState.sc, gameState.colors, gameState.secret)
  showProposal(gameState)

  gameState.screen.blit(gameState.sc.s['sprite_tag_chat'], (780, 170))

  gameState.screen.blit(gameState.sc.chat[gameState.currentChatIndex], (780, 180))
  gameState.currentChatIndex = (gameState.currentChatIndex + 1) % len(gameState.sc.chat)

  if(not isEndScreen):
    drawBtnReturn(pos)
    drawBtnRestart(pos)

  i = 0
  while(i < len(gameState.lines)):
    if(len(gameState.lines[i]) == 5):
      showFeedback(gameState.screen, gameState.sc, 16 - i, gameState.feedback(i))
    i += 1

# Affichage de l'écran crédit
def creditsScreen(gameState:gs.gameState)->None:
  def drawBtnReturn(pos:tuple)->None:
    hitbox = utils.getHitboxRect(btn_return_center, btn_return_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_return_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_return'], (hitbox[0], hitbox[2]))

  pos = pygame.mouse.get_pos()
  drawBtnReturn(pos)

  left = screen_size[0] // 2 - 960 // 2
  top = screen_size[1] // 2 - 650 // 2

  gameState.screen.blit(gameState.sc.s['sprite_credits'], (left, top))

# Affichage de la modale de fin de jeu
def endGameModal(gameState:gs.gameState)->None:
  def drawBtnReset(posMouse:tuple, isWin:bool)->None:
    hitbox = utils.getHitboxRect(btn_restart_center_es_win if isWin else btn_restart_center_es_loose, btn_restart_size)

    if(utils.inRectHitbox(posMouse, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_restart_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_restart'], (hitbox[0], hitbox[2]))

  pos = pygame.mouse.get_pos()

  if(gameState.win):
    gameState.screen.blit(gameState.sc.s['sprite_win'], (0, 0))
    nbTry = str(len(gameState.lines))
    font = pygame.font.Font(gameState.font, 23)
    label = font.render(nbTry, 1, (0, 0, 0))

    gameState.screen.blit(label, [screen_size[0] // 2 + 100, screen_size[1] // 2 + 44])
  else:
    gameState.screen.blit(gameState.sc.s['sprite_loose'], (0, 0))

  drawBtnReset(pos, gameState.win)

"""
Sous probleme des fonction d'affichage des différents écrants
"""

# Dessiner une couleur dans le plateau
def drawColor(f:pygame.Surface, sc:sl.sprite_collection, colors:list, colorIndex:int, row:int, col:int)->None:
  f.blit(sc.s[colors[colorIndex]], [board_offset_x + 5 + 40 * col, board_offset_y + 23 + 40 * row])

# Afficher le plateau
def showBoard(f:pygame.Surface, sc:sl.sprite_collection)->None:
  cord = utils.getHitboxRect((screen_size[0] // 2, screen_size[1] // 2), background_board_size)
  pygame.draw.rect(f, (192, 185, 245), [cord[0] - 20, cord[2] + 20, background_board_size[0], background_board_size[1]])

  # Affichage des cases pour la combinaison secrete
  for col in range(5):
    f.blit(sc.s['sprite_case_color'], (board_offset_x + 40 * col, board_offset_y))

  # Affichage des cases pour les propositions du joueur et du feedback
  for row in range(15):
    for col in range(5):
      f.blit(sc.s['sprite_case_color'], (board_offset_x + 40 * col, board_offset_y + 60 + 40 * row)) # Case proposition joueur
    f.blit(sc.s['sprite_case_feedback'], (board_offset_x + 220, board_offset_y + 60 + 40 * row))  # Case feedback

# Afficher les buttons de choix de couleur
def showColorPicker(gameState:gs.gameState)->None:
  def drawBtnRemove(pos:tuple):
    hitbox = utils.getHitboxRect(btn_remove_center, btn_remove_size)

    if(utils.inRectHitbox(pos, hitbox)):
      gameState.screen.blit(gameState.sc.s['sprite_button_remove_hover'], (hitbox[0], hitbox[2]))
    else:
      gameState.screen.blit(gameState.sc.s['sprite_button_remove'], (hitbox[0], hitbox[2]))
  
  pos = pygame.mouse.get_pos()

  gameState.screen.blit(gameState.sc.s['sprite_background_colors_picker'], [color_picker_offset_x - 13, color_picker_offset_y - 11])

  # Button choix couleur
  for i in range(len(gameState.colors)):
     gameState.screen.blit(gameState.sc.s[gameState.colors[i]], [color_picker_offset_x, color_picker_offset_y + 40 * i])

     if(utils.distance(pos, [color_picker_offset_x + color_radius, color_picker_offset_y + color_radius + 40 * i]) < color_radius):
       gameState.screen.blit(gameState.sc.s['sprite_colors_picker_hover'], [color_picker_offset_x, color_picker_offset_y + 40 * i])

  drawBtnRemove(pos)

# Afficher le secret
def showSecret(f:pygame.Surface, sc:sl.sprite_collection, colors:list, secret:list)->None:
  for i in range(len(secret)):
    color = colors[secret[i]]
    f.blit(sc.s[color], [board_offset_x + 5 + 40 * i, board_offset_y + 3])

# Afficher les couleurs sur le plateau
def showProposal(gameState:gs.gameState)->None:
  i = 0
  while(i < len(gameState.lines)):
    j = 0
    while(j < len(gameState.lines[i])):
      drawColor(gameState.screen, gameState.sc, gameState.colors, gameState.lines[i][j], 15 - i, j)
      j += 1
    i += 1

# Afficher le feedback
def showFeedback(f:pygame.Surface, sc:sl.sprite_collection, row:int, res:int)->None:
  x = board_offset_x + 220
  y = board_offset_y + 20 + 40 * (row-1)

  centres = [(x + 4, y + 4), (x + 4, y + 23), (x + 15, y + 14), (x + 26, y + 4), (x + 26, y + 23)]

  i = 0
  while i < res[0]:
    f.blit(sc.s['sprite_feedback_bp'], centres[i])
    i = i + 1
  j = 0
  while j < res[1]:
    f.blit(sc.s['sprite_feedback_mp'], centres[i])
    i = i + 1
    j = j + 1

# Afficher les regles
def showRules(f:pygame.Surface, sc:sl.sprite_collection)->None:
  hitbox = utils.getHitboxRect(rules_center, rules_size)
  f.blit(sc.s['sprite_rules'], (hitbox[0], hitbox[2]))
