#Importa bibliotecas
import pygame
from config import *
from assets import *
from sprites import *

def game_screen(window, score, lives):
    clock = pygame.time.Clock()#Tempo do jogo

    assets = load_assets()#Carrega arquivos

    #Criação dos grupos
    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()
    all_coins = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cars'] = all_cars
    groups['all_coins'] = all_coins

    #Adicionando os sprites
    player = Gato(groups, assets)
    all_sprites.add(player)
    
    for i in range(4):
        car = Carro(assets, i, score)
        all_cars.add(car)

    for i in range(3):
        coin = Rato(assets, score)
        all_coins.add(coin)

    #Estados durante o jogo
    DONE = 0
    PLAYING = 1
    HIT = 2
    gameplay = PLAYING

    keys_down = {}
    ratos_vivos = 3

    pygame.mixer.music.play(loops=-1)#musica
    while gameplay != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT #Fechar a janela
                return (state, score, lives)

            if gameplay == PLAYING:
                if event.type == pygame.KEYDOWN: #Movimentação do personagem (andar)
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8

                if event.type == pygame.KEYUP: #Movimentação do personagem (ficar parado, parar de andar)
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_UP:
                        player.speedy = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 0
        
        #Atualiza os sprites
        all_sprites.update()
        all_cars.update(assets)
        all_coins.update(score)

        if gameplay == PLAYING:
            
            #Controle das colisões com os carros e os ratos
            hits = pygame.sprite.spritecollide(player, all_coins, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets[MIAU_PONTO].play()
                ratos_vivos -= len(hits)
                score += 10*len(hits)
                if ratos_vivos == 0:
                    score += 100
                    state = GAME
                    return (state, score, lives)

            hits = pygame.sprite.spritecollide(player, all_cars, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                assets[MIAU_MORTE].play()
                player.kill()
                lives -= 1
                keys_down = {}
                gameplay = HIT
        
        if gameplay == HIT: #Se colidiu com um carro
            if lives == 0:
                gameplay = DONE #Perdeu as 7 vidas, acabou o jogo
            else:
                #Reinicia a fase
                gameplay = PLAYING
                for car in all_cars:
                    car.kill()
                player = Gato(groups, assets)
                all_sprites.add(player)
                for i in range(4):
                    car = Carro(assets, i, score)
                    all_cars.add(car)

        #Adicionando o cenário
        window.fill(GREEN)
        window.blit(assets[GRASS_IMG], (0, 0))
        window.blit(assets[STREET_IMG], (0, 121))
        window.blit(assets[GRASS_IMG], (0, 240))
        window.blit(assets[STREET_IMG], (0, 361))
        window.blit(assets[GRASS_IMG], (0, 480))

        #Adcionando HUD do jogo
        for i in range(7):
            window.blit(assets[GRAVE_IMG], (i*LIFE_WIDTH + (LIFE_WIDTH/5), HEIGHT - LIFE_HEIGHT + (LIFE_HEIGHT/4))) #Lapides
        for i in range(lives):
            window.blit(assets[LIFE_IMG], (i*LIFE_WIDTH, HEIGHT - LIFE_HEIGHT)) #Vidas

        #Coloca sprites na tela
        all_coins.draw(window)
        all_cars.draw(window)
        all_sprites.draw(window)

        window.blit(assets[TREES_IMG], (0, 120))
        window.blit(assets[TREES_IMG], (0, 360))

        #Adicionando a pontuação
        text_score = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_score_rect = text_score.get_rect()
        text_score_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_score, text_score_rect)

        pygame.display.update()
    state = GAME_OVER
    return (state, score, lives)