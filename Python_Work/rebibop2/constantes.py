from random import *
import time, pygame
from pygame.locals import *
pygame.init()

#TEXTURE FOND
fond = pygame.image.load("ISNBackground.png").convert()
acceuil = pygame.image.load("acceuil.png").convert()
fond2 = pygame.image.load("background2.png").convert()
fond3 = pygame.image.load("background3.bmp").convert()
#TEXTURES DE PLATEFORMES
plats = pygame.image.load("Ptp.png").convert_alpha()
plathg = pygame.image.load("platehg.png").convert_alpha()
plathd = pygame.image.load("Pthd.png").convert_alpha()
platbd = pygame.image.load("Ptcd.png").convert_alpha()
platbg = pygame.image.load("ptbg.png").convert_alpha()
pt = pygame.image.load("pt.png").convert_alpha()
ptg = pygame.image.load("ptg.png").convert_alpha()
ptd = pygame.image.load("ptd.png").convert_alpha()
ptb = pygame.image.load("ptb.png").convert_alpha()
pierre = pygame.image.load("pierre1.png").convert_alpha()
drapeau = pygame.image.load("drapeau.png").convert_alpha()
bois = pygame.image.load("bois.png").convert_alpha()
eau = pygame.image.load("eau.png").convert_alpha()
difficulte = pygame.image.load("difficulte.png").convert_alpha()
#TEXTURES DES PERSONNAGES
perso = pygame.image.load("licorne.png").convert_alpha()
paysan = pygame.image.load("paysan.png").convert_alpha()
#TEXTURES AUTRES
bvp = pygame.image.load("life1.png").convert_alpha()
bvv = pygame.image.load("life0.png").convert_alpha()
perdu = pygame.image.load("go.png").convert_alpha()
#POLICE D'ECRITURE
font = pygame.font.Font(None, 36)
#COORDONNEES
position_perso = perso.get_rect()
x_perso = position_perso[0]
y_perso = position_perso[1]
x_perso = 50
y_perso = 390
x_paysan1, x_paysan2, x_paysan3, y_paysan1, y_paysan2, y_paysan3 = 800, 250, 1250, 260, 210, 460
#VARIABLES
touch = 0
diff = 0
chgniveau = 0
niveauactuel = 1
tsprite = 50
vie = 5
tma = 0
attack = 0
og = 0
direction = 1
ralentissement = 0
pause = 0
enviep1 = 1
enviep2 = 0
enviep3 = 0
entree = 0
test = 0    
acce = 0
sept = 0
jump = 1
plat = 0
deb = 0
continuer = 1
oui = 0
keydownl, keydownr, keydownu = 0, 0, 0
ui = 0
i = 0
vit = 0.1
gauche = 0
droite = 1
gflip = 0
rflip = 0
joue = 0
vies = 5
kickg, kickd = 0, 0
ct = 0
#TEXTES
texte = font.render(str(y_perso), 1, (255,255,255)) 
texte1 = font.render(str(x_perso), 1, (255,255,255))
texte2 = font.render(str(i), 1, (255,255,255))
texteui = font.render(str(ui), 1, (255,255,255))


