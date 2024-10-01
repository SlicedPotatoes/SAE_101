from mm import TabCouleur
from random import *

"""
Fonction qui génère la combinaison secrète

Elle pioche parmi les couleurs définies dans un tableau en générant un nombre aléatoire compris dans les bornes de celui-ci.
"""
def genSecret():
    arr = []

    for i in range(5):
        arr.append(TabCouleur[randint(0, len(TabCouleur) - 1)])
    
    return arr