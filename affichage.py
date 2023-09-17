"""fonction d'affichahe avec pygame"""
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

def nb_pixel(plateau, taille_page):
    """transforme l'unité du jeu en le nombre de pixel associé que cela représente"""
    return taille_page//len(plateau[0]) + 1



def affiche_carre(screen, case, facteur):
    """permet l'affichage de la case sur la page screen"""
    abscisse, ordonnee = facteur*case[1], facteur*case[0]

    pygame.draw.rect(screen, black, (abscisse, ordonnee, facteur, facteur))

def affiche_quadrillage(screen, longueur, facteur):
    """permet l'affichage du quadrillage du jeu de la vie
        attention, celui ci deborde de l'écran"""
    for i in range(0, longueur):
        pygame.draw.line(screen, black, (0, facteur*i), ((screen.get_size())[0], facteur*i))

    for j in range (0, longueur):
        pygame.draw.line(screen, black, (facteur*j, 0), (facteur*j, (screen.get_size())[0]))
    pygame.display.flip()

def affiche_plateau(screen, plateau, facteur):
    """affiche le plateau sur l'écran"""
    longueur = len(plateau[0])
    affiche_quadrillage(screen, len(plateau[0]), facteur)

    for i in range (0, longueur):
        for j in range (0, longueur):
            if plateau[i][j]:
                affiche_carre(screen, (i, j), facteur)
    pygame.display.flip()
