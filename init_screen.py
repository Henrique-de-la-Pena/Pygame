#Importa bibliotecas
import pygame
from os import path
from config import *

def init_screen(window):
    clock = pygame.time.Clock() #Tempo do jogo

    #Imagem inicial
    background = pygame.image.load(path.join(IMG_DIR, 'init.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Fechar a janela encerra o jogo
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #Tecla Enter inicia o jogo
                    state = GAME
                    running = False
                if event.key == pygame.K_SPACE: #Tecla de espaço abre as infos
                    state = INFO
                    running = False

        window.fill(WHITE)
        window.blit(background, background_rect) #Coloca a tela na janela

        pygame.display.flip()

    return state