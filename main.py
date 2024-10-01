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
            mm.showEndGame(screen, state[1]) # Afficher le message de fin de partie
            mm.afficherSecret(screen, secret) # Afficher la combinaison secrète
            resultIsShow = True # Marquer le résultat comme affiché
        
        continue # Passer à l'it&ration suivante (bloque le reste du code)

    # Construire la proposition courante du joueur
    line = mm.construireProposition(screen, currentLine)
    # Afficher le résultat (feedback) basé sur la comparaison entre "secret" et "line"
    mm.afficherResultat(screen, feedback(secret, line), currentLine)

    # Passer a la ligne suivante
    currentLine += 1

    pygame.display.flip()
    clock.tick(60)