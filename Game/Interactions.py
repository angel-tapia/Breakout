import pygame
from Constants import *

def parsingKey(key):
    if key[pygame.K_RIGHT]:
        return "Right"
    if key[pygame.K_LEFT]:
        return "Left"
    return "Ignore"

def isPause(key, pause):
    if key[pygame.K_p]:
        pause = not pause
    return pause