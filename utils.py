import math

# Fonction retournant les coordinnées des coins d'un rectange
def getHitboxRect(center:tuple, size:tuple)->tuple:
  a = size[0] % 2
  b = size[1] % 2

  return (center[0] - (size[0] // 2) - a, center[0] + (size[0] // 2) + a, center[1] - (size[1] // 2) - b, center[1] + (size[1] // 2) + b)

# Fonction qui retourne la distance entre 2 points, utilisé pour la hitbox des CTA circulaire
def distance(a:list,b:list)->float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Fonction qui retourne vrai si position est dans la hitbox d'un rectangle
def inRectHitbox(pos:tuple, hitbox:tuple)->bool:
  return pos[0] >= hitbox[0] and pos[0] <= hitbox[1] and pos[1] >= hitbox[2] and pos[1] <= hitbox[3]