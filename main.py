import pygame
from genSecret import genSecret
from feedback import feedback
from gameState import gameState
from showWinner import showEndGame
import mm

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# game setup
secret = genSecret()
currentLine = 0
line = [(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)]
resultIsShow = False

# static display
screen.fill("white")
mm.afficherPlateau(screen)
mm.afficherChoixCouleur(screen)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vérification de l'état du jeu : "gameState" retourne un tuple (jeu terminé, victoire / defaite)
    state = gameState(secret, line, currentLine)

    # Si le jeu est terminé
    if(state[0] == True):
        # Et que le resultat n'a pas encore été affiché
        if(not resultIsShow):
            showEndGame(screen, state[1], currentLine + 1) # Afficher le message de fin de partie
            mm.afficherSecret(screen, secret) # Afficher la combinaison secrète
            resultIsShow = True # Marquer le résultat comme affiché
        
        continue # Passer à l'it&ration suivante (bloque le reste du code)

    # Construire la proposition courante du joueur
    line = mm.construireProposition(screen, 16 - currentLine)
    # Afficher le résultat (feedback) basé sur la comparaison entre "secret" et "line"
    mm.afficherResultat(screen, feedback(secret, line), 16 - currentLine)

    # Passer a la ligne suivante
    currentLine += 1

    pygame.display.flip()
    clock.tick(60)