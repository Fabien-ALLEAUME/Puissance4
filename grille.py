import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from player import Player


# Classe Grille contient l'affichage et l'évaluation de la grille du jeu 
class Grille():	
   def __init__(self):
	   self.n = 0
	   self.background = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
	   self.player = randint(1,2) #player who begining (yellow(jaune)=1 red(rouge)=2)
	   self.tyellow = pygame.image.load("images/tyellow.png").convert()
	   self.tred = pygame.image.load("images/tred.png").convert()
	
	def displayGrille(self):
		window.blit(pygame.image.load("images/tray.png").convert(), (0, 0))
		pygame.display.flip()
		for i in range(7):
			for y in range(6):
				if self.background[i][y] ==1:
					displayPion(i, y, self.player)
				if self.background[i][y] ==2:
					displayPion(i, y, self.player)
		
		


    # Joueur selectionne une colonne ou jouer son pion	
	# Prends en entrée la grille de jeu, renvoie la colonne selectionné si celle-ci et vide.
    def selectcol(self):
		pygame.time.Clock().tick(frame)
		res = -1
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 10 < event.pos[1] < 525:
						if 31 < event.pos[0] < 103 and notFull(0):
							res 0
						if 118 < event.pos[0] < 187 and notFull(1):
							res 1
						if 202 < event.pos[0] < 272 and notFull(2):
							res 2
						if 287 < event.pos[0] < 357 and notFull(3):
							res 3
						if 373 < event.pos[0] < 443 and notFull(4):
							res 4
						if 457 < event.pos[0] < 527 and notFull(5):
							res 5
						if 542 < event.pos[0] < 612 and notFull(6):
							res 6
                        else:
                            print("Veuillez selectionner une colonne où vous pouvez jouer")
			if event.type == KEYDOWN:
				if event.key == K_KP1 and notFull(0):
					res 0
				if event.key == K_KP2 and notFull(1):
					res 1
				if event.key == K_KP3 and notFull(2):
					res 2
				if event.key == K_KP4 and notFull(3):
					res 3
				if event.key == K_KP5 and notFull(4):
					res 4
				if event.key == K_KP6 and notFull(5):
					res 5
				if event.key == K_KP7 and notFull(6):
					res 6
                else:
                    print("Veuillez selectionner une colonne où vous pouvez jouer")
		if(res != -1):
			for i in range(6):
				if self.background[res][i] == 0:
					self.background[res][i] = self.player
					return (res, i)
		return (-1,-1)
			

        
    # Renvoie False si la colonne est pleine, True sinon
	# Prends en entrée le numéro de la colonne à vérifier
    def notFull(self, col):
        for n in range(6):
            if self.background[col][n] == 0:
                return True
        return False

	#Renvoie 0 si la grille n'a pas de ligne gagnante, 
    def checkLine(self):
		for l in range(6):
			for k in range(4):
				if self.background[k][l] == self.background[k+1][l] == self.background[k+2][l] == self.background[k+3][l] == 1:
					return [1,self.background,k,l,k+1,l,k+2,l,k+3,l]
				if self.background[k][l] == self.background[k+1][l] == self.background[k+2][l] == self.background[k+3][l] == 2:
					return [2,gself.backgroundrille,k,l,k+1,l,k+2,l,k+3,l]
			return [0]

	#Renvoie 0 si la grille n'a pas de colonne gagnante, ou renvoie le [gagnant, le background, coordonnées de pions en puissance 4]
	def checkColumn(self):
		for k in range(7):
			for l in range(3):
				if self.background[k][l] == self.background[k][l+1] == self.background[k][l+2] == self.background[k][l+3] == 1:
					return [1,self.background,k,l,k,l+1,k,l+2,k,l+3]
				if self.background[k][l] == self.background[k][l+1] == self.background[k][l+2] == self.background[k][l+3] == 2:
					return [2,self.background,k,l,k,l+1,k,l+2,k,l+3]
		return [0]
            
	#Renvoie 0 si la grille n'a pas de diagonale gagnante ayant le bas à gauche et le haut à droite, ou renvoie le [gagnant, le background, coordonnées de pions en puissance 4]
	def checkDiagonalRight(self):
		for k in range(4):
			for l in range(3):
				if self.background[k][l] == self.background[k+1][l+1] == self.background[k+2][l+2] == self.background[k+3][l+3] == 1:
					return [1,self.background,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
				if grille[k][l] == grille[k+1][l+1] == grille[k+2][l+2] == grille[k+3][l+3] == 2:
					return [2,self.background,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
		return [0]

	#Renvoie 0 si la grille n'a pas de diagonale gagnante ayant le bas à gauche et le haut à droite, ou renvoie le [gagnant, le background, coordonnées de pions en puissance 4]
	def CheckDiagonalLeft(self):
		for k in range(4):
			for l in range(3):
				if self.background[k][5-l] == self.background[k+1][4-l] == self.background[k+2][3-l] == self.background[k+3][2-l] == 1:
					return [1,self.background,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
				if self.background[k][5-l] == self.background[k+1][4-l] == self.background[k+2][3-l] == self.background[k+3][2-l] == 2:
					return [2,self.background,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
		return [0]

	#Affiche le pion placé par le joueur
	#Prend en entrée des cordonnées et la couleur du joueur qui doit placer le pion
	def displayPion(self, coord1, coord2, color):
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
	#Prends des coordonnées en entrée 
	def result(self, k1, c1, k2, c2, k3, c3, k4, c4):
		window.blit(pygame.image.load("images/tray.png").convert(), (0, 0))
		color = grille[k1][c1]
		displayPion(c1, k1, color)
		displayPion(c2, k2, color)
		displayPion(c3, k3, color)
		displayPion(c4, k4, color)
		if self.background[k1][c1] == 1:
			window.blit(pygame.image.load("images/wyellow.png").convert(), (80, 525))
		else:
			window.blit(pygame.image.load("images/wred.png").convert(), (80, 525))
		pygame.display.flip()

	#Verifie si il y a un gagnant, renvoie la couleur si oui, 0 sinon
	def isWinner(self): 
	if checkLine()[0] == 1:
		result(checkLine()[1], checkLine()[2], checkLine()[3], checkLine()[4], checkLine()[5], checkLine()[6], checkLine()[7], checkLine()[8], checkLine()[9])
		return 1
	if checkColumn()[0] == 1:
		result(checkColumn()[1], checkColumn()[2], checkColumn()[3], checkColumn()[4], checkColumn()[5], checkColumn()[6], checkColumn()[7], checkColumn()[8], checkColumn()[9])
		return 1
	if checkDiagonalRight()[0] == 1:
		result(checkDiagonalRight()[1], checkDiagonalRight()[2], checkDiagonalRight()[3], checkDiagonalRight()[4], checkDiagonalRight()[5], checkDiagonalRight()[6], checkDiagonalRight()[7], checkDiagonalRight()[8], checkDiagonalRight()[9])
		return 1
	if CheckDiagonalLeft()[0] == 1:
		result(CheckDiagonalLeft()[1], CheckDiagonalLeft()[2], CheckDiagonalLeft()[3], CheckDiagonalLeft()[4], CheckDiagonalLeft()[5], CheckDiagonalLeft()[6], CheckDiagonalLeft()[7], CheckDiagonalLeft()[8], CheckDiagonalLeft()[9])
		return 1
	if checkLine()[0] == 2:
		result(checkLine()[1], checkLine()[2], checkLine()[3], checkLine()[4], checkLine()[5], checkLine()[6], checkLine()[7], checkLine()[8], checkLine()[9])
		return 2
	if checkColumn()[0] == 2:
		result(checkColumn()[1], checkColumn()[2], checkColumn()[3], checkColumn()[4], checkColumn()[5], checkColumn()[6], checkColumn()[7], checkColumn()[8], checkColumn()[9])
		return 2
	if checkDiagonalRight()[0] == 2:
		result(checkDiagonalRight()[1], checkDiagonalRight()[2], checkDiagonalRight()[3], checkDiagonalRight()[4], checkDiagonalRight()[5], checkDiagonalRight()[6], checkDiagonalRight()[7], checkDiagonalRight()[8], checkDiagonalRight()[9])
		return 2
	if CheckDiagonalLeft()[0] == 2:
		result(CheckDiagonalLeft()[1], CheckDiagonalLeft()[2], CheckDiagonalLeft()[3], CheckDiagonalLeft()[4], CheckDiagonalLeft()[5], CheckDiagonalLeft()[6], CheckDiagonalLeft()[7], CheckDiagonalLeft()[8], CheckDiagonalLeft()[9])
		return 2
	return 0
			