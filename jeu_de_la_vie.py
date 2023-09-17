"""le jeu de la vie"""

import sys
import pygame
import cellule
import plateaux
import affichage
import positions

def cree_plateau_vide(longueur):
    """cree le plateau vide"""
    return [[0 for i in range(0, longueur)] for i in range(0, longueur)]

def calcule_plateau_suivant(plateau, longueur_max):
    """calcule la position suivante grace au règles du jeu de la vie et
    du plateau actuel, affiche le plateau suivant et le retourne
    invariant : le bord du plateau est toujours un 0 """

    augmente_plateau_en_fin = False
    longueur = len(plateau[0])
    plateau_suivant = [[0 for i in range(0, longueur)] for i in range(0, longueur)]

    for i in range (0, longueur):
        for j in range (0, longueur):
            if plateau[i][j] == 1:
                if cellule.doit_survivre(plateau, (i, j)):
                    if i in [0, longueur-1] or j in [0, longueur-1]:
                        augmente_plateau_en_fin = True
                plateau_suivant[i][j] = int( cellule.doit_survivre(plateau, (i, j)) )

            else:
                if cellule.doit_se_creer(plateau, (i, j)):
                    plateau_suivant[i][j] = 1
                    if i in [0, longueur-1] or j in [0, longueur-1]:
                        augmente_plateau_en_fin = True

    if augmente_plateau_en_fin and longueur  < longueur_max:
        plateau_suivant = plateaux.augmente_taille_plateau(plateau_suivant, 5)

    return plateau_suivant

def lancer_la_page(plateau,
                   taille_page = 900,
                   nb_generation = 200,
                   tick = 50,
                   longueur_max = 500):
    """fonction principale qui va permettre d'afficher le rendu graphique de notre jeu"""

     # Initialise screen
    pygame.init()
    i = 0

    screen = pygame.display.set_mode((taille_page, taille_page))
    pygame.display.set_caption('jeu de la vie')
    screen.fill(affichage.white)

    affichage.affiche_plateau(screen, plateau, taille_page)
    plateaux.augmente_taille_plateau(plateau, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if i<nb_generation:

            facteur = affichage.nb_pixel(plateau, taille_page)

            print(f"{i} ...")

            screen.fill(affichage.white)

            plateau = calcule_plateau_suivant(plateau, longueur_max)
            affichage.affiche_plateau(screen, plateau, facteur)

            pygame.display.flip()

            pygame.time.wait(tick)
            i +=1

def cree(position):
    """cree la matrice des cellules depuis la liste de couple de cellules vivante 
        dans la module positions"""
    cellules, taille = position()

    plateau = cree_plateau_vide(taille)

    for case in cellules:
        plateau[case[0]][case[1]] = 1

    return plateau

def main():
    """fonction main"""


    canon = cree(positions.canon_a_planneurs)
    #clignotant = cree(positions.clignotant)
    #croissance = cree(positions.croissance_infinie_min)

    #lancer_la_page(croissance, nb_generation=1000, tick=1, taille_page=1000, longueur_max=100)
    #lancer_la_page(clignotant)
    lancer_la_page(canon, nb_generation=300, tick=100, longueur_max=50)

main()
