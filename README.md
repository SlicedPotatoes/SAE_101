# SAE S101 - MasterMind en Python

Ce repository contient le code et les documents associés au projet **SAE S1.01** du BUT Informatique, qui consiste à développer une application en Python permettant de jouer une manche de MasterMind contre l'ordinateur.

## Branche Alternative - Interface Graphique Améliorée

Une seconde branche du projet est disponible, proposant une refonte complète de la structure du code ainsi qu'une interface graphique améliorée pour une expérience utilisateur plus agréable et intuitive. Cette version inclut des améliorations visuelles et ergonomiques pour rendre le jeu plus immersif.

## Objectif de la SAE

Le but de ce projet est de développer un programme Python permettant à un joueur humain de deviner une combinaison de couleurs générée aléatoirement par l'ordinateur, en suivant les règles du jeu MasterMind. L'interface utilisateur est gérée via la bibliothèque `mm.py` basée sur Pygame.

## Spécifications Techniques

### Fonctionnalités principales

1. **Interface Utilisateur (IHM):**
   - Utilisation de la bibliothèque `mm.py` (basée sur Pygame) pour afficher l’interface de jeu.
   - Le fichier `mm.py` contient les fonctions et variables nécessaires pour gérer les éléments de l'IHM.

2. **Fonctionnalité du Jeu:**
   - **Génération aléatoire** d'une combinaison secrète de 5 couleurs.
   - **Interaction utilisateur:** Le joueur propose une combinaison, et le programme affiche le résultat sous la forme d'un tuple `(bien placés, mal placés)`.
   - **Résultat de manche:** Affichage d'un message indiquant si le joueur a gagné ou perdu, avec le nombre de tentatives.
  
### Structure des Fichiers

```
├── feedback.py      # Code source de la fonction de feedback avec les jeux de tests
├── gameState.py     # Code source de la fonction retournant l'état du jeu et les jeux de tests
├── genSecret.py     # Code source de la fonction de génération de combinaisons et les jeux de tests
├── main.py          # Programme principal
├── mm.py            # Bibliothèque de gestion d'IHM
├── showWinner.py    # Code source pour afficher le résultat de la manche (IHM)
├── README.md        # Informations sur le projet
├── Rapport.pdf      # Rapport technique de la SAE
└── .gitignore       # Fichiers ignorés par Git
```

### Installation

1. **Cloner le repository:**
```bash
git clone https://github.com/SlicedPotatoes/SAE_101.git
cd SAE_101
```
2. **Installer les dépendances:**
```bash
pip install pygame
```
3. **Lancer l'application:**
```bash
python .\main.py
```

### Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.
