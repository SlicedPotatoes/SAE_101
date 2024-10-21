import pygame

class sprite_collection:
  def __init__(self) -> None:
    root = "V2\\sprite\\"
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
    }

    self.s = {}

    for s in hashmap.items():
      self.s[s[0]] = pygame.image.load(root + s[1])