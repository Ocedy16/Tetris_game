import pygame
import random
from pygame.locals import *  # importer les constantes

# Autre façon de voir les formes. A tester. Mettre toutes les coordonées des zéros dans des listes à l'intérieur d'une liste
T = [[[2, 1], [2, 2], [1, 2], [3, 2]], [[2, 1], [2, 2], [2, 3], [3, 2]], [[1, 2], [2, 2], [3, 2], [2, 3]],
     [[2, 1], [2, 2], [2, 3], [1, 2]]]
L = [[[1, 1], [1, 2], [2, 2], [3, 2]], [[2, 1], [2, 2], [1, 3], [2, 3]], [[1, 2], [2, 2], [3, 2], [3, 3]],
     [[2, 1], [3, 1], [2, 2], [2, 3]]]
S = [[[2, 2], [3, 2], [3, 3], [4, 3]], [[2, 1], [1, 2], [2, 2], [1, 3]]]
#Z = [[[2, 2], [3, 2], [1, 3], [2, 3]]]
#I = [[[2, 0], [2, 1], [2, 2], [2, 3]]]
#O = [[[2, 2], [3, 2], [2, 3], [3, 3]]]

# Ainsi de suite avec les autres. Puis lier cela aux coordonnées de la pièce. Ex: le x et le y de la pièce représentent tout en haut à gauche de la pièce et
# les x et y de combien on doit "bouger" pour tomber sur le bloc. Il faut donc considérer les blocs indépendamment. Peut être implémenter qqc dans la classe.
# Une chose à tester pour voir si la méthode est la bonne: implémenter une classe dans un autre fichier avec les 4 coordonnées du bloc. Voir si modifier
# Le x et le y du bloc change bien les sous coordonnées automatiquement. En gros, est ce que le calcul se fait automatiquement. Je pense que oui mais j'aimerais
# Être sûre.

formes = [T, S, L]


class Piece(object):
    def __init__(self, lettre, colonne, ligne):
        self.x = colonne
        self.y = ligne
        self.couleur = (random.randint(10, 254), random.randint(10, 254), random.randint(10, 254))
        self.lettre = lettre
        self.rotation = 0
        self.forme = self.lettre[self.rotation]
        # Voir pour peut être ajouter un sous accès liste si on accède d'abord aux formes.
        print(f"Piece Constructor / Forme : {self.forme} / X: {self.x} / Y: {self.y}")
        self.bloc_1 = [self.x + self.forme[0][0], self.y + self.forme[0][1]]
        self.bloc_2 = [self.x + self.forme[1][0], self.y + self.forme[1][1]]
        self.bloc_3 = [self.x + self.forme[2][0], self.y + self.forme[2][1]]
        self.bloc_4 = [self.x + self.forme[3][0], self.y + self.forme[3][1]]
        self.blocs = [self.bloc_1, self.bloc_2, self.bloc_3, self.bloc_4]

    def deplacer(self):
        self.bloc_1 = [self.x + self.forme[0][0], self.y + self.forme[0][1]]
        self.bloc_2 = [self.x + self.forme[1][0], self.y + self.forme[1][1]]
        self.bloc_3 = [self.x + self.forme[2][0], self.y + self.forme[2][1]]
        self.bloc_4 = [self.x + self.forme[3][0], self.y + self.forme[3][1]]
        self.blocs = [self.bloc_1, self.bloc_2, self.bloc_3, self.bloc_4]

    def tourner(self):
        print("----------------------")
        print(f"SELF Forme : {self.forme}")
        print(f"SELF Lettre : {self.lettre}")
        print(f"SELF Rotation : {self.rotation}")
        print(f"Forme : {self.forme}")
        if self.rotation <= len(self.lettre):
            self.forme = self.lettre[self.rotation]
            self.bloc_1 = [self.x + self.forme[0][0], self.y + self.forme[0][1]]
            self.bloc_2 = [self.x + self.forme[1][0], self.y + self.forme[1][1]]
            self.bloc_3 = [self.x + self.forme[2][0], self.y + self.forme[2][1]]
            self.bloc_4 = [self.x + self.forme[3][0], self.y + self.forme[3][1]]
            self.blocs = [self.bloc_1, self.bloc_2, self.bloc_3, self.bloc_4]


# ce que j'ai codé pour définir les blocs, c'est toujours la même idée mais je trouve ça plus clair que les tableaux S,Z,... au début
# par contre il y a peut-être des erreurs ou oublis quand j'ai défini les propriété d'un bloc/tetros

# les couleurs qui correspondent aux blocs dans le jeu classique
couleur_forme = [[0, 255, 255], [255, 255, 0], [255, 0, 0], [0, 255, 0], [255, 0, 255], [255, 100, 10],
                 [0, 0, 100]]  # cyan, jaune, rouge, vert, violet, orange, navy


def creer_grille(grille_finie):
    if type(grille_finie) == list: print('creer_grille errer')
    grille = [[(0, 0, 0) for x in range(10)] for y in
              range(20)]  # Reinitialisation de la grille. Le tuple indique la couleur

    # Ici le but est d'afficher la grille en fonction des informations stockées.
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (j, i) in grille_finie:
                c = grille_finie[(j, i)]
                grille[i][j] = c
    return grille

def convertir_orientation_piece(piece):
    l = len(piece.lettre)
    piece.rotation = (piece.rotation + 1) % l


