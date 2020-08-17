import pygame
import random
from Constants import *

class Ball:

    def __init__ (self):
        self.x = screenLarge//2
        self.y = screenWidth//2
        

    def move(self):
        return False

    def valid(self):
        return False

    def setDirection(self, direction):
        return False

class Bricks:

    
class Paddle:

    def __init__ (self):
        self.x = screenLarge//2
        self.y = screenWidth-100

    def move(self):
        if self.direction is "Left":
            self.x -= speed
        if self.direction is "Right":
            self.x += speed
        self.isValid()
        
    def isValid(self):
        if self.x + largePaddle > screenLarge:
            self.x = screenLarge-largePaddle
        if self.x < 0:
            self.x = 0
