import pygame
import random
from Constants import *

class Ball:

    def __init__ (self):
        self.x = screenWidth//2
        self.y = screenHeight//2
        

    def move(self):
        return False

    def valid(self):
        return False

    def setDirection(self, direction):
        return False

class Brick(pygame.sprite.Sprite):

    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthBrick,heightBrick))
        self.image.fill((200, 100, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Paddle(pygame.sprite.Sprite):

    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((widthPaddle, heightPaddle))
        self.image.fill((146, 168, 209))
        self.rect = self.image.get_rect()
        self.rect.center = (screenWidth//2, screenHeight-100)

    def move(self):
        if self.direction is "Left":
            self.rect.x -= speed
        if self.direction is "Right":
            self.rect.x += speed
        self.isValid()
        
    def isValid(self):
        if self.rect.x + widthPaddle > screenWidth:
            self.rect.x = screenWidth-widthPaddle
        if self.rect.x < 0:
            self.rect.x = 0
