#IMPORTATION DES MODULES NECESSAIRES#
import pygame
import math
from pygame.locals import *
from random import *
import time
import threading

#INITIALISATION DES ELEMENTS PRIMAIRES (Ecran, pygame, titre)#
pygame.init()                                                                           #Initialisation de pygame
pygame.display.set_caption('KNIGHT OF JUSTICE')                                         #Définition du titre du programme
fenetre = pygame.display.set_mode((1920,752), RESIZABLE)                                #Initialisation de la fenêtre
pygame.key.set_repeat(200, 30)                                                          #Définition du seuil de durée d'appui sur une touche pour la compter comme un appui répété


#IMPORTATION DU MODULE CONSTANTES.PY (Séparé du reste, car la fenêtre doit être initialisée avant de pouvoir utiliser le module#
from constantes import *


#Classe
class Niveau:                                                                           #Définition de la classe
    def __init__(self, fichier):                                                                #Ajout du fichier texte de niveau comme paramètre de Niveau(), permettant ainsi de définir le fichier à utiliser
        self.fichier = fichier
        self.structure = 0

    def creer(self):                                                                            #Définition de la fonction creer(), permettant de créer en mémoire le niveau à partir du fichier texte
        with open(self.fichier, "r") as fichier:                                                    #Ouverture du fichier définit précedemment, en lecture seulement
            strniveau = []                                                                              #Définition de la liste strniveau, vide pour le moment
            for ligne in fichier:                                                                       #Pour chaque ligne du fichier texte:
                lignenv = []                                                                                #Définition de la liste lignenv
                for sprite in ligne:                                                                        #Pour chaque sprite (correspondant à une lettre dans le fichier texte) dans la ligne:
                    if sprite != "\n":                                                                          #Si le sprite (la lettre) n'est pas une fin de niveau (un \n):
                        lignenv.append(sprite)                                                                      #Ajout de la lettre dans la liste lignenv, correspondant à une ligne du niveau
                strniveau.append(lignenv)                                                                       #Ajout de la liste lignenv dans la liste strniveau, qui contient la liste des sprites du niveau
            self.structure = strniveau                                                                      #strniveau est copié dans self.structure

    def affichage(self, fenetre, xperso, yperso, chgniveau2):                                               #Définition de affichage(), prenant en paramètre la fenetre et les coordonnées du perso, permettant d'afficher les blocs et gérer les collisions
        nligne = 0                                                                                  #Définition de la variable locale nligne, à 0
        global x_perso, y_perso, keydownr, keydownl, vit, og, chgniveau, niveauactuel, vie, touch   #Définition de x_perso, y_perso, keydownr, keydownl, vit et og comme variable globales, modifiables par la fonction
        for ligne in self.structure:                                                                #Pour chaque ligne dans self.structure:
            ncase = 0                                                                                   #Définition de la variable locale ncase, à 0
            for sprite in ligne:                                                                        #Pour chaque sprite (lettre) dans la ligne:
                x = ncase * tsprite                                                                         #Définition de la variable locale x, définit par le produit du nombre de case ncase de largeur de l'image et de la largeur en pixels d'une image
                y = nligne * tsprite                                                                        #Définition de la variable locale y, définit par le produit du nombre de case ncase de hauteur de l'image et de la hauteur en pixels d'une image
                if sprite == 'a' or sprite == 'b' or sprite == 'c' or sprite == 'd' or sprite == 'e' or sprite == 'f' or sprite == 'g' or sprite == 'h' or sprite == 'i' or sprite == 'z' or sprite == 'k':          #Si le sprite correspond à un bloc de terrain
                    if sprite == 'a':                                                                           #Affichage des blocs, en fonction du sprite contenu dans self.structure et des coordonnées obtenues précédemment (x et y)
                        fenetre.blit(plats, (x,y))                                                              #Si le sprite vaut a:
                    elif sprite == 'b':                                                                             #Affichage du bloc plats (correspondant à a), aux coordonéées x et y
                        fenetre.blit(plathg, (x,y))                                                             #
                    elif sprite == 'c':                                                                             #
                        fenetre.blit(plathd, (x,y))                                                             #
                    elif sprite == 'd':                                                                             #
                        fenetre.blit(platbd, (x,y))                                                             #
                    elif sprite == 'e':                                                                             #
                        fenetre.blit(platbg, (x,y))                                                             #
                    elif sprite == 'f':                                                                             #
                        fenetre.blit(pt, (x,y))                                                                 #
                    elif sprite == 'g':                                                                             #
                        fenetre.blit(ptg, (x,y))                                                                #
                    elif sprite == 'h':                                                                             #
                        fenetre.blit(ptd, (x,y))                                                                #
                    elif sprite == 'i':                                                                             #
                        fenetre.blit(ptb, (x,y))                                                                #
                    elif sprite == 'z':                                                                             #
                        fenetre.blit(pierre, (x,y))                                                             #
                    elif sprite == 'k':
                        fenetre.blit(bois, (x,y))
                    

                                                                                                                #Définition des collisions lorsque le joueur est contre un bloc (verticalement ou horizontalement)
                    if xperso >= x-20 and xperso <= x and yperso >= y-50 and yperso <= y+30:                    #Si le personnage est dans la zone de détection gauche d'un bloc:      
                        keydownr = 0                                                                                #Son déplacement vers la droite est annulé
                        touch = 1
                    elif xperso >= x+50 and xperso <= x+60 and yperso >= y-50 and yperso <= y+30:               #Si le personnage est dans la zone de détection droite d'un bloc:
                        keydownl = 0                                                                                #Son déplacement vers la gauche est annulé
                        touch = 1
                    elif xperso >= x and xperso <= x+50 and yperso >= y-100 and yperso <= y:                    #Si le personnage est dans la zone de détection supérieure d'un bloc:    
                        vit, y_perso, og = 0, y-100, 1                                                              #Sa chute est arrêtée, et il lui est empêché de traverser le bloc
                        touch = 1
                    elif xperso >= x-20 and xperso <= x and yperso >= y+50 and yperso <= y+70:                  #Si le personnage est dans la zone de détection inférieure d'un bloc:
                        y_perso = y+50                                                                              #Sa position est corrigée, il est renvoyé au-dessus du bloc
                        touch = 1
                    else:
                        touch = 0
                elif sprite == 'y':                                                                         #Si le sprite (lettre) lu est un y:                     
                    fenetre.blit(drapeau, (x,y))                                                                #Un drapeau est affiché aux coordonnées x et y
                    if xperso >= x-20 and x_perso <= x+60 and yperso >= y-50 and yperso <= y+30 and chgniveau2 == 0:
                        niveauactuel += 1
                        chgniveau = 1
                elif sprite == 'o':
                    fenetre.blit(eau,(x,y))
                    if xperso >= x-20 and x_perso <= x+60 and yperso >= y-50 and yperso <= y+30 and chgniveau2 == 0:
                        vie = 0
                ncase +=1                                                                                   #On passe à la prochaine case 
            nligne += 1                                                                                 #On passe à la prochaine ligne

