import pygame
from os import path
from config import *

def info_screen(window):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'info.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = INIT
                    running = False

        window.fill(BLUE)
        window.blit(background, background_rect)

        pygame.display.flip()

    return state