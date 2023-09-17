"""fonctions relatives au plateau"""

def augmente_taille_plateau_1(plateau):
    """augmente la taille du plateau de une case dans toutes les directions"""

    longueur = len(plateau[0])

    for i in range (0, longueur):
        plateau[i].insert(0, 0)
        plateau[i].append(0)

    plateau.insert(0, [0 for i in range (longueur+2)])
    plateau.append([0 for i in range (longueur+2)])

    return plateau

def augmente_taille_plateau(plateau, pas_augmentation):
    """augmente la taille du plateaux de pas_augmentation dans toutes les directions"""
    for _ in range(pas_augmentation):
        plateau = augmente_taille_plateau_1(plateau)

    return plateau
