import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from grille import Grille
from score import Score

class Player():
    def __init__(self, username, color, score):
        self.name= username
        self.color= color
        self.score= score

    def changeScore(p, res):
        if res == 'Win':
            setWin(p.score)
        if res == 'Draw':
            setDraw(p.score)
        if res == 'Loose':
            setLoose(p.score)
            

