from mm import *
import pygame

# Fonction qui affiche le résultat de la partie à la fin de celle-ci
def showEndGame(f, isWin, nbTry):
    width = 720
    height = 360

    left = (1280 // 2) - (width // 2)
    top = (720 // 2) - (height // 2)
    
    nbTry = nbTry-1

    pygame.draw.rect(f,Orange,[left, top, width, height])

    text1 = "GG"
    text2 = "FF"
    text3 = "Nombre d'essais : " + str(nbTry)

    myfont1 = pygame.font.SysFont("monospace", 70)
    myfont2 = pygame.font.SysFont("monospace", 20)

    label1 = myfont1.render(text1 if isWin else text2, 1, Noir)

    left = (1280 // 2) - label1.get_size()[0] // 2
    top = (720 // 2) - label1.get_size()[1] // 2
    
    label2 = myfont2.render(text3, 1, Noir)

    leftTry = (1280 // 2) - (2 * label1.get_size()[0]) + 40
    topTry = (720 // 2) + label1.get_size()[1] // 2

    f.blit(label1, (left, top))
    f.blit(label2, (leftTry, topTry))
    
    pygame.display.update()
   