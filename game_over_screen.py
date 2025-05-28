#Importa bibliotecas
import pygame
from os import path
from config import *
from assets import *

def game_over_screen(window, score, highscore):
    clock = pygame.time.Clock() #Tempo do jogo

    assets = load_assets() #Carrega arquivos

    #Imagem de fim de jogo
    background = pygame.image.load(path.join(IMG_DIR, 'fim_de_jogo.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Fechar a janela encerra o programa
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #Tecla Esc encerra o programa
                    state = QUIT
                    running = False
                if event.key == pygame.K_RETURN:
                    #Enter joga de novo
                    state = GAME
                    running = False
        
        window.fill(WHITE)
        window.blit(background, background_rect) #Coloca a imagem

        #Texto para jogar de novo
        try_again = assets[TEXT_FONT].render('Pressione Enter para jogar de novo', True, WHITE)
        try_again_rect = try_again.get_rect()
        try_again_rect.midbottom = (WIDTH/2, HEIGHT/2)

        #Texto de pontuação
        final_score = assets[TEXT_FONT].render('Sua pontuação foi de {} pontos'.format(score), True, BLACK)
        final_score_rect = final_score.get_rect()
        final_score_rect.midbottom = (WIDTH/2, HEIGHT - 50)

        #Texto de recorde (Por programa rodado)
        highscore_text = assets[TEXT_FONT].render('A maior pontuação é de {} pontos'.format(highscore), True, BLACK)
        highscore_text_rect = highscore_text.get_rect()
        highscore_text_rect.midbottom = (WIDTH/2, HEIGHT - 10)

        #Coloca tudo na tela
        window.blit(try_again, try_again_rect)
        window.blit(final_score, final_score_rect)
        window.blit(highscore_text, highscore_text_rect)

        pygame.display.flip()
    
    return state