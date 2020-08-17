import pygame
import random
from Constants import *
from Class_Breakout import *
from Interactions import *
from Breakout_Game import *

if __name__ == '__main__':
    game = Game()
    while game.running :
        game.simulate()
        game.draw()
    while game.end:
        game.over()
