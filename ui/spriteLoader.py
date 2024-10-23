import pygame

class sprite_collection:
  def __init__(self) -> None:
    root = "sprite\\"
    hashmap = {
      'sprite_case_color': 'game_screen\\case_color.png',
      
      'sprite_color_black': 'game_screen\\color_back.png',
      'sprite_color_white': 'game_screen\\color_white.png',
      'sprite_color_gray': 'game_screen\\color_gray.png',
      'sprite_color_blue': 'game_screen\\color_blue.png',
      'sprite_color_red': 'game_screen\\color_red.png',
      'sprite_color_green': 'game_screen\\color_green.png',
      'sprite_color_orange': 'game_screen\\color_orange.png',
      'sprite_color_pink': 'game_screen\\color_pink.png',

      'sprite_button_play': 'menu\\button_play.png',
      'sprite_button_play_hover': 'menu\\button_play_hover.png',

      'sprite_button_return': 'game_screen\\button_return.png',
      'sprite_button_return_hover': 'game_screen\\button_return_hover.png',

      'sprite_button_restart': 'end_screen\\button_restart.png',
      'sprite_button_restart_hover': 'end_screen\\button_restart_hover.png'
    }

    self.s = {}
    for s in hashmap.items():
      self.s[s[0]] = pygame.image.load(root + s[1])

    i = 1

    self.background = []

    while(i <= 54):
      numStr = str(i)
      numStr = '0' * (2 - len(numStr)) + numStr

      i += 1

      self.background.append(pygame.image.load(root + "background\\frame-" + numStr + ".png"))
