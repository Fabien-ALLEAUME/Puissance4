import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from player import Player

class Puissance():
    def __init__(self, player_1, player_2):
        self.palyer_1 = player_1
        self.player_2 = player_2
        self.grille = Grille()
        self.winner = 0


if __name__ == '__main__':
    # for setup in json.load(open("setup.json")):
	# 	frame = setup.pop("frame")
    while w == 0:
        pygame.init()
        window = pygame.display.set_mode((648,604), RESIZABLE)
        Grille()