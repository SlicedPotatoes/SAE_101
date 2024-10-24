import pygame

class sprite_collection:
  def __init__(self)->None:
    root = "sprite\\"
    # Dictionnaire contenant la clé d'un sprite et son chemain
    hashmap = {
      'icon': 'icon.png',
      
      # Sprite GameScreen Case
      'sprite_case_color': 'game_screen\\case_color.png',
      'sprite_case_feedback': 'game_screen\\case_feedback.png',

      # Sprite GameScreen FeedBack
      'sprite_feedback_bp': 'game_screen\\feedback_bp.png',
      'sprite_feedback_mp': 'game_screen\\feedback_mp.png',
      
      # Sprite GameScreen Colors
      'sprite_color_black': 'game_screen\\color_black.png',
      'sprite_color_white': 'game_screen\\color_white.png',
      'sprite_color_gray': 'game_screen\\color_gray.png',
      'sprite_color_blue': 'game_screen\\color_blue.png',
      'sprite_color_red': 'game_screen\\color_red.png',
      'sprite_color_green': 'game_screen\\color_green.png',
      'sprite_color_orange': 'game_screen\\color_orange.png',
      'sprite_color_pink': 'game_screen\\color_pink.png',

      # Sprite GameScreen Tag chat
      'sprite_tag_chat': 'chat\\tag_chat.png',

      # Sprite GameScreen Btn Remove
      'sprite_button_remove': 'game_screen\\button_remove.png',
      'sprite_button_remove_hover': 'game_screen\\button_remove_hover.png',
      
      # Sprite Frame Container
      'sprite_background_colors_picker': 'game_screen\\background_colors_picker.png',
      'sprite_rules': 'game_screen\\rules.png',

      # Sprite Menu Btn Play
      'sprite_button_play': 'menu\\button_play.png',
      'sprite_button_play_hover': 'menu\\button_play_hover.png',

      # Sprite Btn Return
      'sprite_button_return': 'game_screen\\button_return.png',
      'sprite_button_return_hover': 'game_screen\\button_return_hover.png',

      # Sprite Btn Restart
      'sprite_button_restart': 'end_screen\\button_restart.png',
      'sprite_button_restart_hover': 'end_screen\\button_restart_hover.png',

      # Sprite Menu Btn Credits
      'sprite_button_credits': 'menu\\button_credits.png',
      'sprite_button_credits_hover': 'menu\\button_credits_hover.png',

      # Sprite Menu Btn Quit
      'sprite_button_quit': 'menu\\button_quit.png',
      'sprite_button_quit_hover': 'menu\\button_quit_hover.png',

      # Sprite Credits
      'sprite_credits': 'credits.png',

      # Modal Fin de game
      'sprite_loose': 'end_screen\\loose.png',
      'sprite_win': 'end_screen\\win.png',

      # Logo
      'sprite_logo': 'menu\\logo.png',

      # Colors Picker Hover
      'sprite_colors_picker_hover': 'game_screen\\colors_picker_hover.png'
    }

    # Dictionnaire permettant d'accéder à partir d'une clé à un object Surface (affichable dans pygame)
    self.s = {}
    # Remplir le dictionnaire ci-dessus
    for s in hashmap.items():
      self.s[s[0]] = pygame.image.load(root + s[1])

    i = 1
    # List qui contient les frames du background animé
    self.background = []

    while(i <= 54):
      numStr = str(i)
      numStr = '0' * (2 - len(numStr)) + numStr
      i += 1
      self.background.append(pygame.image.load(root + "background\\frame-" + numStr + ".png"))

    i = 0
    # List qui contient les frames du joli chat sur l'écran du jeu
    self.chat = []
    # Remplir la liste ci-dessus
    while(i <= 10):
      numStr = str(i)
      numStr = '0' * (2 - len(numStr)) + numStr
      i += 1
      self.chat.append(pygame.image.load(root + "chat\\" + numStr + ".png"))