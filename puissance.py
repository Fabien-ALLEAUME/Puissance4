import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint
from grille import Grille

class Puissance():
    def __init__(self, player_1, player_2):
        self.palyer_1 = player_1
        self.player_2 = player_2
        self.grille = Grille()
        self.winner = 0

    def main(self):
        self.puissance()

    def power(self):
        window.blit(pygame.image.load("images/tray.png").convert(), (0, 0))
        pygame.display.flip()
        while(self.grille.n < 42):
            displayGrille(self.grille)
            if puissance.grille.player == 1:
                window.blit(puissance.grille.tyellow, (500, 550))
                pygame.display.flip()
            else:
                window.blit(puissance.grille.tred, (500, 550))
                pygame.display.flip()
            col = -1
            line = -1
            while col == -1:
                (col, line)= selectcol(self.grille)
            displayPion(col, line, self.grille.player)
            n += 1
            if player == 1:
                player = 2
            else:
                player = 1
            if n > 6:
                self.winner = isWinner(self.grille.background)
    
    def getPlayer(self, username1, username2):
        for player in players:
            if(player.username == username1):
                self.player_1 = player
            else: 
                self.player_1.newPlayer(username1)
            if(player.username == username2):
                self.player_2 = player
            else: 
                self.player_1.newPlayer(username2)

if __name__ == '__main__':
    for setup in json.load(open("setup.json")):
        frame = setup.pop("frame")
    pygame.init()
    window = pygame.display.set_mode((648,604), RESIZABLE)
    main()
