import pygame
from logique.genSecret import genSecret
from logique.feedback import feedback
from logique.gameState import gameState
import mm

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# game setup
secret = genSecret()
currentLine = 1

screen.fill("white")
mm.afficherPlateau(screen)
mm.afficherChoixCouleur(screen)

line = [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]

resultIsShow = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    state = gameState(secret, line, currentLine)

    if(state[0] == True):
        if(not resultIsShow):
            mm.showEndGame(screen, state[1])
            mm.afficherSecret(screen, secret)
            resultIsShow = True
        
        continue

    line = mm.construireProposition(screen, currentLine)
    mm.afficherResultat(screen, feedback(secret, line), currentLine)

    currentLine += 1

    pygame.display.flip()
    clock.tick(60)