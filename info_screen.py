#Importa bibliotecas
import pygame
from os import path
from config import *

def info_screen(window):
    clock = pygame.time.Clock() #Tempo do jogo

    #Imagem de fundo
    background = pygame.image.load(path.join(IMG_DIR, 'info.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Encerra o jogo se fechar a janela
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Tecla Esc volta para o menu
                    state = INIT
                    running = False

        window.fill(BLUE)
        window.blit(background, background_rect) #COloca fundo

        pygame.display.flip()

    return state