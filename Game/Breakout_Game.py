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
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.points = 0
        self.score = 0
        self.ball = Ball()
        self.paddle = Paddle()
        self.Paddle_list = pygame.sprite.Group()
        self.Paddle_list.add(self.paddle)
        self.Brick_list = pygame.sprite.Group()
        for i in range (0,10):
            for j in range (0,4):
                self.brick = Brick(40 + i*70, 15 + j*35)
                self.Brick_list.add(self.brick)

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
        self.Paddle_list.update()
        self.Brick_list.update()

    def draw(self):
        #Display points obtained actually
        self.screen.fill(black)
        pygame.display.set_caption("Points = " + str(self.points))
        
        #Draw
        #pygame.draw.rect(self.screen,(146, 168, 209),(self.paddle.x, self.paddle.y , widthPaddle, heightPaddle))
        self.Paddle_list.draw(self.screen)
        self.Brick_list.draw(self.screen)
        pygame.display.update()

    def over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = False
                return
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game over', True, (255, 0, 0), (0, 0, 0))
        textObj = text.get_rect()
        textObj.center = (screenWidth// 2, screenHeight // 2)
        self.screen.blit(text, textObj)
        pygame.display.update()
