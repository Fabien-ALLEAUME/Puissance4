import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint

class Score():
    def __init__(self, win, draw, lose):
        self.win = win
        self.draw = draw
        self.lose = lose

    #Ne prends rien en entrée, renvoie un string pour afficher l'historique de jeu
    def __str__(self):
        return self.win + " Wins - "+ self.draw + "Draws - " + self.lose + "Loses"
    
    #Ne prends rien en entrée, incrémente de 1 l'attribut win d'un objet Score
    def addWin(self):
        self.win = self.win+1

    #Ne prends rien en entrée, incrémente de 1 l'attribut draw d'un objet Score
    def addDraw(self):
        self.draw = self.draw+1

    #Ne prends rien en entrée, incrémente de 1 l'attribut lose d'un objet Score
    def addLose(self):
        self.lose = self.lose+1
        