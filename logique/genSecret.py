from mm import TabCouleur
from random import *

def genSecret():
    arr = []

    for i in range(5):
        arr.append(TabCouleur[randint(0, len(TabCouleur) - 1)])
    
    return arr