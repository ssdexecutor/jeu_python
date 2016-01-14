import pygame
from pygame.locals import *

pygame.init()

#def pause():
#def pnj:

def alterner(l, r):
    pygame.key.set_repeat(10, 60)
    a = 1
    if a % 2 == 1:
        a = a + 1
        perso = pygame.image.load(l).convert_alpha()
        print "Droite"
    else:
        a = a + 1
        perso = pygame.image.load(r).convert_alpha()
        print "Gauche"

# declaration des variables du jeu
fenetre = pygame.display.set_mode((800, 540))
continuer = True
fond = pygame.image.load("terrain2.png").convert()
perso = pygame.image.load("face.png").convert_alpha()
perso_position = perso.get_rect()
start_fond = pygame.image.load("fond.jpg")
start_boutton = pygame.image.load("start.png")
menu = True
jeu = True

#"blittage" des surfaces
fenetre.blit(start_fond, (0,0))
fenetre.blit(start_boutton, (270,400))
pygame.display.flip() # raffriachissement des surfaces

while continuer: # boucle principale (strucutre du jeu)
    pygame.time.Clock().tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        else:
            while menu: # boucle du menu
                print "Menu"
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        menu = 0

            while jeu: # boucle du jeu
                print "Jeu"
                for event in pygame.event.get():
                    print "event"
                    if event.type == QUIT:
                        print "fin du jeu\n"
                        continuer = False

                    if event.type == KEYDOWN:
                        if event.key == K_a:
                            perso_position = perso_position.move(0, 5)
                            alterner("faceL.png", "faceR.png")

                        if event.key == K_u:
                            perso_position = perso_position.move(5, 0)

                        if event.key == K_o:
                            perso_position = perso_position.move(-5, 0)
                    
                        if event.key == K_QUOTE:
                            perso_position = perso_position.move(0, -5)

                        if event.key == K_ESCAPE:
                            #pause()
                            jeu = False
                continuer = True
#                print continuer
                pygame.key.set_repeat(10, 60)
                fenetre.blit(fond, (0,0))
                fenetre.blit(perso, perso_position)
                pygame.display.flip()

pygame.quit()