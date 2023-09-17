"""module permettant d'implémenter les figures les plus connues du jeu de la vie"""

def canon_a_planneurs():
    """realise le canon à planneurs de Ghosper"""
    cellules = [(4, 0), (4, 1), (5, 0), (5, 1), (4, 10), (5, 10),
                (6, 10), (3, 11), (7, 11), (2, 12), (8, 12), (2, 13),
                (8, 13), (5, 14), (3, 15), (7, 15), (4, 16), (5, 16), (6, 16),
                (5, 17), (2, 20), (3, 20), (4, 20), (2, 21), (3, 21),
                (4, 21), (1, 22), (5, 22), (0, 24), (1, 24), (5, 24),
                (6, 24), (2, 34), (3, 34), (2, 35), (3, 35)]

    return cellules, 36

def croissance_infinie_min():
    """plus petit ensemble de cellules ayant une croissance infinie"""
    cellules = [(1, 1), (1, 3), (2, 3), (3,5), (4, 5), (5, 5),
                (4, 7), (5, 7), (6, 7), (5, 8)]

    return cellules, 9

def clignotant():
    """la figure du clignotant"""
    cellules = [(0, 1), (1, 1), (2, 1)]

    return cellules, 3
