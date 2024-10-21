import pygame
import ui.spriteLoader as sl

def showBoard(f:pygame.Surface, sc:sl.sprite_collection):
  offset_x = 300
  offset_y = 0

  # Affichage des cases pour la combinaison secrete
  for col in range(5):
    f.blit(sc.s['sprite_case_color'], (offset_x + 40 * col, offset_y))

  # Affichage des cases pour les propositions du joueur et du feedback
  for row in range(15):
    for col in range(5):
      f.blit(sc.s['sprite_case_color'], (offset_x + 40 * col, offset_y + 60 + 40 * row)) # Case proposition joueur
      f.blit(sc.s['sprite_case_color'], (offset_x + 220, offset_y + 60 + 40 * row))  # Case feedback

def showColorPicker(f:pygame.Surface, sc:sl.sprite_collection, colors:list):
  for i in range(len(colors)):
     f.blit(sc.s[colors[i]], (75, 80 + 40 * i))

    #pygame.draw.circle(f,Marron,[75,80+40*9],15)
    #pygame.draw.circle(f,Noir,[75,80+40*9],15,1)
    #pygame.display.update()