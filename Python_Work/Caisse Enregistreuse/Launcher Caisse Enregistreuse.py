#######Programme Caisse Enregistreuse#########
#######Quentin MELLARD et Ethan FUCHS#########

###IMPORTATION###
#Importation des polices de caractère du module tkinter
import tkinter.font as tkFont

#Importation de la fonction tk du module tkinter permettant nottamment de respecter la dernière mise à niveau syntaxique du module tkinter et de Python
import tkinter as tk

#Importation des modules time, csv et os permettant respectivement d'importer les valeurs temporelle de l'ordinateur, la création et la modification de tableur
#et la création de fichier et de dossier
import time, csv, os

#Imporation du sous-module path du module os afin de naviguer dans différent dossier et chemin de l'ordinateur
import os.path

###DECLARATION DES DIFFERENTES VARIABLES DU PROGRAMME###
#La variable m correspond à la position relative des articles à afficher sur le canvas.
#La variable men correspond aux menus qui s'affiche.
#La variable down correspond à la position relative des articles à afficher sur le canvas.
#La variable ann correspond à la position relative des articles à afficher sur le canvas.
#La variable debc correspond à la position relative des articles à afficher sur le canvas.
#La variable mdp correspond à la validiter du mot de passe.
m,men,down,ann,debc,e=0,0,0,0,0,0
mdp=False

#Ecriture dans un fichier texte des noms et des prix des articles
#
#
#
#

#Liste des différents nom de produit
na_art=["Pizza","Flamme","Knack","Merguez","Saucisse Blanche","","","","","","","",
        "Café","Bière","Oranginas","Coca","Eau Pétillante","Eau Plate","Panaché","Picon","Verre de Blanc","Verre de Rouge","","",
        "Gâteau","Glace","Barbe à papa","Crêpe","","","","","","","",""]

#Texte du tichet de caisse et de l'affichage ainsi que les différentes coordonnées de chaque parti du texte.
txt,coord=["Nom de l'entreprise ou de l'associtation","Slogan","Numéro de téléphone","mail","-------------------------------------------"],[245,20,50,70,90,110]

