"""fonctions liées a l'état futur de la cellule"""

def doit_se_creer(plateau, cellule):
    """plateau est tel que defini dans le prgrm jeu_de_la_vie.py
    renvoie vrai si la cellule doit se créer, 
    précondition : la cellule était à l'état 0 avant l'appel"""

    return nombre_voisin(plateau, cellule) == 3

def doit_survivre(plateau, cellule):
    """plateau est tel que defini dans le prgrm jeu_de_la_vie.py
    renvoie vrai si la cellule doit rester en vie, 
    précondition : la cellule était à l'état 1 avant l'appel"""

    return nombre_voisin(plateau, cellule) in [2, 3]

def val_case(plateau, case):
    """la case peut etre un nombre négatif ou > len(plateau [0])"""

    i, j = case

    longueur = len(plateau[0])
    est_case_dehors = (i < 0 or j < 0
                   or i > longueur-1 or j > longueur-1)

    if est_case_dehors:
        return 0
    return plateau[i][j]


def nombre_voisin(plateau, cellule):
    """renvoie le nombre de voisin de la cellule relativement au plateau
    précondition : la cellule a regarder n'est pas au bord du plateau"""

    i, j = cellule

    return (val_case(plateau, (i-1, j-1)) +
            val_case(plateau, (i-1, j)) +
            val_case(plateau, (i-1, j+1)) +

            val_case(plateau, (i, j-1)) +
            val_case(plateau, (i, j+1)) +

            val_case(plateau, (i+1, j-1)) +
            val_case(plateau, (i+1, j)) +
            val_case(plateau, (i+1, j+1)))
