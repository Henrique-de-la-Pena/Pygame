import pygame
from os import path
from config import *

def init_screen(window):
    clock = pygame.time.Clock()

    #background = pygame.image.load(path.join(IMG_DIR, '')).convert()
    #background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        window.fill(WHITE)
        #window.blit(background, background_rect)

        pygame.display.flip()

    return state