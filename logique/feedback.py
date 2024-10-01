"""
Prends en paramètre la combinaison secrète et la tentative de l'utilisateur

Retourne le nombre d'éléments bien placés, et le nombre de couleurs 
"""
def feedback(secret, comb):
    i = 0

    wellPlaced = 0 # Compteur pour les couleurs bien placées

    secretDic = {}
    combList = []

    # Parcourt les deux listes (secret et comb) pour comparer les couleurs
    while(i < len(secret)):
        secretColor = secret[i] # Couleur actuelle de la combinaison secrète
        combColor = comb[i]     # Couleur actuelle de la tentative

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

if (__name__ == "__main__"):
    def printResult(secret, comb, result):
        print("feedback(", secret, ",", comb, ") Attendue:", result, " Retourné:", feedback(secret, comb))

    # Jeux de test
    printResult([1, 2, 3, 4, 4], [4, 4, 4, 1, 2], (0, 4))