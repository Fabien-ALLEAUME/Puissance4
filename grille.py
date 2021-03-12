import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from pion import Pion


# Classe Grille contient l'affichage et l'évaluation de la grille du jeu 
class Grille():

    # Affiche la grille vide
   def __init__(self):
       window.blit(pygame.image.load("images/tray.png").convert(), (0, 0))
       pygame.display.flip()
       background = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
       full = 0 #0=column is not full, 1=column is full
       player = randint(1,2) #player who begining (yellow(jaune)=1 red(rouge)=2)
       tyellow = pygame.image.load("images/tyellow.png").convert()
       tred = pygame.image.load("images/tred.png").convert()


    # Affiche la grille après qu'un Joueur ait joué
    def displayGrille():


    # Joueur selectionne une colonne ou jouer son pion 
    def selectcol(grille): #player select a column for place his pion
		pygame.time.Clock().tick(frame)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 10 < event.pos[1] < 525:
						if 31 < event.pos[0] < 103 and checkColumn(grille, 0):
							return 0
						if 118 < event.pos[0] < 187 and checkColumn(grille, 1):
							return 1
						if 202 < event.pos[0] < 272 and checkColumn(grille, 2):
							return 2
						if 287 < event.pos[0] < 357 and checkColumn(grille, 3):
							return 3
						if 373 < event.pos[0] < 443 and checkColumn(grille, 4):
							return 4
						if 457 < event.pos[0] < 527 and checkColumn(grille, 5):
							return 5
						if 542 < event.pos[0] < 612 and checkColumn(grille, 6):
							return 6
                        else:
                            print("Veuillez selectionner une colonne où vous pouvez jouer")
			if event.type == KEYDOWN:
				if event.key == K_KP1 and checkColumn(grille, 0):
					return 0
				if event.key == K_KP2 and checkColumn(grille, 1):
					return 1
				if event.key == K_KP3 and checkColumn(grille, 2):
					return 2
				if event.key == K_KP4 and checkColumn(grille, 3):
					return 3
				if event.key == K_KP5 and checkColumn(grille, 4):
					return 4
				if event.key == K_KP6 and checkColumn(grille, 5):
					return 5
				if event.key == K_KP7 and checkColumn(grille, 6):
					return 6
                else:
                    print("Veuillez selectionner une colonne où vous pouvez jouer")
        
    # Renvoie False si la colonne est pleine, True sinon 
    def checkColumn(grille, col):
        for n in range(6):
            if grille[col][n] == 0:
                return True
        return False

       
            
if __name__ == '__main__':
    # for setup in json.load(open("setup.json")):
	# 	frame = setup.pop("frame")
    while w == 0:
        pygame.init()
        window = pygame.display.set_mode((648,604), RESIZABLE)
        Grille()