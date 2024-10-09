"""
Prends en paramètre la combinaison secrète, la dernière tentative de l'utilisateur et le nombre de tentatives.

Retourne si le jeu est fini, et qui est le vainqueur (dans le cas où le jeu n'est pas fini cette valeur n'a pas de sens)
"""
def gameState(secret, line, currentLine):
    # Si le nombre d'essais est supérieur ou égal à 15, le jeu est fini par une défaite
    if(currentLine >= 15):
        return (True, False)
    
    i = 0

    # On compare chaque élément de la tentative et combinaison secrète
    while(i < len(secret)):
        # Si pour une paire d'éléments, les éléments sont différents, le jeu continue.
        if(secret[i] != line[i]):
            return (False, False)
        i += 1
    
    # Sinon, le jeu est fini sur une victoire de l'utilisateur
    return (True, True)

if (__name__ == "__main__"):
    def printResult(secret, line, currentLine, result):
        print("gameState(", secret, ",", line, ",", currentLine, ") Attendue:", result, " Retourné:", gameState(secret, line, currentLine))

    # Jeux de test
    printResult([1, 2, 3, 4, 4], [4, 4, 4, 1, 2], 15, (True, False))
    printResult([1, 2, 3, 4, 4], [1, 2, 3, 4, 4], 8, (True, True))
    printResult([1, 2, 3, 4, 4], [4, 4, 3, 2, 1], 8, (False, False))