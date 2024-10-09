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

def hash(list):
    return (list[0], list[1], list[2], list[3], list[4])

if(__name__ == "__main__"):
    for i in range(10):
        print(genSecret())