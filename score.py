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

    def __str__(self):
        return self.win + " Wins - "+ self.draw + "Draws - " + self.lose + "Loses"
    
    def setWin(s):
        s.win = s.win+1

    def setDraw(d):
        s.draw = s.draw+1

    def setLose(d):
        s.lose = s.lose+1
        