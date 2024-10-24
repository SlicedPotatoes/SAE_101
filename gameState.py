import pygame
import ui.spriteLoader as sl

from random import *

class gameState:
  def __init__(self, colors:list, sc:sl.sprite_collection)->None:
    self.running = True
    self.font = "VCRosdNEUE.ttf"

    # Données relatives a l'affichage
    self.currentScreen = 'main_menu'
    self.screen = pygame.display.set_mode((1280, 720))
    self.currentBackgroundIndex = 0
    self.currentChatIndex = 0

    # Données statiques relatives au jeu
    self.colors = colors
    self.sc = sc

    # Données relatives au jeu
    self.isGameEnd = False
    self.win = False
    self.secret = self.genSecret()
    self.lines = [[]]
  
  # Méthode pour reset l'état du jeu
  def reset(self, screen_name:str)->None:
     self.currentScreen = screen_name
     self.isGameEnd = False
     self.win = False
     self.secret = self.genSecret()
     self.lines = [[]]

  # Méthode pour générer le secret
  def genSecret(self)->list:
    arr = []

    for i in range(5):
        arr.append(randint(0, len(self.colors) - 1))

    return arr

  # Méthode de feedback pour une proposition
  def feedback(self, row:int)->tuple:
    i = 0

    wellPlaced = 0 # Compteur pour les couleurs bien placées

    secretDic = {}
    combList = []

    # Parcourt les deux listes (secret et comb) pour comparer les couleurs
    while(i < len(self.secret)):
        secretColor = self.secret[i] # Couleur actuelle de la combinaison secrète
        combColor = self.lines[row][i]     # Couleur actuelle de la tentative

        # Si les couleurs sont identiques, elles sont bien placées
        if(secretColor == combColor):
            wellPlaced += 1
        # Sinon, on les stocke pour la vérification des "bonnes couleurs mal placées"
        else:
            if(secretColor in secretDic):
                secretDic[secretColor] += 1
            else:
                secretDic[secretColor] = 1
            combList.append(combColor)
        
        i += 1

    goodColor = 0 # Compteur pour les bonnes couleurs mal placées

    # Parcours des éléments mal placés
    for element in combList:
        # Si l'élément se trouve également dans la combinaison secrète et qu'il n'a pas été compté pour "WellPlaced" ou "goodColor"
        if(element in secretDic and secretDic[element] > 0):
            goodColor += 1          # On incrémente goodColor
            secretDic[element] -= 1 # On décrémente l'élément pour ne pas le recompter

    return (wellPlaced, goodColor)

  # Méthode exécutée à chaque frame pour mettre à jour gameState
  def update(self)->None:
    # Si le nombre d'essais est supérieur ou égal à 15, le jeu est fini par une défaite
    if(len(self.lines) > 15):
        self.isGameEnd = True
        self.win = False
        self.currentScreen = 'end_screen'
    
    # Si la proposition n'est pas complète on n'a pas besoin d'exécuté le code qui suit
    if(len(self.lines[-1]) != 5):
      return

    i = 0

    # On compare chaque élément de la tentative et combinaison secrète
    while(i < len(self.secret)):
        # Si pour une paire d'éléments, les éléments sont différents, le jeu continue.
        if(self.secret[i] != self.lines[-1][i]):
            self.isGameEnd = False
            self.win = False

            self.lines.append([])
            return
        i += 1
    
    # Sinon, le jeu est fini sur une victoire de l'utilisateur
    self.isGameEnd = True
    self.win = True
    self.currentScreen = 'end_screen'