###DEFINITION ET FONCTION###
#Fonction permettant la mise à jour des article (principalement des noms)
def affichage():
   #Récupération des différentes variable
   global m, Caisse, mdp, helv15, helv10, qb_repas, qb_boisson, qb_dessert, qb_but0_txt, qb_but1_txt, qb_but2_txt, qb_but3_txt, qb_but4_txt, qb_but5_txt, qb_but6_txt, qb_but7_txt, qb_but8_txt, qb_but9_txt, qb_but10_txt, qb_but11_txt,qb_but0, qb_but1, qb_but2, qb_but3, qb_but4, qb_but5, qb_but6, qb_but7, qb_but8, qb_but9, qb_but10, qb_but11
   #Vérification du mot de passe
   if mdp==True:
      #Déclaration de la variable caisse et lancement de la fenêtre Tkinter
      Caisse=tk.Tk()
      #Titre de la fenêtre
      Caisse.title("Caisse enregistreuse")
      #Couleur du fond de la fenêtre
      Caisse["bg"]="#CECECE"
      #Police de caractère en taille 15
      helv15 = tkFont.Font(size=15,weight='bold')
      #Police de caractère en taille 10
      helv10 = tkFont.Font(size=10,weight='bold')
      ##Création ticket de caisse
      #Création de la barre de défilement (scrolling)
      scrollbar=tk.Scrollbar(Caisse)
      #Création du canvas
      can=tk.Canvas(Caisse, width=478, height=256, bg="white", yscrollcommand=scrollbar.set)
      #Boucle pour chaque partie du texte
      for i in range(0,len(txt)):
         #Insertion du texte de la liste "txt" au coordonnées indiquer dans la liste "coord"
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la fenêtre (Dans une grille (similaire au tableur) invisible de la ligne 0 à la ligne 1 et de la colonne 3 à la colonne 4,
      #il aura donc 4 cellules de surface)
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Liaison de la barre de défilement avec le canvas
      scrollbar.config(command=can.yview,width=530)
      #Position de la barre de défilement par rapport au milieu de l'espace attribué (la fenêtre ou la cellule
      scrollbar.set(170+13*m,0)
      #Position de la barre de défilement par rapport à la grille
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
      ##Création des boutons ainsi que leur disposition et leur taille
      #Création du bouton Repas
      qb_repas=tk.Button(Caisse,text="Repas",bg="white",overrelief="raised",borderwidth=15,font=helv15,command=f1)
      #Création du bouton Boisson
      qb_boisson=tk.Button(Caisse,text="Boisson",bg="cyan",overrelief="raised",borderwidth=15,font=helv15,command=f2)
      #Création du bouton Dessert
      qb_dessert=tk.Button(Caisse,text="Dessert",bg="yellow",overrelief="raised",borderwidth=15,font=helv15,command=f3)
      #Création de la variable texte du bouton 0
      qb_but0_txt=tk.StringVar()
      #Création de la variable texte du bouton 1
      qb_but1_txt=tk.StringVar()
      #Création de la variable texte du bouton 2
      qb_but2_txt=tk.StringVar()
      #Création de la variable texte du bouton 3
      qb_but3_txt=tk.StringVar()
      #Création de la variable texte du bouton 4
      qb_but4_txt=tk.StringVar()
      #Création de la variable texte du bouton 5
      qb_but5_txt=tk.StringVar()
      #Création de la variable texte du bouton 6
      qb_but6_txt=tk.StringVar()
      #Création de la variable texte du bouton 7
      qb_but7_txt=tk.StringVar()
      #Création de la variable texte du bouton 8
      qb_but8_txt=tk.StringVar()
      #Création de la variable texte du bouton 9
      qb_but9_txt=tk.StringVar()
      #Création de la variable texte du bouton 10
      qb_but10_txt=tk.StringVar()
      #Création de la variable texte du bouton 11
      qb_but11_txt=tk.StringVar()
      #Création du bouton 0
      qb_but0=tk.Button(Caisse,textvariable=qb_but0_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f4)
      #Création du bouton 1
      qb_but1=tk.Button(Caisse,textvariable=qb_but1_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f5)
      #Création du bouton 2
      qb_but2=tk.Button(Caisse,textvariable=qb_but2_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f6)
      #Création du bouton 3
      qb_but3=tk.Button(Caisse,textvariable=qb_but3_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f7)
      #Création du bouton 4
      qb_but4=tk.Button(Caisse,textvariable=qb_but4_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f8)
      #Création du bouton 5
      qb_but5=tk.Button(Caisse,textvariable=qb_but5_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f9)
      #Création du bouton 6
      qb_but6=tk.Button(Caisse,textvariable=qb_but6_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f10)
      #Création du bouton 7
      qb_but7=tk.Button(Caisse,textvariable=qb_but7_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f11)
      #Création du bouton 8
      qb_but8=tk.Button(Caisse,textvariable=qb_but8_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f12)
      #Création du bouton 9
      qb_but9=tk.Button(Caisse,textvariable=qb_but9_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f13)
      #Création du bouton 10
      qb_but10=tk.Button(Caisse,textvariable=qb_but10_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f14)
      #Création du bouton 11
      qb_but11=tk.Button(Caisse,textvariable=qb_but11_txt,background="white",overrelief="raised",borderwidth=15,font=helv15,command=f15)
      #Mise à jour de la variable texte du bouton 0
      qb_but0_txt.set(na_art[0])
      #Mise à jour de la variable texte du bouton 1
      qb_but1_txt.set(na_art[1])
      #Mise à jour de la variable texte du bouton 2
      qb_but2_txt.set(na_art[2])
      #Mise à jour de la variable texte du bouton 3
      qb_but3_txt.set(na_art[3])
      #Mise à jour de la variable texte du bouton 4
      qb_but4_txt.set(na_art[4])
      #Mise à jour de la variable texte du bouton 5
      qb_but5_txt.set(na_art[5])
      #Mise à jour de la variable texte du bouton 6
      qb_but6_txt.set(na_art[6])
      #Mise à jour de la variable texte du bouton 7
      qb_but7_txt.set(na_art[7])
      #Mise à jour de la variable texte du bouton 8
      qb_but8_txt.set(na_art[8])
      #Mise à jour de la variable texte du bouton 9
      qb_but9_txt.set(na_art[9])
      #Mise à jour de la variable texte du bouton 10
      qb_but10_txt.set(na_art[10])
      #Mise à jour de la variable texte du bouton 11
      qb_but11_txt.set(na_art[11])
      #Création du bouton Total
      qb_Total=tk.Button(Caisse,text="Total",background="blue",overrelief="raised",borderwidth=15,font=helv15,command=f16)
      #Création du bouton Enregistrer
      qb_Enregistrer=tk.Button(Caisse,text="Enregistrer",background="blue",overrelief="raised",borderwidth=15,font=helv15,command=f17)
      #Création du bouton Fermer
      qb_Fermer=tk.Button(Caisse,text="Fermer",background="blue",overrelief="raised",borderwidth=15,font=helv15,command=Caisse.destroy)
      #Création du bouton Annuler
      qb_Annuler=tk.Button(Caisse,text="Annuler",background="blue",overrelief="raised",borderwidth=15,font=helv15, command=f19)
      #Création du bouton Paramètres
      qb_Paramètres=tk.Button(Caisse,text="Paramètres",background="blue",overrelief="raised",borderwidth=15,font=helv15,command=f20)
      #Création du bouton Aide permettant de connaître les dévelloppeurs du logiciel
      qb_Aide=tk.Button(Caisse,wraplength=250,text="A propos de la Caisse Enregisteuse",background="blue",overrelief="raised",borderwidth=15,font=helv15,command=f21)
      #Taille du bouton Repas
      qb_repas.config(height=4,width=19)
      #Taille du bouton Boisson
      qb_boisson.config(height=4,width=19)
      #Taille du bouton Dessert
      qb_dessert.config(height=4,width=19)
      #Taille du bouton 0
      qb_but0.config(height=4,width=19)
      #Taille du bouton 1
      qb_but1.config(height=4,width=19)
      #Taille du bouton 2
      qb_but2.config(height=4,width=19)
      #Taille du bouton 3
      qb_but3.config(height=4,width=19)
      #Taille du bouton 4
      qb_but4.config(height=4,width=19)
      #Taille du bouton 5
      qb_but5.config(height=4,width=19)
      #Taille du bouton 6
      qb_but6.config(height=4,width=19)
      #Taille du bouton 7
      qb_but7.config(height=4,width=19)
      #Taille du bouton 8
      qb_but8.config(height=4,width=19)
      #Taille du bouton 9
      qb_but9.config(height=4,width=19)
      #Taille du bouton 10
      qb_but10.config(height=4,width=19)
      #Taille du bouton 11
      qb_but11.config(height=4,width=19)
      #Taille du bouton Total
      qb_Total.config(height=4,width=19)
      #Taille du bouton Enregistrer
      qb_Enregistrer.config(height=4,width=19)
      #Taille du bouton Fermer
      qb_Fermer.config(height=4,width=19)
      #Taille du bouton Annuler
      qb_Annuler.config(height=4,width=19)
      #Taille du bouton Paramètre
      qb_Paramètres.config(height=4,width=19)
      #Taille du bouton Aide
      qb_Aide.config(height=4,width=19)
      #Disposition du bouton Repas dans la grille
      qb_repas.grid(row=0,column=0)
      #Disposition du bouton Boisson dans la grille
      qb_boisson.grid(row=0,column=1)
      #Disposition du bouton Dessert dans la grille
      qb_dessert.grid(row=0,column=2)
      #Disposition du bouton 0 dans la grille
      qb_but0.grid(row=1, column=0)
      #Disposition du bouton 1 dans la grille
      qb_but1.grid(row=1, column=1)
      #Disposition du bouton 2 dans la grille
      qb_but2.grid(row=1, column=2)
      #Disposition du bouton 3 dans la grille
      qb_but3.grid(row=2, column=0)
      #Disposition du bouton 4 dans la grille
      qb_but4.grid(row=2, column=1)
      #Disposition du bouton 5 dans la grille
      qb_but5.grid(row=2, column=2)
      #Disposition du bouton 6 dans la grille
      qb_but6.grid(row=3, column=0)
      #Disposition du bouton 7 dans la grille
      qb_but7.grid(row=3, column=1)
      #Disposition du bouton 8 dans la grille
      qb_but8.grid(row=3, column=2)
      #Disposition du bouton 9 dans la grille
      qb_but9.grid(row=4, column=0)
      #Disposition du bouton 10 dans la grille
      qb_but10.grid(row=4, column=1)
      #Disposition du bouton 11 dans la grille
      qb_but11.grid(row=4, column=2)
      #Disposition du bouton Total dans la grille
      qb_Total.grid(row=2, column=3)
      #Disposition du bouton Enregistrer dans la grille
      qb_Enregistrer.grid(row=2, column=4)
      #Disposition du bouton Fermer dans la grille
      qb_Fermer.grid(row=3, column=3)
      #Disposition du bouton Annuler dans la grille
      qb_Annuler.grid(row=3, column=4)
      #Disposition du bouton Paramètres dans la grille
      qb_Paramètres.grid(row=4, column=3)
      #Disposition du bouton Aide dans la grille
      qb_Aide.grid(row=4, column=4)
      #Déclaration de la boucle de la fenêtre Caisse
      Caisse.mainloop()

#Fonction d'actualisation du dictionnaire article
def factu():
   #Récupération de la variable men
   global article
   #Liste de tout les articles dans l'ordre des pages (ligne 1 = repas, ligne 2 et 3 = dessert, ligne 4 = boisson, ligne 5, 6 et 7 = produit vide)
   article={na_art[0]:[10,7,0,0],na_art[1]:[10,7,0,0],na_art[2]:[10,4,0,0],na_art[3]:[10,4,0,0],na_art[4]:[10,4,0,0],
            na_art[12]:[10,1,0,0],na_art[13]:[10,2.5,0,0],na_art[14]:[10,2,0,0],na_art[15]:[10,2,0,0],na_art[16]:[10,2,0,0],na_art[17]:[10,2,0,0],
            na_art[18]:[10,2,0,0],na_art[19]:[10,2.5,0,0],na_art[20]:[10,2,0,0],na_art[21]:[10,2,0,0],
            na_art[24]:[10,1,0,0],na_art[25]:[10,1,0,0],na_art[26]:[10,1,0,0],na_art[27]:[10,1,0,0],
            na_art[5]:[10,7,0,0],na_art[6]:[10,7,0,0],na_art[7]:[10,4,0,0],na_art[8]:[10,4,0,0],na_art[9]:[10,4,0,0],na_art[10]:[10,7,0,0],na_art[11]:[10,7,0,0],
            na_art[22]:[10,0,0,0],na_art[23]:[10,0,0,0],na_art[28]:[10,0,0,0],na_art[29]:[10,0,0,0],na_art[30]:[10,0,0,0],na_art[31]:[10,0,0,0],na_art[32]:[10,0,0,0],
            na_art[33]:[10,0,0,0],na_art[34]:[10,0,0,0],na_art[35]:[10,0,0,0]}

#Actualisation de démarrage du dictionnaire article
factu()

#Fonction du bouton repas
def f1():
   #Récupération de la variable men
   global m, Caisse, men
   #Variable men mis à 0 afin d'indiqué le menu actuelle au différentes fonctions de chaque bouton
   men=0
   #Texte écrit sur le bouton numéros 1
   qb_but0_txt.set(na_art[0])
   #Texte écrit sur le bouton numéros 2
   qb_but1_txt.set(na_art[1])
   #Texte écrit sur le bouton numéros 3
   qb_but2_txt.set(na_art[2])
   #Texte écrit sur le bouton numéros 4
   qb_but3_txt.set(na_art[3])
   #Texte écrit sur le bouton numéros 5
   qb_but4_txt.set(na_art[4])
   #Texte écrit sur le bouton numéros 6
   qb_but5_txt.set(na_art[5])
   #Texte écrit sur le bouton numéros 7
   qb_but6_txt.set(na_art[6])
   #Texte écrit sur le bouton numéros 8
   qb_but7_txt.set(na_art[7])
   #Texte écrit sur le bouton numéros 9
   qb_but8_txt.set(na_art[8])
   #Texte écrit sur le bouton numéros 10
   qb_but9_txt.set(na_art[9])
   #Texte écrit sur le bouton numéros 11
   qb_but10_txt.set(na_art[10])
   #Texte écrit sur le bouton numéros 12
   qb_but11_txt.set(na_art[11])
   ##Mise à jour de la couleur en blanc
   #Mise à jour de la couleur blanc sur le bouton 0
   qb_but0.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 1
   qb_but1.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 2
   qb_but2.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 3
   qb_but3.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 4
   qb_but4.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 5
   qb_but5.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 6
   qb_but6.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 7
   qb_but7.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 8
   qb_but8.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 9
   qb_but9.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 10
   qb_but10.configure(bg = "white")
   #Mise à jour de la couleur blanc sur le bouton 11
   qb_but11.configure(bg = "white")

#Fonction du bouton dessert
def f2():
   #Récupération de la variable men
   global m, Caisse, men
   #Variable men mis à 0 afin d'indiqué le menu actuelle au différentes fonctions de chaque bouton
   men=1
   #Texte écrit sur le bouton numéros 13
   qb_but0_txt.set(na_art[12])
   #Texte écrit sur le bouton numéros 14
   qb_but1_txt.set(na_art[13])
   #Texte écrit sur le bouton numéros 15
   qb_but2_txt.set(na_art[14])
   #Texte écrit sur le bouton numéros 16
   qb_but3_txt.set(na_art[15])
   #Texte écrit sur le bouton numéros 17
   qb_but4_txt.set(na_art[16])
   #Texte écrit sur le bouton numéros 18
   qb_but5_txt.set(na_art[17])
   #Texte écrit sur le bouton numéros 19
   qb_but6_txt.set(na_art[18])
   #Texte écrit sur le bouton numéros 20
   qb_but7_txt.set(na_art[19])
   #Texte écrit sur le bouton numéros 21
   qb_but8_txt.set(na_art[20])
   #Texte écrit sur le bouton numéros 22
   qb_but9_txt.set(na_art[21])
   #Texte écrit sur le bouton numéros 23
   qb_but10_txt.set(na_art[22])
   #Texte écrit sur le bouton numéros 24
   qb_but11_txt.set(na_art[23])
   ##Mise à jour de la couleur en cyan
   #Mise à jour de la couleur cyan sur le bouton 0
   qb_but0.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 1
   qb_but1.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 2
   qb_but2.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 3
   qb_but3.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 4
   qb_but4.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 5
   qb_but5.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 6
   qb_but6.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 7
   qb_but7.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 8
   qb_but8.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 9
   qb_but9.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 10
   qb_but10.configure(bg = "cyan")
   #Mise à jour de la couleur cyan sur le bouton 11
   qb_but11.configure(bg = "cyan")

#Fonction du bouton boisson
def f3():
   #Récupération de la variable men
   global m, Caisse, men
   #Variable men mis à 0 afin d'indiqué le menu actuelle au différentes fonctions de chaque bouton
   men=2
   #Texte écrit sur le bouton numéros 25
   qb_but0_txt.set(na_art[24])
   #Texte écrit sur le bouton numéros 26
   qb_but1_txt.set(na_art[25])
   #Texte écrit sur le bouton numéros 27
   qb_but2_txt.set(na_art[26])
   #Texte écrit sur le bouton numéros 28
   qb_but3_txt.set(na_art[27])
   #Texte écrit sur le bouton numéros 29
   qb_but4_txt.set(na_art[28])
   #Texte écrit sur le bouton numéros 30
   qb_but5_txt.set(na_art[29])
   #Texte écrit sur le bouton numéros 31
   qb_but6_txt.set(na_art[30])
   #Texte écrit sur le bouton numéros 32
   qb_but7_txt.set(na_art[31])
   #Texte écrit sur le bouton numéros 33
   qb_but8_txt.set(na_art[32])
   #Texte écrit sur le bouton numéros 34
   qb_but9_txt.set(na_art[33])
   #Texte écrit sur le bouton numéros 35
   qb_but10_txt.set(na_art[34])
   #Texte écrit sur le bouton numéros 36
   qb_but11_txt.set(na_art[35])
   ##Mise à jour de la couleur en jaune
   #Mise à jour de la couleur jaune sur le bouton 0
   qb_but0.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 1
   qb_but1.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 2
   qb_but2.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 3
   qb_but3.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 4
   qb_but4.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 5
   qb_but5.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 6
   qb_but6.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 7
   qb_but7.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 8
   qb_but8.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 9
   qb_but9.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 10
   qb_but10.configure(bg = "yellow")
   #Mise à jour de la couleur jaune sur le bouton 11
   qb_but11.configure(bg = "yellow")

#Fonction du bouton 1
def f4():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[0]) in txt:
         article[na_art[0]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[0])
         down=130+13*m
         coord.append(down)
         article[na_art[0]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[0]][3]=article[na_art[0]][1]*article[na_art[0]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[12]) in txt:
         article[na_art[12]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[12])
         down=130+13*m
         coord.append(down)
         article[na_art[12]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[12]][3]=article[na_art[12]][1]*article[na_art[12]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Desser est actif
   elif men==2:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[24]) in txt:
         article[na_art[24]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[24])
         down=130+13*m
         coord.append(down)
         article[na_art[24]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[24]][3]=article[na_art[24]][1]*article[na_art[24]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 2
def f5():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[1]) in txt:
         article[na_art[1]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[1])
         down=130+13*m
         coord.append(down)
         article[na_art[1]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[1]][3]=article[na_art[1]][1]*article[na_art[1]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[13]) in txt:
         article[na_art[13]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[13])
         down=130+13*m
         coord.append(down)
         article[na_art[13]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[13]][3]=article[na_art[13]][1]*article[na_art[13]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[25]) in txt:
         article[na_art[25]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[25])
         down=130+13*m
         coord.append(down)
         article[na_art[25]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[25]][3]=article[na_art[25]][1]*article[na_art[25]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 3
def f6():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[2]) in txt:
         article[na_art[2]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[2])
         down=130+13*m
         coord.append(down)
         article[na_art[2]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[2]][3]=article[na_art[2]][1]*article[na_art[2]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[14]) in txt:
         article[na_art[14]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[14])
         down=130+13*m
         coord.append(down)
         article[na_art[14]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[14]][3]=article[na_art[14]][1]*article[na_art[14]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[26]) in txt:
         article[na_art[26]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[26])
         down=130+13*m
         coord.append(down)
         article[na_art[26]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[26]][3]=article[na_art[26]][1]*article[na_art[26]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 4
def f7():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[3]) in txt:
         article[na_art[3]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[3])
         down=130+13*m
         coord.append(down)
         article[na_art[3]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[3]][3]=article[na_art[3]][1]*article[na_art[3]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[15]) in txt:
         article[na_art[15]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[15])
         down=130+13*m
         coord.append(down)
         article[na_art[15]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[15]][3]=article[na_art[15]][1]*article[na_art[15]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[27]) in txt:
         article[na_art[27]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[27])
         down=130+13*m
         coord.append(down)
         article[na_art[27]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[27]][3]=article[na_art[27]][1]*article[na_art[27]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 5
def f8():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[4]) in txt:
         article[na_art[4]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[4])
         down=130+13*m
         coord.append(down)
         article[na_art[4]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[4]][3]=article[na_art[4]][1]*article[na_art[4]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[16]) in txt:
         article[na_art[16]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[16])
         down=130+13*m
         coord.append(down)
         article[na_art[16]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[16]][3]=article[na_art[16]][1]*article[na_art[16]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[28]) in txt:
         article[na_art[28]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[28])
         down=130+13*m
         coord.append(down)
         article[na_art[28]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[28]][3]=article[na_art[28]][1]*article[na_art[28]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 6
def f9():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[5]) in txt:
         article[na_art[5]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[5])
         down=130+13*m
         coord.append(down)
         article[na_art[5]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[5]][3]=article[na_art[5]][1]*article[na_art[5]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[17]) in txt:
         article[na_art[17]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[17])
         down=130+13*m
         coord.append(down)
         article[na_art[17]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[17]][3]=article[na_art[17]][1]*article[na_art[17]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[29]) in txt:
         article[na_art[29]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[29])
         down=130+13*m
         coord.append(down)
         article[na_art[29]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[29]][3]=article[na_art[29]][1]*article[na_art[29]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 7
def f10():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[6]) in txt:
         article[na_art[6]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[6])
         down=130+13*m
         coord.append(down)
         article[na_art[6]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[6]][3]=article[na_art[6]][1]*article[na_art[6]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[18]) in txt:
         article[na_art[18]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[18])
         down=130+13*m
         coord.append(down)
         article[na_art[18]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[18]][3]=article[na_art[18]][1]*article[na_art[18]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[30]) in txt:
         article[na_art[30]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[30])
         down=130+13*m
         coord.append(down)
         article[na_art[30]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[30]][3]=article[na_art[30]][1]*article[na_art[30]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 8
def f11():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[7]) in txt:
         article[na_art[7]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[7])
         down=130+13*m
         coord.append(down)
         article[na_art[7]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[7]][3]=article[na_art[7]][1]*article[na_art[7]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[19]) in txt:
         article[na_art[19]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[19])
         down=130+13*m
         coord.append(down)
         article[na_art[19]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[19]][3]=article[na_art[19]][1]*article[na_art[19]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[31]) in txt:
         article[na_art[31]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[31])
         down=130+13*m
         coord.append(down)
         article[na_art[31]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[31]][3]=article[na_art[31]][1]*article[na_art[31]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 9
def f12():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[8]) in txt:
         article[na_art[8]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[8])
         down=130+13*m
         coord.append(down)
         article[na_art[8]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[8]][3]=article[na_art[8]][1]*article[na_art[8]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[20]) in txt:
         article[na_art[20]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[20])
         down=130+13*m
         coord.append(down)
         article[na_art[20]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[20]][3]=article[na_art[20]][1]*article[na_art[20]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[32]) in txt:
         article[na_art[32]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[32])
         down=130+13*m
         coord.append(down)
         article[na_art[32]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[32]][3]=article[na_art[32]][1]*article[na_art[32]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 10
def f13():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[9]) in txt:
         article[na_art[9]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[9])
         down=130+13*m
         coord.append(down)
         article[na_art[9]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[9]][3]=article[na_art[9]][1]*article[na_art[9]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[21]) in txt:
         article[na_art[21]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[21])
         down=130+13*m
         coord.append(down)
         article[na_art[21]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[21]][3]=article[na_art[21]][1]*article[na_art[21]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[33]) in txt:
         article[na_art[33]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[33])
         down=130+13*m
         coord.append(down)
         article[na_art[33]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[33]][3]=article[na_art[33]][1]*article[na_art[33]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 11
def f14():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[10]) in txt:
         article[na_art[10]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[10])
         down=130+13*m
         coord.append(down)
         article[na_art[10]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[10]][3]=article[na_art[10]][1]*article[na_art[10]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[22]) in txt:
         article[na_art[22]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[22])
         down=130+13*m
         coord.append(down)
         article[na_art[22]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[22]][3]=article[na_art[22]][1]*article[na_art[22]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[34]) in txt:
         article[na_art[34]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[34])
         down=130+13*m
         coord.append(down)
         article[na_art[34]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[34]][3]=article[na_art[34]][1]*article[na_art[34]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton 12
def f15():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Si le menu Repas est actif
   if men==0:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[11]) in txt:
         article[na_art[11]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[11])
         down=130+13*m
         coord.append(down)
         article[na_art[11]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[11]][3]=article[na_art[11]][1]*article[na_art[11]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Si le menu Boisson est actif
   elif men==1:
      #Si le texte est déjà présent alors rajouter 1 au nombre d'article
      if str(na_art[23]) in txt:
         article[na_art[23]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[23])
         down=130+13*m
         coord.append(down)
         article[na_art[23]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[23]][3]=article[na_art[23]][1]*article[na_art[23]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   elif men==2:
      if str(na_art[35]) in txt:
         article[na_art[35]][2]+=1
      #Sinon rajouter l'article dans la liste txt et de nouvelle coordonnées associé à celui-ci
      else:
         txt.append(na_art[35])
         down=130+13*m
         coord.append(down)
         article[na_art[35]][2]+=1
         m+=1
      #Recréation du canvas pour l'actualiser
      can=tk.Canvas(Caisse, width=478, height=256, bg="white")
      #Calcul du coût pour le produit en question
      article[na_art[35]][3]=article[na_art[35]][1]*article[na_art[35]][2]
      #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
      #les anciennes valeurs et articles)
      for i in range(0,5):
         text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
      for i in range(5,len(txt)):
         text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
      #Affichage du canvas
      can.pack()
      #Disposition du canvas dans la grille
      can.grid(row=0,column=3,rowspan=2,columnspan=4)
      #Réactualisation de la barre de défilement
      scrollbar=tk.Scrollbar(Caisse)
      scrollbar.config(command=can.yview,width=530)
      scrollbar.set(170+13*m,0)
      scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

##Fonction du bouton Total
def f16():
   #Récupération de la variable m et Caisse
   global m, Caisse
   #Déclaration de la variable somme
   somme=0
   #Positionnement du texte
   down=150+13*m
   #Recréation du canvas pour l'actualiser
   can=tk.Canvas(Caisse, width=478, height=256, bg="white")
   #Recréation du texte du canvas en ajoutant le nouvelle article (sauf si déjà présent donc supperposition du nouveau canvas sur l'ancien afin de cacher
   #les anciennes valeurs et articles)
   for i in range(0,5):
      text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
   for i in range(5,len(txt)):
      text=can.create_text(245,coord[i+1],text=str(int(article[txt[i]][2]))+" X "+str(txt[i])+"   "+str(article[txt[i]][3])+" €")
   #Calcule de la somme total de l'ensemble des articles
   for i in article:
      somme+=article[i][2]*article[i][1]
   #Création du texte pour l'affichage du total
   text=can.create_text(245,down-15,text="-------------------------------------")
   text=can.create_text(245,down,font=helv10,text="Total"+" "*30+str(somme)+" €")
   #Affichage du canvas
   can.pack()
   #Disposition du canvas dans la grille
   can.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Réactualisation de la barre de défilement
   scrollbar=tk.Scrollbar(Caisse)
   scrollbar.config(command=can.yview,width=530)
   scrollbar.set(170+13*m,0)
   scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Enregistrement en appellant la fonction f17()
   f17()

#Fonction du bouton Enregistrer
def f17():
   #Récupération de la variable ann
   global ann
   #Déclaration de la variable somme
   somme=0
   #Ajout de 1 à la valeur de la variable ann
   ann+=1
   #Importation de la date
   date=time.localtime()
   #Création du fichier texte (du ticket de caisse)
   f=open(str(time.strftime("Transaction\Toutes les transactions\Transaction n ",date)+str(ann)),"w")
   f.write(time.strftime("Transaction effectué le %d.%m.%Y à %Hh%Mm%Ss n ",date)+str(ann))
   for i in range(0,5):
      f.write(str(txt[i]+"\n"))
   for i in range(5,len(txt)):
      f.write(str(txt[i])+"   "+str(article[txt[i]][3])+" €\n")
   for i in article:
      somme+=article[i][2]*article[i][1]
   f.write("-------------------------------------\n")
   f.write("Total"+" "*30+str(somme)+" €")
   f.close()

#Fonction du bouton Annuler
def f19():
   #Récupération de la variable txt, coord, m
   global txt, coord, m
   #Recréation du canvas pour l'actualiser
   can=tk.Canvas(Caisse, width=478, height=256, bg="white")
   #Remise à 0 de toutes les valeurs entrez
   for i in article:
      article[i][2]=0
      article[i][3]=0
   m,men,down=0,0,0
   txt,coord=["Nom de l'entreprise ou de l'associtation","Slogan","Numéro de téléphone","mail","-------------------------------------------"],[245,20,50,70,90,110]
   for i in range(0,5):
      text=can.create_text(coord[0],coord[i+1],text=str(txt[i]))
   #Affichage du canvas
   can.pack()
   #Disposition du canvas dans la grille
   can.grid(row=0,column=3,rowspan=2,columnspan=4)
   #Réactualisation de la barre de défilement
   scrollbar=tk.Scrollbar(Caisse)
   scrollbar.config(command=can.yview,width=530)
   scrollbar.set(170+13*m,0)
   scrollbar.grid(row=0,column=3,rowspan=2,columnspan=4)

#Fonction du bouton Paramètre
def f20():
   #Récupération de la variable e
   global e
   page1=tk.Tk()
   page1.geometry("570x385")
   def f22():
      #Récupération de la variable e
      global e
      #Vérification des prix
      try:
         if lab4.get()!="":
             na_art[0]=lab4.get()
         if lab5.get()!="":
             na_art[1]=lab5.get()
         if lab6.get()!="":
             na_art[2]=lab6.get()
         if lab7.get()!="":
             na_art[3]=lab7.get()
         if lab8.get()!="":
             na_art[4]=lab8.get()
         if lab9.get()!="":
             na_art[5]=lab9.get()
         if lab10.get()!="":
             na_art[6]=lab10.get()
         if lab11.get()!="":
             na_art[7]=lab11.get()
         if lab12.get()!="":
             na_art[8]=lab12.get()
         if lab13.get()!="":
             na_art[9]=lab13.get()
         if lab14.get()!="":
             na_art[10]=lab14.get()
         if lab15.get()!="":
             na_art[11]=lab15.get()
         factu()
         print("good work Repas")
      except:
         print("bad work Repas")
      try:
         if lab18.get()!="":
             na_art[12]=lab18.get()
         if lab19.get()!="":
             na_art[13]=lab19.get()
         if lab20.get()!="":
             na_art[14]=lab20.get()
         if lab21.get()!="":
             na_art[15]=lab21.get()
         if lab22.get()!="":
             na_art[16]=lab22.get()
         if lab23.get()!="":
             na_art[17]=lab23.get()
         if lab24.get()!="":
             na_art[18]=lab24.get()
         if lab25.get()!="":
             na_art[19]=lab25.get()
         if lab26.get()!="":
             na_art[20]=lab26.get()
         if lab27.get()!="":
             na_art[21]=lab27.get()
         if lab28.get()!="":
             na_art[22]=lab28.get()
         if lab29.get()!="":
             na_art[23]=lab29.get()
         factu()
         print("good work Dessert")
      except:
         print("bad work Dessert")
      try:
         if lab32.get()!="":
             na_art[24]=lab32.get()
         if lab33.get()!="":
             na_art[25]=lab33.get()
         if lab34.get()!="":
             na_art[26]=lab34.get()
         if lab35.get()!="":
             na_art[27]=lab35.get()
         if lab36.get()!="":
             na_art[28]=lab36.get()
         if lab37.get()!="":
             na_art[29]=lab37.get()
         if lab38.get()!="":
             na_art[30]=lab38.get()
         if lab39.get()!="":
             na_art[31]=lab39.get()
         if lab40.get()!="":
             na_art[32]=lab40.get()
         if lab41.get()!="":
             na_art[33]=lab41.get()
         if lab42.get()!="":
             na_art[34]=lab42.get()
         if lab43.get()!="":
             na_art[35]=lab43.get()
         factu()
         print("good work Boisson")
      except:
         print("bad work Boisson")
      #Mise à jour des prix
      article[na_art[0]][1]=float(prix0.get())
      article[na_art[1]][1]=float(prix1.get())
      article[na_art[2]][1]=float(prix2.get())
      article[na_art[3]][1]=float(prix3.get())
      article[na_art[4]][1]=float(prix4.get())
      article[na_art[5]][1]=float(prix5.get())
      article[na_art[6]][1]=float(prix6.get())
      article[na_art[7]][1]=float(prix7.get())
      article[na_art[8]][1]=float(prix8.get())
      article[na_art[9]][1]=float(prix9.get())
      article[na_art[10]][1]=float(prix10.get())
      article[na_art[11]][1]=float(prix11.get())
      article[na_art[12]][1]=float(prix12.get())
      article[na_art[13]][1]=float(prix13.get())
      article[na_art[14]][1]=float(prix14.get())
      article[na_art[15]][1]=float(prix15.get())
      article[na_art[16]][1]=float(prix16.get())
      article[na_art[17]][1]=float(prix17.get())
      article[na_art[18]][1]=float(prix18.get())
      article[na_art[19]][1]=float(prix19.get())
      article[na_art[20]][1]=float(prix20.get())
      article[na_art[21]][1]=float(prix21.get())
      article[na_art[22]][1]=float(prix22.get())
      article[na_art[23]][1]=float(prix23.get())
      article[na_art[24]][1]=float(prix24.get())
      article[na_art[25]][1]=float(prix25.get())
      article[na_art[26]][1]=float(prix26.get())
      article[na_art[27]][1]=float(prix27.get())
      article[na_art[28]][1]=float(prix28.get())
      article[na_art[29]][1]=float(prix29.get())
      article[na_art[30]][1]=float(prix30.get())
      article[na_art[31]][1]=float(prix31.get())
      article[na_art[32]][1]=float(prix32.get())
      article[na_art[33]][1]=float(prix33.get())
      article[na_art[34]][1]=float(prix34.get())
      article[na_art[35]][1]=float(prix35.get())
   #Déclaration des variables des entrées des paramétres
   art0=tk.StringVar(page1,value=na_art[0])
   art1=tk.StringVar(page1,value=na_art[1])
   art2=tk.StringVar(page1,value=na_art[2])
   art3=tk.StringVar(page1,value=na_art[3])
   art4=tk.StringVar(page1,value=na_art[4])
   art5=tk.StringVar(page1,value=na_art[5])
   art6=tk.StringVar(page1,value=na_art[6])
   art7=tk.StringVar(page1,value=na_art[7])
   art8=tk.StringVar(page1,value=na_art[8])
   art9=tk.StringVar(page1,value=na_art[9])
   art10=tk.StringVar(page1,value=na_art[10])
   art11=tk.StringVar(page1,value=na_art[11])
   art12=tk.StringVar(page1,value=na_art[12])
   art13=tk.StringVar(page1,value=na_art[13])
   art14=tk.StringVar(page1,value=na_art[14])
   art15=tk.StringVar(page1,value=na_art[15])
   art16=tk.StringVar(page1,value=na_art[16])
   art17=tk.StringVar(page1,value=na_art[17])
   art18=tk.StringVar(page1,value=na_art[18])
   art19=tk.StringVar(page1,value=na_art[19])
   art20=tk.StringVar(page1,value=na_art[20])
   art21=tk.StringVar(page1,value=na_art[21])
   art22=tk.StringVar(page1,value=na_art[22])
   art23=tk.StringVar(page1,value=na_art[23])
   art24=tk.StringVar(page1,value=na_art[24])
   art25=tk.StringVar(page1,value=na_art[25])
   art26=tk.StringVar(page1,value=na_art[26])
   art27=tk.StringVar(page1,value=na_art[27])
   art28=tk.StringVar(page1,value=na_art[28])
   art29=tk.StringVar(page1,value=na_art[29])
   art30=tk.StringVar(page1,value=na_art[30])
   art31=tk.StringVar(page1,value=na_art[31])
   art32=tk.StringVar(page1,value=na_art[32])
   art33=tk.StringVar(page1,value=na_art[33])
   art34=tk.StringVar(page1,value=na_art[34])
   art35=tk.StringVar(page1,value=na_art[35])
   #Déclaration des entrées de textes
   artp0=tk.StringVar(page1,value=article[na_art[0]][1])
   artp1=tk.StringVar(page1,value=article[na_art[1]][1])
   artp2=tk.StringVar(page1,value=article[na_art[2]][1])
   artp3=tk.StringVar(page1,value=article[na_art[3]][1])
   artp4=tk.StringVar(page1,value=article[na_art[4]][1])
   artp5=tk.StringVar(page1,value=article[na_art[5]][1])
   artp6=tk.StringVar(page1,value=article[na_art[6]][1])
   artp7=tk.StringVar(page1,value=article[na_art[7]][1])
   artp8=tk.StringVar(page1,value=article[na_art[8]][1])
   artp9=tk.StringVar(page1,value=article[na_art[9]][1])
   artp10=tk.StringVar(page1,value=article[na_art[10]][1])
   artp11=tk.StringVar(page1,value=article[na_art[11]][1])
   artp12=tk.StringVar(page1,value=article[na_art[12]][1])
   artp13=tk.StringVar(page1,value=article[na_art[13]][1])
   artp14=tk.StringVar(page1,value=article[na_art[14]][1])
   artp15=tk.StringVar(page1,value=article[na_art[15]][1])
   artp16=tk.StringVar(page1,value=article[na_art[16]][1])
   artp17=tk.StringVar(page1,value=article[na_art[17]][1])
   artp18=tk.StringVar(page1,value=article[na_art[18]][1])
   artp19=tk.StringVar(page1,value=article[na_art[19]][1])
   artp20=tk.StringVar(page1,value=article[na_art[20]][1])
   artp21=tk.StringVar(page1,value=article[na_art[21]][1])
   artp22=tk.StringVar(page1,value=article[na_art[22]][1])
   artp23=tk.StringVar(page1,value=article[na_art[23]][1])
   artp24=tk.StringVar(page1,value=article[na_art[24]][1])
   artp25=tk.StringVar(page1,value=article[na_art[25]][1])
   artp26=tk.StringVar(page1,value=article[na_art[26]][1])
   artp27=tk.StringVar(page1,value=article[na_art[27]][1])
   artp28=tk.StringVar(page1,value=article[na_art[28]][1])
   artp29=tk.StringVar(page1,value=article[na_art[29]][1])
   artp30=tk.StringVar(page1,value=article[na_art[30]][1])
   artp31=tk.StringVar(page1,value=article[na_art[31]][1])
   artp32=tk.StringVar(page1,value=article[na_art[32]][1])
   artp33=tk.StringVar(page1,value=article[na_art[33]][1])
   artp34=tk.StringVar(page1,value=article[na_art[34]][1])
   artp35=tk.StringVar(page1,value=article[na_art[35]][1])
   lab1=tk.Label(page1,height=2,font=helv15,text="Paramétrage des produits")
   lab2=tk.Label(page1,height=1,font=helv10,text="Nom du Repas")
   lab3=tk.Label(page1,height=1,font=helv10,text="Prix")
   lab4=tk.Entry(page1,width=15,font=helv10,textvariable=art0)
   lab5=tk.Entry(page1,width=15,font=helv10,textvariable=art1)
   lab6=tk.Entry(page1,width=15,font=helv10,textvariable=art2)
   lab7=tk.Entry(page1,width=15,font=helv10,textvariable=art3)
   lab8=tk.Entry(page1,width=15,font=helv10,textvariable=art4)
   lab9=tk.Entry(page1,width=15,font=helv10,textvariable=art5)
   lab10=tk.Entry(page1,width=15,font=helv10,textvariable=art6)
   lab11=tk.Entry(page1,width=15,font=helv10,textvariable=art7)
   lab12=tk.Entry(page1,width=15,font=helv10,textvariable=art8)
   lab13=tk.Entry(page1,width=15,font=helv10,textvariable=art9)
   lab14=tk.Entry(page1,width=15,font=helv10,textvariable=art10)
   lab15=tk.Entry(page1,width=15,font=helv10,textvariable=art11)
   lab16=tk.Label(page1,height=1,font=helv10,text="Nom du Dessert")
   lab17=tk.Label(page1,height=1,font=helv10,text="Prix")
   lab18=tk.Entry(page1,width=15,font=helv10,textvariable=art12)
   lab19=tk.Entry(page1,width=15,font=helv10,textvariable=art13)
   lab20=tk.Entry(page1,width=15,font=helv10,textvariable=art14)
   lab21=tk.Entry(page1,width=15,font=helv10,textvariable=art15)
   lab22=tk.Entry(page1,width=15,font=helv10,textvariable=art16)
   lab23=tk.Entry(page1,width=15,font=helv10,textvariable=art17)
   lab24=tk.Entry(page1,width=15,font=helv10,textvariable=art18)
   lab25=tk.Entry(page1,width=15,font=helv10,textvariable=art19)
   lab26=tk.Entry(page1,width=15,font=helv10,textvariable=art20)
   lab27=tk.Entry(page1,width=15,font=helv10,textvariable=art21)
   lab28=tk.Entry(page1,width=15,font=helv10,textvariable=art22)
   lab29=tk.Entry(page1,width=15,font=helv10,textvariable=art23)
   lab30=tk.Label(page1,height=1,font=helv10,text="Nom de la Boisson")
   lab31=tk.Label(page1,height=1,font=helv10,text="Prix")
   lab32=tk.Entry(page1,width=15,font=helv10,textvariable=art24)
   lab33=tk.Entry(page1,width=15,font=helv10,textvariable=art25)
   lab34=tk.Entry(page1,width=15,font=helv10,textvariable=art26)
   lab35=tk.Entry(page1,width=15,font=helv10,textvariable=art27)
   lab36=tk.Entry(page1,width=15,font=helv10,textvariable=art28)
   lab37=tk.Entry(page1,width=15,font=helv10,textvariable=art29)
   lab38=tk.Entry(page1,width=15,font=helv10,textvariable=art30)
   lab39=tk.Entry(page1,width=15,font=helv10,textvariable=art31)
   lab40=tk.Entry(page1,width=15,font=helv10,textvariable=art32)
   lab41=tk.Entry(page1,width=15,font=helv10,textvariable=art33)
   lab42=tk.Entry(page1,width=15,font=helv10,textvariable=art34)
   lab43=tk.Entry(page1,width=15,font=helv10,textvariable=art35)
   prix0=tk.Entry(page1,width=5,font=helv10,textvariable=artp0)
   prix1=tk.Entry(page1,width=5,font=helv10,textvariable=artp1)
   prix2=tk.Entry(page1,width=5,font=helv10,textvariable=artp2)
   prix3=tk.Entry(page1,width=5,font=helv10,textvariable=artp3)
   prix4=tk.Entry(page1,width=5,font=helv10,textvariable=artp4)
   prix5=tk.Entry(page1,width=5,font=helv10,textvariable=artp5)
   prix6=tk.Entry(page1,width=5,font=helv10,textvariable=artp6)
   prix7=tk.Entry(page1,width=5,font=helv10,textvariable=artp7)
   prix8=tk.Entry(page1,width=5,font=helv10,textvariable=artp8)
   prix9=tk.Entry(page1,width=5,font=helv10,textvariable=artp9)
   prix10=tk.Entry(page1,width=5,font=helv10,textvariable=artp10)
   prix11=tk.Entry(page1,width=5,font=helv10,textvariable=artp11)
   prix12=tk.Entry(page1,width=5,font=helv10,textvariable=artp12)
   prix13=tk.Entry(page1,width=5,font=helv10,textvariable=artp13)
   prix14=tk.Entry(page1,width=5,font=helv10,textvariable=artp14)
   prix15=tk.Entry(page1,width=5,font=helv10,textvariable=artp15)
   prix16=tk.Entry(page1,width=5,font=helv10,textvariable=artp16)
   prix17=tk.Entry(page1,width=5,font=helv10,textvariable=artp17)
   prix18=tk.Entry(page1,width=5,font=helv10,textvariable=artp18)
   prix19=tk.Entry(page1,width=5,font=helv10,textvariable=artp19)
   prix20=tk.Entry(page1,width=5,font=helv10,textvariable=artp20)
   prix21=tk.Entry(page1,width=5,font=helv10,textvariable=artp21)
   prix22=tk.Entry(page1,width=5,font=helv10,textvariable=artp22)
   prix23=tk.Entry(page1,width=5,font=helv10,textvariable=artp23)
   prix24=tk.Entry(page1,width=5,font=helv10,textvariable=artp24)
   prix25=tk.Entry(page1,width=5,font=helv10,textvariable=artp25)
   prix26=tk.Entry(page1,width=5,font=helv10,textvariable=artp26)
   prix27=tk.Entry(page1,width=5,font=helv10,textvariable=artp27)
   prix28=tk.Entry(page1,width=5,font=helv10,textvariable=artp28)
   prix29=tk.Entry(page1,width=5,font=helv10,textvariable=artp29)
   prix30=tk.Entry(page1,width=5,font=helv10,textvariable=artp30)
   prix31=tk.Entry(page1,width=5,font=helv10,textvariable=artp31)
   prix32=tk.Entry(page1,width=5,font=helv10,textvariable=artp32)
   prix33=tk.Entry(page1,width=5,font=helv10,textvariable=artp33)
   prix34=tk.Entry(page1,width=5,font=helv10,textvariable=artp34)
   prix35=tk.Entry(page1,width=5,font=helv10,textvariable=artp35)
   butapp=tk.Button(page1,text="Appliquer",bg="white",overrelief="raised",borderwidth=4,font=helv15,command=f22)
   butapp.config(height=0,width=61)
   #Positionnement dans la grille
   lab1.grid(row=0,column=0,columnspan=6)
   lab2.grid(row=1,column=0)
   lab3.grid(row=1,column=1)
   lab4.grid(row=2,column=0)
   lab5.grid(row=3,column=0)
   lab6.grid(row=4,column=0)
   lab7.grid(row=5,column=0)
   lab8.grid(row=6,column=0)
   lab9.grid(row=7,column=0)
   lab10.grid(row=8,column=0)
   lab11.grid(row=9,column=0)
   lab12.grid(row=10,column=0)
   lab13.grid(row=11,column=0)
   lab14.grid(row=12,column=0)
   lab15.grid(row=13,column=0)
   lab16.grid(row=1,column=2)
   lab17.grid(row=1,column=3)
   lab18.grid(row=2,column=2)
   lab19.grid(row=3,column=2)
   lab20.grid(row=4,column=2)
   lab21.grid(row=5,column=2)
   lab22.grid(row=6,column=2)
   lab23.grid(row=7,column=2)
   lab24.grid(row=8,column=2)
   lab25.grid(row=9,column=2)
   lab26.grid(row=10,column=2)
   lab27.grid(row=11,column=2)
   lab28.grid(row=12,column=2)
   lab29.grid(row=13,column=2)
   lab30.grid(row=1,column=4)
   lab31.grid(row=1,column=5)
   lab32.grid(row=2,column=4)
   lab33.grid(row=3,column=4)
   lab34.grid(row=4,column=4)
   lab35.grid(row=5,column=4)
   lab36.grid(row=6,column=4)
   lab37.grid(row=7,column=4)
   lab38.grid(row=8,column=4)
   lab39.grid(row=9,column=4)
   lab40.grid(row=10,column=4)
   lab41.grid(row=11,column=4)
   lab42.grid(row=12,column=4)
   lab43.grid(row=13,column=4)
   prix0.grid(row=2,column=1)
   prix1.grid(row=3,column=1)
   prix2.grid(row=4,column=1)
   prix3.grid(row=5,column=1)
   prix4.grid(row=6,column=1)
   prix5.grid(row=7,column=1)
   prix6.grid(row=8,column=1)
   prix7.grid(row=9,column=1)
   prix8.grid(row=10,column=1)
   prix9.grid(row=11,column=1)
   prix10.grid(row=12,column=1)
   prix11.grid(row=13,column=1)
   prix12.grid(row=2,column=3)
   prix13.grid(row=3,column=3)
   prix14.grid(row=4,column=3)
   prix15.grid(row=5,column=3)
   prix16.grid(row=6,column=3)
   prix17.grid(row=7,column=3)
   prix18.grid(row=8,column=3)
   prix19.grid(row=9,column=3)
   prix20.grid(row=10,column=3)
   prix21.grid(row=11,column=3)
   prix22.grid(row=12,column=3)
   prix23.grid(row=13,column=3)
   prix24.grid(row=2,column=5)
   prix25.grid(row=3,column=5)
   prix26.grid(row=4,column=5)
   prix27.grid(row=5,column=5)
   prix28.grid(row=6,column=5)
   prix29.grid(row=7,column=5)
   prix30.grid(row=8,column=5)
   prix31.grid(row=9,column=5)
   prix32.grid(row=10,column=5)
   prix33.grid(row=11,column=5)
   prix34.grid(row=12,column=5)
   prix35.grid(row=13,column=5)
   butapp.grid(row=14,column=0,columnspan=6)
   page1.mainloop()

#Fonction du bouton Aide
def f21():
   page=tk.Tk()
   page.geometry("400x400")
   labe1=tk.Label(page,height=6,font=helv15,text="Dévelloppeur du logiciel de la caisse enregistreuse :")
   labe2=tk.Label(page,height=3,font=helv10,text="Quentin Mellard et Ethan Fuchs")
   labe3=tk.Label(page,height=3,font=helv10,text="06/01/2019")
   labe4=tk.Label(page,height=3,wraplength=400,text="Programme réaliser dans le cadre du projet de la spécialité ISN durant l'année scolaire 2018-2019 et durant notre cursus de Terminal.")
   labe5=tk.Label(page,height=3,wraplength=400,text="Le programme est rémunérer grâce à différent don fait par les utilisateurs.")
   labe1.pack()
   labe2.pack()
   labe3.pack()
   labe4.pack()
   labe5.pack()
   page.mainloop()

def vérification():
    global m, Caisse, mdp
    texte=str(var_saisie.get())
    if texte=="QEsaint-antoine2019":
        mdp=True
        Caisse_enregistreuse.destroy()
        affichage()
    else:
        ligne_texte_eds=tk.Label(Caisse_enregistreuse,text="Mot de passe incorect")
        ligne_texte_eds.pack(padx=200,pady=150)

#Début caisse
Caisse_enregistreuse=tk.Tk()
Caisse_enregistreuse.geometry("1366x768")
Caisse_enregistreuse.title("Caisse enregistreuse")
Caisse_enregistreuse["bg"]="cyan"
ligne_texte_mdp=tk.Label(Caisse_enregistreuse,text="Entrez le mot de passe")
var_saisie=tk.StringVar()
ligne_saisie=tk.Entry(Caisse_enregistreuse, textvariable = var_saisie, width=50)
Bouton_valider=tk.Button(Caisse_enregistreuse,text="Valider", command=vérification)
fermer=tk.Button(Caisse_enregistreuse,text="Fermer",overrelief="raised",borderwidth=2,command=Caisse_enregistreuse.destroy)
ligne_texte_mdp.pack(padx=300,pady=50)
ligne_saisie.pack()
Bouton_valider.pack(padx=200, pady=115)
fermer.pack(padx=200, pady=85)
Caisse_enregistreuse.mainloop()

