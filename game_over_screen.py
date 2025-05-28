import pygame
from os import path
from config import *

def game_over_screen(window):
    clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'fim_de_jogo.png')).convert()
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
                    state = QUIT
                    running = False
                if event.key == pygame.K_RETURN:
                    state = GAME
                    running = False
        
        window.fill(WHITE)
        window.blit(background, background_rect)

        pygame.display.flip()
    
    return state