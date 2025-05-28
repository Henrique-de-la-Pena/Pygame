import pygame
import random
from config import *
from init_screen import init_screen
from info_screen import info_screen
from game_screen import game_screen
from game_over_screen import game_over_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Caça Rato')
score = 0
lives = 7
highscore = 0

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        gameplayed = game_screen(window, score, lives)
        state = gameplayed[0]
        score = gameplayed[1]
        lives = gameplayed[2]
    elif state == INFO:
        state = info_screen(window)
    elif state == GAME_OVER:
        if score > highscore:
            highscore = score
        state = game_over_screen(window, score, highscore)
        score = 0
        lives = 7
    else:
        state = QUIT

pygame.quit()