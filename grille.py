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
    def displayGrille(grille):
		


    # Joueur selectionne une colonne ou jouer son pion	
	# Prends en entrée la grille de jeu, renvoie la colonne selectionné si celle-ci et vide.
    def selectcol(grille):
		pygame.time.Clock().tick(frame)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 10 < event.pos[1] < 525:
						if 31 < event.pos[0] < 103 and notFull(grille, 0):
							return 0
						if 118 < event.pos[0] < 187 and notFull(grille, 1):
							return 1
						if 202 < event.pos[0] < 272 and notFull(grille, 2):
							return 2
						if 287 < event.pos[0] < 357 and notFull(grille, 3):
							return 3
						if 373 < event.pos[0] < 443 and notFull(grille, 4):
							return 4
						if 457 < event.pos[0] < 527 and notFull(grille, 5):
							return 5
						if 542 < event.pos[0] < 612 and notFull(grille, 6):
							return 6
                        else:
                            print("Veuillez selectionner une colonne où vous pouvez jouer")
			if event.type == KEYDOWN:
				if event.key == K_KP1 and notFull(grille, 0):
					return 0
				if event.key == K_KP2 and notFull(grille, 1):
					return 1
				if event.key == K_KP3 and notFull(grille, 2):
					return 2
				if event.key == K_KP4 and notFull(grille, 3):
					return 3
				if event.key == K_KP5 and notFull(grille, 4):
					return 4
				if event.key == K_KP6 and notFull(grille, 5):
					return 5
				if event.key == K_KP7 and notFull(grille, 6):
					return 6
                else:
                    print("Veuillez selectionner une colonne où vous pouvez jouer")
        
    # Renvoie False si la colonne est pleine, True sinon
	# Prends la grille et le numéro de la colonne à vérifier en parametre
    def notFull(grille, col):
        for n in range(6):
            if grille[col][n] == 0:
                return True
        return False

	#Renvoie 0 si la grille n'a pas de ligne gagnante, 
	#Prends la grille en paramètre
    def checkLine(grille):
		for l in range(6):
			for k in range(4):
				if grille[k][l] == grille[k+1][l] == grille[k+2][l] == grille[k+3][l] == 1:
					return [1,grille,k,l,k+1,l,k+2,l,k+3,l]
				if grille[k][l] == grille[k+1][l] == grille[k+2][l] == grille[k+3][l] == 2:
					return [2,grille,k,l,k+1,l,k+2,l,k+3,l]
			return [0]

	#Renvoie 0 si la grille n'a pas de colonne gagnante, 
	#Prends la grille en paramètre
	def checkColumn(grille):
		for k in range(7):
			for l in range(3):
				if grille[k][l] == grille[k][l+1] == grille[k][l+2] == grille[k][l+3] == 1:
					return [1,grille,k,l,k,l+1,k,l+2,k,l+3]
				if grille[k][l] == grille[k][l+1] == grille[k][l+2] == grille[k][l+3] == 2:
					return [2,grille,k,l,k,l+1,k,l+2,k,l+3]
		return [0]
            
	#Renvoie 0 si la grille n'a pas de diagonale gagnante ayant le bas à gauche et le haut à droite, 
	#Prends la grille en paramètre
	def checkDiagonalRight(grille):
		for k in range(4):
			for l in range(3):
				if grille[k][l] == grille[k+1][l+1] == grille[k+2][l+2] == grille[k+3][l+3] == 1:
					return [1,grille,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
				if grille[k][l] == grille[k+1][l+1] == grille[k+2][l+2] == grille[k+3][l+3] == 2:
					return [2,grille,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
		return [0]

	#Renvoie 0 si la grille n'a pas de diagonale gagnante ayant le bas à gauche et le haut à droite, 
	#Prends la grille en paramètre
	def CheckDiagonalLeft(grille):
		for k in range(4):
			for l in range(3):
				if grille[k][5-l] == grille[k+1][4-l] == grille[k+2][3-l] == grille[k+3][2-l] == 1:
					return [1,grille,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
				if grille[k][5-l] == grille[k+1][4-l] == grille[k+2][3-l] == grille[k+3][2-l] == 2:
					return [2,grille,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
		return [0]

	#Affiche le pion placé par le joueur
	#Prend en entrée des cordonnées et la couleur du joueur qui doit placer le pion
	def displayPion(coord1, coord2, color):
		pioncollin = [coord1, coord2]
		c = [440 + pioncollin[0]*-85, 28 + pioncollin[1]*85]
		if color == 1:
			piony = pygame.image.load("images/pionYellow.png").convert()
			window.blit(piony, (c[1], c[0]))
		else:
			pionr = pygame.image.load("images/pionRed.png").convert()
			window.blit(pionr, (c[1], c[0]))
		pygame.display.flip()

	#Affiche la grille avec le puissance 4 gagnant 
	#Prends la grille et des coordonnées en entrée 
	def result(grille, k1, c1, k2, c2, k3, c3, k4, c4):
		window.blit(pygame.image.load("images/tray.png").convert(), (0, 0))
		color = grille[k1][c1]
		displayPion(c1, k1, color)
		displayPion(c2, k2, color)
		displayPion(c3, k3, color)
		displayPion(c4, k4, color)
		if grille[k1][c1] == 1:
			window.blit(pygame.image.load("images/wyellow.png").convert(), (80, 525))
		else:
			window.blit(pygame.image.load("images/wred.png").convert(), (80, 525))
		pygame.display.flip()

	#Verifie si il y a un gagnant, renvoie la couleur si oui, 0 sinon 
	#Prend la grille en entrée
	def isWinner(grille): #return the player winner or 0
	if checkLine(grille)[0] == 1:
		result(checkLine(grille)[1], checkLine(grille)[2], checkLine(grille)[3], checkLine(grille)[4], checkLine(grille)[5], checkLine(grille)[6], checkLine(grille)[7], checkLine(grille)[8], checkLine(grille)[9])
		return 1
	if checkColumn(grille)[0] == 1:
		result(checkColumn(grille)[1], checkColumn(grille)[2], checkColumn(grille)[3], checkColumn(grille)[4], checkColumn(grille)[5], checkColumn(grille)[6], checkColumn(grille)[7], checkColumn(grille)[8], checkColumn(grille)[9])
		return 1
	if checkDiagonalRight(grille)[0] == 1:
		result(checkDiagonalRight(grille)[1], checkDiagonalRight(grille)[2], checkDiagonalRight(grille)[3], checkDiagonalRight(grille)[4], checkDiagonalRight(grille)[5], checkDiagonalRight(grille)[6], checkDiagonalRight(grille)[7], checkDiagonalRight(grille)[8], checkDiagonalRight(grille)[9])
		return 1
	if CheckDiagonalLeft(grille)[0] == 1:
		result(CheckDiagonalLeft(grille)[1], CheckDiagonalLeft(grille)[2], CheckDiagonalLeft(grille)[3], CheckDiagonalLeft(grille)[4], CheckDiagonalLeft(grille)[5], CheckDiagonalLeft(grille)[6], CheckDiagonalLeft(grille)[7], CheckDiagonalLeft(grille)[8], CheckDiagonalLeft(grille)[9])
		return 1
	if checkLine(grille)[0] == 2:
		result(checkLine(grille)[1], checkLine(grille)[2], checkLine(grille)[3], checkLine(grille)[4], checkLine(grille)[5], checkLine(grille)[6], checkLine(grille)[7], checkLine(grille)[8], checkLine(grille)[9])
		return 2
	if checkColumn(grille)[0] == 2:
		result(checkColumn(grille)[1], checkColumn(grille)[2], checkColumn(grille)[3], checkColumn(grille)[4], checkColumn(grille)[5], checkColumn(grille)[6], checkColumn(grille)[7], checkColumn(grille)[8], checkColumn(grille)[9])
		return 2
	if checkDiagonalRight(grille)[0] == 2:
		result(checkDiagonalRight(grille)[1], checkDiagonalRight(grille)[2], checkDiagonalRight(grille)[3], checkDiagonalRight(grille)[4], checkDiagonalRight(grille)[5], checkDiagonalRight(grille)[6], checkDiagonalRight(grille)[7], checkDiagonalRight(grille)[8], checkDiagonalRight(grille)[9])
		return 2
	if CheckDiagonalLeft(grille)[0] == 2:
		result(CheckDiagonalLeft(grille)[1], CheckDiagonalLeft(grille)[2], CheckDiagonalLeft(grille)[3], CheckDiagonalLeft(grille)[4], CheckDiagonalLeft(grille)[5], CheckDiagonalLeft(grille)[6], CheckDiagonalLeft(grille)[7], CheckDiagonalLeft(grille)[8], CheckDiagonalLeft(grille)[9])
		return 2
	return 0
			
if __name__ == '__main__':
    # for setup in json.load(open("setup.json")):
	# 	frame = setup.pop("frame")
    while w == 0:
        pygame.init()
        window = pygame.display.set_mode((648,604), RESIZABLE)
        Grille()