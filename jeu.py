import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from puissance import Puissance

def main():
    username1= input("username: ")
    username2= input("username: ")
    score= Score(0,0,0)
    player_1 = Player(username1, score)
    player_2 = Player(username2, score)
    puissance= Puissance(username1, username2)
    puissance.power()

        
if __name__ == '__main__':
    for setup in json.load(open("setup.json")):
        frame = setup.pop("frame")
    pygame.init()
    window = pygame.display.set_mode((648,604), RESIZABLE)
    main()