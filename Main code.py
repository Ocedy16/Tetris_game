import pygame
import random
from pygame.locals import *  # importer les constantes
from pygame import mixer
import copy

# Autre façon de voir les formes. A tester. Mettre toutes les coordonées des zéros dans des listes à l'intérieur d'une liste
T = [[[2, 1], [2, 2], [1, 2], [3, 2]], [[2, 1], [2, 2], [2, 3], [3, 2]], [[1, 2], [2, 2], [3, 2], [2, 3]],
     [[2, 1], [2, 2], [2, 3], [1, 2]]]
L = [[[1, 1], [1, 2], [2, 2], [3, 2]], [[2, 1], [2, 2], [1, 3], [2, 3]], [[1, 2], [2, 2], [3, 2], [3, 3]],
     [[2, 1], [3, 1], [2, 2], [2, 3]]]
S = [[[2, 2], [3, 2], [3, 3], [4, 3]], [[2, 1], [1, 2], [2, 2], [1, 3]]]
Z = [[[2, 2], [3, 2], [1, 3], [2, 3]],[[2,3],[2,4],[3,3],[3,2]]]
I = [[[2, 0], [2, 1], [2, 2], [2, 3]],[[0,2],[1,2],[2,2],[3,2]]]
O = [[[2, 2], [3, 2], [2, 3], [3, 3]]]
J = [[[3, 1], [1, 2], [2, 2], [3, 2]], [[1, 1], [2, 1], [2, 2], [2, 3]], [[1, 2], [2, 2], [3, 2], [1, 3]], [[2, 1], [2, 2], [2, 3], [3, 3]]]


# Ainsi de suite avec les autres. Puis lier cela aux coordonnées de la pièce. Ex: le x et le y de la pièce représentent tout en haut à gauche de la pièce et
# les x et y de combien on doit "bouger" pour tomber sur le bloc. Il faut donc considérer les blocs indépendamment. Peut être implémenter qqc dans la classe.
# Une chose à tester pour voir si la méthode est la bonne: implémenter une classe dans un autre fichier avec les 4 coordonnées du bloc. Voir si modifier
# Le x et le y du bloc change bien les sous coordonnées automatiquement. En gros, est ce que le calcul se fait automatiquement. Je pense que oui mais j'aimerais
# Être sûre.

formes = [T, S, L, Z, I, O, J]

class Piece(object):
    def __init__(self, lettre, couleur, colonne, ligne):
        self.x = colonne
        self.y = ligne
        #self.couleur = (random.randint(10, 254), random.randint(10, 254), random.randint(10, 254))
        self.couleur= couleur
        self.lettre = lettre
        self.rotation = 0
        self.forme = self.lettre[self.rotation]
        # Voir pour peut être ajouter un sous accès liste si on accède d'abord aux formes.
        #print(f"Piece Constructor / Forme : {self.forme} / X: {self.x} / Y: {self.y}")
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
        #print("----------------------")
        #print(f"SELF Forme : {self.forme}")
        #print(f"SELF Lettre : {self.lettre}")
        #print(f"SELF Rotation : {self.rotation}")
        #print(f"Forme : {self.forme}")
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
couleur_forme = [[0, 191, 255], [238, 201, 0], [255, 0, 0], [0, 238, 0], [171, 130, 255], [255, 128, 0], [139, 76, 57]]  # cyan, jaune, rouge, vert, violet, orange, navy

#dico_forme_couleur_tuple = {formes[1]:(255,0,255), formes[2]:(0,255,0), formes[3]:(255,0,0), formes[4]:(0,0,100), formes[5]:(255,255,0), formes[6]:(0,255,255), formes[7]:(255,100,10)}

def creer_grille(grille_finie):# liste des blocs avec tuple = couleur et indice du tuple = coordonnées
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
    for bloc in piece.blocs :
        grille_finie[(bloc[0], bloc[1])] = piece.couleur



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
        if (0,i) in grille_finie:
            return True
        i = i + 1
    return False

def verifier_defaite_debut(piece,grille_finie):
     if espace_valide(piece, grille_finie)==False:
          return True
     return False


def get_shape():
    global formes, couleur_forme
    new_int=random.randint(0,6)
    return Piece(formes[new_int],couleur_forme[new_int], 3, 0)





def dessiner_piece(new_piece):
    for blocs in new_piece.blocs:
        pygame.draw.rect(fenetre, new_piece.couleur, (150+blocs[0] * 30, 50 + blocs[1] * 30, 29, 29))
    pygame.display.update()
    pygame.init()


def dessiner_piece_suivante(piece_suivante):
    pygame.draw.rect(fenetre, (255, 255, 255), (15 * 30, 0 * 30, 29 * 6, 29 * 6))
    new_piece = copy.deepcopy(piece_suivante)
    new_piece.x = 15
    new_piece.deplacer()
    # print (new_piece.x)
    new_piece.y = 0
    new_piece.deplacer()
    for blocs in new_piece.blocs :
        pygame.draw.rect(fenetre, new_piece.couleur,( blocs[0] * 30, blocs[1] * 30, 29, 29))
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
            pygame.draw.rect(fenetre, grille[i][j], (150 + j * 30, 50 + i * 30, 29, 29))
    pygame.display.update()
    pygame.init()


