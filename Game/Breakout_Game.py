import pygame
import random
from Constants import *
from Interactions import *
from Class_Breakout import *

class Game:

    def __init__(self):
        self.running = True
        self.end = True
        self.pause = False
        self.screen = pygame.display.set_mode((screenLarge, screenWidth))
        self.points = 0
        self.score = 0
        self.ball = Ball()
        self.paddle = Paddle()


    def simulate(self):
        pygame.time.delay(80)
        #Check if is finished 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
        #receive key
        self.key = pygame.key.get_pressed()

        #Check if is paused the game
        self.pause = isPause(self.key, self.pause)
        if self.pause is True:
            self.key = pygame.K_u
            return

        self.paddle.direction = parsingKey(self.key)
        self.paddle.move()

    def draw(self):
        #Display points obtained actually
        self.screen.fill(black)
        pygame.display.set_caption("Points = " + str(self.points))
        
        #Draw
        pygame.draw.rect(self.screen,(146, 168, 209),(self.paddle.x, self.paddle.y , largePaddle, widthPaddle))
        pygame.display.update()

    def over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = False
                return
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game over', True, (255,0,0), (0,0,0))
        textObj = text.get_rect()
        textObj.center = (screenLarge// 2, screenWidth // 2)
        self.screen.blit(text, textObj)
        pygame.display.update()