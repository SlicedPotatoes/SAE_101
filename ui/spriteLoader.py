import pygame

class sprite_collection:
  def __init__(self) -> None:
    root = "sprite\\"
    hashmap = {
      'sprite_case_color': 'case_color.png',
      
      'sprite_color_black': 'color_back.png',
      'sprite_color_white': 'color_white.png',
      'sprite_color_gray': 'color_gray.png',
      'sprite_color_blue': 'color_blue.png',
      'sprite_color_red': 'color_red.png',
      'sprite_color_green': 'color_green.png',
      'sprite_color_orange': 'color_orange.png',
      'sprite_color_pink': 'color_pink.png',

      'sprite_button_play': 'button_play.png',
      'sprite_button_play_hover': 'button_play_hover.png',
    }

    self.s = {}
    for s in hashmap.items():
      self.s[s[0]] = pygame.image.load(root + s[1])

    i = 1

    self.backgroundMenu = []

    while(i <= 54):
      numStr = str(i)
      numStr = '0' * (2 - len(numStr)) + numStr

      i += 1

      self.backgroundMenu.append(pygame.image.load(root + "background_menu\\frame-" + numStr + ".png"))