def save_dict(piece, grille_finie):
    grille_finie[(piece.bloc_1[0], piece.bloc_1[1])] = piece.couleur
    grille_finie[(piece.bloc_2[0], piece.bloc_2[1])] = piece.couleur
    grille_finie[(piece.bloc_3[0], piece.bloc_3[1])] = piece.couleur
    grille_finie[(piece.bloc_4[0], piece.bloc_4[1])] = piece.couleur


def espace_valide(piece, grille_finie):
    for bloc in piece.blocs:
        if bloc[0] < 0 or bloc[0] > 9:
            return False
        if 0 > bloc[1] < 0 or bloc[1] > 19:
            return False
        if (bloc[0], bloc[1]) in grille_finie:
            return False
    return True


def verifier_defaite(grille_finie, grille):
    i = 0
    while i < len(grille[0]):
        if grille_finie[(0, i)] != (0, 0, 0):
            return True
        i = i + 1
    return False


def get_shape():
    global formes, couleur_forme
    return Piece(random.choice(formes), 3, 0)


def dessiner_piece(new_piece):
    pygame.draw.rect(fenetre, new_piece.couleur, (50 + new_piece.bloc_1[0] * 15, 50 + new_piece.bloc_1[1] * 15, 13, 13))
    pygame.draw.rect(fenetre, new_piece.couleur, (50 + new_piece.bloc_2[0] * 15, 50 + new_piece.bloc_2[1] * 15, 13, 13))
    pygame.draw.rect(fenetre, new_piece.couleur, (50 + new_piece.bloc_3[0] * 15, 50 + new_piece.bloc_3[1] * 15, 13, 13))
    pygame.draw.rect(fenetre, new_piece.couleur, (50 + new_piece.bloc_4[0] * 15, 50 + new_piece.bloc_4[1] * 15, 13, 13))
    pygame.display.update()
    pygame.init()


def ecrire_texte_milieu(texte, taille, couleur, surface):
    return 0


def dessiner_grille(grille):
    # Pour chaque élément dans la grille, dessiner sa couleur
    for i in range(20):
        for j in range(10):
            # if (j, i) in grille_finie :
            # for i in range (3) :
            pygame.draw.rect(fenetre, grille[i][j], (50 + j * 15, 50 + i * 15, 13, 13))
    pygame.display.update()
    pygame.init()


def effacer_ligne(grille_finie, i):
    for j in range(10):
        grille_finie[(i,j)] == (0, 0, 0)


def retirer_lignes_pleine(grille, grille_finie):
    while i < 20:
        while j < 10:
            if grille_finie[i][j] == (0, 0, 0):
                i = i + 1
                j = 0
            else:
                j = j + 1
        effacer_ligne(grille_finie, i)
        j = 0
        i = i + 1


def main():
    clock = pygame.time.Clock()
    running = True
    grille_finie = {}
    grille = creer_grille(grille_finie)
    dessiner_grille(grille)
    piece = get_shape()
    dessiner_piece(piece)
    time_elapsed_since_last_action = 0
    while running == True:
        dt = clock.tick()
        grille = creer_grille(grille_finie)
        time_elapsed_since_last_action += dt
        if time_elapsed_since_last_action > 1000:
            time_elapsed_since_last_action = 0
            piece.y += 1
            piece.deplacer()
            if not (espace_valide(piece, grille_finie)):
                piece.y -= 1
                piece.deplacer()
                save_dict(piece, grille_finie)
                piece = get_shape()

            else:
                grille = creer_grille(grille_finie)
                dessiner_grille(grille)
                piece.deplacer()
                dessiner_piece(piece)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.x -= 1
                    piece.deplacer()
                    if not (espace_valide(piece, grille_finie)):
                        piece.x += 1
                        piece.deplacer()
                    else:
                        grille = creer_grille(grille_finie)
                        dessiner_grille(grille)
                        piece.deplacer()
                        dessiner_piece(piece)
                if event.key == pygame.K_RIGHT:
                    piece.x += 1
                    piece.deplacer()
                    if not (espace_valide(piece, grille_finie)):
                        piece.x -= 1
                        piece.deplacer()
                    else:
                        grille = creer_grille(grille_finie)
                        dessiner_grille(grille)
                        piece.deplacer()
                        dessiner_piece(piece)
                if event.key == pygame.K_DOWN:
                    piece.y += 1
                    piece.deplacer()
                    if not (espace_valide(piece, grille_finie)):
                        piece.y -= 1
                        piece.deplacer()
                        save_dict(piece, grille_finie)
                        piece = get_shape()

                    else:
                        grille = creer_grille(grille_finie)
                        dessiner_grille(grille)
                        piece.deplacer()
                        dessiner_piece(piece)

                if event.key == pygame.K_SPACE:
                    convertir_orientation_piece(piece)
                    #piece.tourner(piece.lettre)
                    piece.tourner()
                    if not (espace_valide(piece, grille_finie)):
                        piece.rotation = (piece.rotation - 1) % len(piece.forme)
                        piece.tourner()
                    else:
                        grille = creer_grille(grille_finie)
                        dessiner_grille(grille)
                        piece.tourner()
                        dessiner_piece(piece)


pygame.init()
fenetre = pygame.display.set_mode((600, 700))
fenetre.fill((255, 255, 255))  # pour avoir un fond blanc
main()