depart = 1
continu = 0
     

#DEBUT DE LA BOUCLE DU JEU#
while continuer:
    if depart == 1:
        fenetre.blit(acceuil, (0, 0))
        fenetre.blit(difficulte, (550, 400))
        souris = pygame.mouse.get_pos()
        xsouris = souris[0]
        ysouris = souris[1]
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if xsouris >= 559 and xsouris <= 670 and ysouris >= 410 and ysouris <= 540:
                    continu = 1
                    depart = 0
                    diff = 1
                if xsouris >= 680 and xsouris <= 810 and ysouris >= 410 and ysouris <= 540:
                    continu = 1
                    depart = 0
                    diff = 2
                if xsouris >= 820 and xsouris <= 930 and ysouris >= 410 and ysouris <= 540:
                    continu = 1
                    depart = 0
                    diff = 3
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:                   #Si l'évenement est de type QUIT (appui sur la croix rouge) ou si c'est un appui sur la touche "échap":
                continuer = 0                                                                               #On arrête la boucle et donc le jeu
        if diff == 2:
            vie = 3
        elif diff == 3:
            vie = 1
                
        pygame.display.flip()
    if continu == 1:
        fenetre.blit(fond, (0,0))                                                                   #Affichage du fond d'écran                                                
        if niveauactuel == 1:                                                                       #Si le niveau actuel est le premier:
            niveau = Niveau("n1")                                                                       #On charge le niveau 1
        elif niveauactuel == 2:                                                                     #Si le niveau actuel est le second:
            niveau = Niveau("n2")                                                                       #On charge le niveau 2
            if chgniveau == 1:                                                                         #Si le joueur vient de finir le niveau 1:
                if diff == 1:
                    vie += 1
                x_perso, y_perso = 0, 400                                                               #Le joueur est placé au début du deuxième niveau
                enviep2, enviep3 = 1, 1                                                                 #Les deux paysans du niveau sont activés
                chgniveau = 0
                fond = fond2                                                                           #On change le fond d'écran
        elif niveauactuel == 3:
            niveau = Niveau("n3")
            if chgniveau == 1:                                                                         #Si le joueur vient de finir le niveau 1:
                if diff == 1:
                    vie += 1
                x_perso, y_perso = 0, 300                                                               #Le joueur est placé au début du deuxième niveau
                enviep2, enviep3 = 1, 1                                                                 #Les deux paysans du niveau sont activés
                chgniveau = 0
                fond = fond3
        niveau.creer()                                                                              #On charge le niveau actuel
        
        for event in pygame.event.get():                                                            #Pour tout évenement acquis par l'ordinateur (clavier, souris, etc..):    
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:                   #Si l'évenement est de type QUIT (appui sur la croix rouge) ou si c'est un appui sur la touche "échap":
                continuer = 0                                                                               #On arrête la boucle et donc le jeu
            if event.type == KEYDOWN:                                                                   #Si l'évenement est de type appui sur une touche du clavier:            
                if event.key == K_LEFT:                                                                     #Si la touche pressée est la flèche de gauche:
                    keydownl = 1                                                                                #On ordonne un mouvement du joueur vers la gauche
                    direction = -1                                                                              #On indique qu'il s'oriente vers la gauche
                if event.key == K_RIGHT:                                                                    #Si la touche pressée est la flèche de droite:
                    keydownr = 1                                                                                #On ordonne un mouvement du joueur vers la droite
                    direction = 1                                                                               #On indique qu'il s'oriente vers la droite
                if event.key == K_UP:                                                                       #Si la touche pressée est la flèche du haut:
                    keydownu = 1                                                                                #On ordonne un saut
                if event.key == K_RETURN:                                                                   #Si la touche pressée est la touche "Entrée":
                    entree = int(input(""))                                                                     #On attend une entrée sous forme de texte/caractères dans la console
                if event.key == K_r:                                                                        #Si la touche pressée est la touche "R":
                    ralentissement = 1                                                                          #On ordonne de ralentir le jeu
                if event.key == K_p:                                                                        #Si la touche pressée est la touche "P":
                    pause = 1                                                                                   #On ordonne de mettre le jeu en pause
                if event.key == K_SPACE:                                                                    #Si la touche pressée est la "Barre espace":
                    attack = 1                                                                                  #On ordonne au personnage d'attaquer
            if event.type == KEYUP:                                                                     #Si l'évenement est de type relâchement d'une touche:
                if event.key == K_LEFT:                                                                     #Si la touche relachée est la flèche gauche:
                    keydownl = 0                                                                                #On ordonne d'arrêter le mouvement vers la gauche
                if event.key == K_RIGHT:                                                                    #Si la touche relachée est la flèche droite:
                    keydownr = 0                                                                                #On ordonne d'arrêter le mouvement vers la droite
                if event.key == K_UP:                                                                       #Si la touche relachée est la flèche haut:
                    keydownu = 0                                                                                #On ordonne d'arrêter le saut
                if event.key == K_r:                                                                        #Si la touche relachée est la touche "R":
                    ralentissement = 0                                                                          #On arrête le ralentissement du jeu
                if event.key == K_p:                                                                        #Si la touche relachée est la touche "P":
                    pause = 0                                                                                   #On arrête la mise en pause du jeu

        if ralentissement == 1:                                                                             #Si un ralentissement a été ordonnée:
            pygame.time.wait(200)                                                                               #La boucle fait une pause de 200 millisecondes à chaque execution                 
        
        if pause == 0:                                                                                      #Si une pause n'a pas été ordonnée (et donc que le jeu peut fonctionner normalement):
            if y_perso <= 730:                                                                                  #Si le personnage est au-dessus la limite basse:  
                vit += 0.5                                                                                          #Sa vitesse de chute augmente                      
            if vit >= 1:                                                                                        #S'il a une vitesse de chute:
                og = 0                                                                                              #Il n'est plus sur le sol

            if keydownu == 1:                                                                                   #Si un ordre de saut a été donné:
                if y_perso >= 727 or og == 1:                                                                       #Si le personnage est sur la limite basse ou qu'il est sur le sol:
                    oui = 1                                                                                             #Le saut est authorisé
            if oui == 1:                                                                                        #Si le saut est authorisé:                          
                if i < 20:                                                                                          #Si le compteur "i" est inférieur à 20:
                    y_perso -= 10                                                                                       #Le personnage monte
                    i += 1                                                                                              #On incrémente le compteur "i"
                if i >= 20:                                                                                         #Si le compteur "i" a atteint ou depassé 20:
                    i = 0                                                                                               #On réinitialise le compteur "i"
                    oui = 0                                                                                             #On réinitialise l'authorisation de saut
                og = 0                                                                                              #On indique que le personnage est en l'air

            if direction == -1 and attack != 1:
                perso = pygame.image.load("h1g.png").convert_alpha()
                if og == 0:
                    perso = pygame.image.load("h1sg.png").convert_alpha()
            if direction == 1 and attack != 1:
                perso = pygame.image.load("h1d.png").convert_alpha()
                if og == 0:
                    perso = pygame.image.load("h1sd.png").convert_alpha()

            niveau.affichage(fenetre, x_perso, y_perso, chgniveau)
            texte = font.render(str(y_perso), 1, (255,255,255)) #indicateur
            texte1 = font.render(str(x_perso), 1, (255,255,255))
            if oui == 0:                                        #gravité
                if y_perso < 752:
                        y_perso += vit
                elif y_perso >= 752:
                        y_perso = 752
                        vit = 0

            #attaque
            if attack == 1:
                if direction == -1:
                    perso = pygame.image.load("herosheadag.png").convert_alpha()
                    if og != 1:
                        perso = pygame.image.load("herosheadagj.png").convert_alpha()
                    if niveauactuel == 1:
                        if x_perso >= 850 and x_perso <= 970 and y_perso >= 200 and y_perso <= 500:
                            enviep1 = 0
                    if niveauactuel == 2:
                        if x_perso >= 300 and x_perso <= 420 and y_perso >= 150 and y_perso <= 450:
                            enviep3 = 0
                if direction == 1:
                    perso = pygame.image.load("herosheada.png").convert_alpha()
                    if og != 1:
                        perso = pygame.image.load("herosheadaj.png").convert_alpha()
                    if niveauactuel == 1:
                        if x_perso >= 750 and x_perso <= 900 and y_perso >= 200 and y_perso <= 500:
                            enviep1 = 0
                    if niveauactuel == 2:
                        if x_perso >= 200 and x_perso <= 350 and y_perso >= 150 and y_perso <= 450:
                            enviep2 = 0
                        if x_perso >= 1200 and x_perso <= 1350 and y_perso >= 350 and y_perso <= 800:
                            enviep3 = 0
                tma += 1
                if tma >= 5:
                    attack = 0
                    tma = 0

            #Paysans#
            if niveauactuel == 1:       
                if enviep1 == 1:
                    if x_paysan1 > 780 and x_paysan1 <= 830 and x_paysan1 > x_perso:
                        x_paysan1 -= 1
                        paysan = pygame.image.load("paysan.png")
                    elif x_paysan1 >= 780 and x_paysan1 < 830 and x_paysan1 < x_perso:
                        x_paysan1 += 1
                        paysan = pygame.image.load("paysan1.png")
                    if x_paysan1 <= 780:
                        x_paysan1 = 780
                    elif x_paysan1 >= 830:
                        x_paysan1 = 830
                    if x_perso >= 800 and x_perso < 850:
                        kickg = 1
                        vie -= 1
                    elif x_perso >= 850 and x_perso <= 900:
                        kickd = 1
                        vie -= 1
            if niveauactuel == 2:
                if enviep2 == 1:
                    if x_paysan2 > 230 and x_paysan2 <= 280 and x_paysan2 > x_perso:
                        x_paysan2 -= 1
                        paysan = pygame.image.load("paysan.png")
                    elif x_paysan2 >= 230 and x_paysan2 < 280 and x_paysan2 < x_perso:
                        x_paysan2 += 1
                        paysan = pygame.image.load("paysan1.png")
                    if x_paysan2 <= 230:
                        x_paysan2 = 230
                    elif x_paysan2 >= 280:
                        x_paysan2 = 280
                    if x_perso >= 250 and x_perso < 300:
                        kickg = 1
                        vie -= 1
                    elif x_perso >= 300 and x_perso <= 350:
                        kickd = 1
                        vie -= 1
                if enviep3 == 1:
                    if x_paysan3 > 1230 and x_paysan3 <= 1280 and x_paysan3 > x_perso:
                        x_paysan3 -= 1
                        paysan = pygame.image.load("paysan.png")
                    elif x_paysan3 >= 1230 and x_paysan3 < 1280 and x_paysan3 < x_perso:
                        x_paysan3 += 1
                        paysan = pygame.image.load("paysan1.png")
                    if x_paysan3 <= 1230:
                        x_paysan3 = 1230
                    elif x_paysan3 >= 1280:
                        x_paysan3 = 1280
                    if x_perso >= 1250 and x_perso < 1300 and y_perso >= 410:
                        kickg = 1
                        vie -= 1
                    elif x_perso >= 1300 and x_perso <= 1350 and y_perso >= 410:
                        kickd = 1
                        vie -= 1

            if kickg == 1 and ct <= 20 or kickd == 1 and ct <= 20:
                keydownr, keydownl = 0, 0
                ct += 1
                if kickg == 1 and ct <= 20 and touch == 0:
                    x_perso -= 10
                elif kickg == 1 and ct <= 20 and touch == 1:
                    x_perso += 10
                elif kickd == 1 and ct <= 20 and touch == 0:
                    x_perso += 10
                elif kickd == 1 and ct <= 20 and touch == 1:
                    x_perso -= 10
            elif ct > 20:
                ct = 0
                kickg, kickd = 0, 0
            
            if keydownl == 1:                                   #propriété par touche
                x_perso -= 10
            if keydownr == 1:
                x_perso += 10

            if x_perso < 0:
                x_perso = 0

            #codes   
            if entree == 1:
                x_perso = int(input("x:"))
                y_perso = int(input("y:"))
                entree = 0
            if entree == 2:
                envie = 0

            time.sleep(0.005)       
            fenetre.blit(perso, (x_perso, y_perso+10))
            if enviep1 == 1:
                fenetre.blit(paysan, (x_paysan1, y_paysan1))
            if enviep2 == 1:
                fenetre.blit(paysan, (x_paysan2, y_paysan2))
            if enviep3 == 1:
                fenetre.blit(paysan, (x_paysan3, y_paysan3))
            if vie >= 1:
                fenetre.blit(bvp, (900, 300))
            if vie >= 2:
                fenetre.blit(bvp, (910, 300))
            if vie >= 3:
                fenetre.blit(bvp, (920, 300))
            if vie >= 4:
                fenetre.blit(bvp, (930, 300))
            if vie == 5:
                fenetre.blit(bvp, (940, 300))
            pygame.display.flip()                               #boucle

            if vie == 0:
                fenetre.blit(perdu, (0, 0))
                pygame.display.flip()
                time.sleep(10)
                continuer = 0