def retirer_lignes_pleine(grille,grille_finie):
    inc = 0
    for i in range(len(grille) - 1, -1, -1):
        row = grille[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                if grille_finie.get((j, i)):
                    del grille_finie[(j, i)]
    if inc > 0:
        for key in sorted(list(grille_finie), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                grille_finie[newKey] = grille_finie.pop(key)
    return(inc)



def change_duree (grille,grille_finie): # quand le nombre de lignes retirées a augmenté de 10, la pièce augmente de vitesse
    global vitesse, compteur_lignes, niveau, score
    inc=retirer_lignes_pleine(grille,grille_finie)
    compteur_lignes+=inc
    if inc==1:
        score=score+(niveau*40+40)
    if inc==2:
        score=score+(niveau*100+100)
    if inc==3:
        score=score+(niveau*300+300)
    if inc==4:
        score=score+(niveau*1200+1200)
    if compteur_lignes>=2:
        niveau+=1
        vitesse=niveau*50
        compteur_lignes -= 2
    #if retirer_lignes_pleine(grille,grille_finie, nb_lignes_total) >= nb_lignes_prec + 1 :
      #  duree -= 900
       # nb_lignes_prec = nb_lignes_total
    #return (duree)

# def afficher_score():
# ecrire le code

def main_screen():
    begin = True
    pygame.display.set_caption('Tetris')
    font = pygame.font.SysFont('inkfree', 30, italic=True, bold=True)

    text = font.render('Press any key to play', True,
                       (255, 255, 255))
    textrect = text.get_rect()
    textrect.center = (600 // 2, 700 // 2)

    while begin:
        fenetre.blit(text, textrect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                begin = False
                main()

            pygame.display.update()



def end_screen():
    print("end")
    begin = True
    fenetre.fill((0,0,0))
    font = pygame.font.SysFont('inkfree', 30, italic=True, bold=True)  # try inkfree, georgia,impact,dubai,arial
    text1 = font.render('You loose : press return key to play again', True,(255, 255, 255))
    textrect1 = text1.get_rect()
    textrect1.center = (600 // 2, 300)
    text2=font.render('or press space key to end', True,(255, 255, 255))
    textrect1 = text1.get_rect()
    textrect2 = text2.get_rect()
    textrect1.center = (600 // 2, 300)
    textrect2.center = (600 // 2, 400)

    while begin:
        fenetre.blit(text1, textrect1)
        fenetre.blit(text2,textrect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    pygame.display.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    begin = False
                    main()

            pygame.display.update()

def main():
    global vitesse
    fenetre.fill((255, 255, 255))
    score = 0
    clock = pygame.time.Clock()
    running = True
    grille_finie = {}
    grille = creer_grille(grille_finie)
    dessiner_grille(grille)
    piece = get_shape()
    piece_suivante = get_shape()
    dessiner_piece(piece)
    dessiner_piece_suivante(piece_suivante)
    time_elapsed_since_last_action = 0
    #nb_lignes_total = 0
    #nb_lignes_prec = 0

    while running:
        if verifier_defaite_debut(piece,grille_finie):
            running=False
            vitesse=0
            niveau=0
            score=0
            end_screen()

        dt = clock.tick()
        grille = creer_grille(grille_finie)
        time_elapsed_since_last_action += dt
        if time_elapsed_since_last_action+vitesse > 1000 :
            time_elapsed_since_last_action = 0
            piece.y += 1
            piece.deplacer()
            if not (espace_valide(piece, grille_finie)):
                piece.y -= 1
                piece.deplacer()
                save_dict(piece, grille_finie)
                piece = copy.deepcopy(piece_suivante)
                piece_suivante = get_shape()
                if verifier_defaite_debut(piece,grille_finie):
                    running=False
                    vitesse=0
                    niveau=0
                    score=0
                    end_screen()

            else:
                grille = creer_grille(grille_finie)
                dessiner_grille(grille)
                piece.deplacer()
                dessiner_piece(piece)
                dessiner_piece_suivante(piece_suivante)

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
                        dessiner_piece_suivante(piece_suivante)
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
                        dessiner_piece_suivante(piece_suivante)
                if event.key == pygame.K_DOWN:
                    piece.y += 1
                    piece.deplacer()
                    if not (espace_valide(piece, grille_finie)):
                        piece.y -= 1
                        piece.deplacer()
                        save_dict(piece, grille_finie)
                        piece = copy.deepcopy(piece_suivante)
                        piece_suivante = get_shape()
                        if verifier_defaite_debut(piece,grille_finie):
                              running=False
                              score=0
                              niveau=0
                              vitesse=0
                              end_screen()
                        #retirer_lignes_pleine(grille, grille_finie, nb_lignes_total)
                        change_duree(grille,grille_finie)

                    else:
                        grille = creer_grille(grille_finie)
                        dessiner_grille(grille)
                        piece.deplacer()
                        dessiner_piece(piece)
                        dessiner_piece_suivante(piece_suivante)


                if event.key == pygame.K_SPACE:
                    convertir_orientation_piece(piece)
                    # piece.tourner(piece.lettre)
                    piece.tourner()
                    if not (espace_valide(piece, grille_finie)):
                        piece.rotation = (piece.rotation - 1) % len(piece.forme)
                        piece.tourner()
                    else:
                        grille = creer_grille(grille_finie)
                        dessiner_grille(grille)
                        piece.tourner()
                        dessiner_piece(piece)
                        dessiner_piece_suivante(piece_suivante)
        #retirer_lignes_pleine(grille, grille_finie, nb_lignes_total)
        change_duree(grille,grille_finie)
        if verifier_defaite(grille_finie,grille):
            running=False
            vitesse=0
            niveau=0
            score=0
            end_screen()
        # afficher_score()


pygame.init()
fenetre = pygame.display.set_mode((600, 700))
compteur_lignes=0
vitesse=0
niveau=0
score=0
"""
mixer.init()
mixer.music.load('D:/Dossier Océane/Tetris_music.mp3.mp3')
mixer.music.play()
"""
main_screen()
