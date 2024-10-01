"""
Prends en paramètre la combinaison secrète, la dernière tentative de l'utilisateur et le nombre de tentatives.

Retourne si le jeu est fini, et qui est le vainqueur (dans le cas où le jeu n'est pas fini cette valeur n'a pas de sens)
"""
def gameState(secret, line, currentLine):
    # Si le nombre d'essais est supérieur ou égal à 16, le jeu est fini par une défaite
    if(currentLine >= 16):
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