import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from score import Score

players = []

class Player():
    def __init__(self, username, score):
        self.name= username
        self.score= score

    #Prend en entrée res qui sera un string pour définir le résultat, en fonction de res actualise le score
    def changeScore(self, res):
        if res == 'Win':
            self.score.setWin()
        if res == 'Draw':
            self.score.setDraw()
        if res == 'Loose':
            self.score.setLoose()
    
    #Prend en entrée un username, crée un player et le sauvegarde dans le tableau players
    def newPlayer(self, username):
        self.name = username
        self.score= Score(0,0,0)
        players.append(player)

    
            

