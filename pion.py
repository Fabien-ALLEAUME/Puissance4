import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint


class Pion():
    def __init__(self, player, color, number):
        self.joueur= joueur
        self.couleur= couleur
        self.numero= numero
        if self.couleur== "RED": 
            self.image="images/pionRed.png"
        if self couleur== "YELLOW":
            self.image="images/pionYellow.png"