import pygame
from config import *
from assets import *
from sprites import *

def game_screen(window, score, lives):
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()
    all_coins = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cars'] = all_cars
    groups['all_coins'] = all_coins


    player = Gato(groups, assets)
    all_sprites.add(player)
    
    for i in range(4):
        car = Carro(assets, i)
        all_sprites.add(car)
        all_cars.add(car)

    for i in range(3):
        coin = Rato(assets)
        all_sprites.add(coin)
        all_coins.add(coin)

    DONE = 0
    PLAYING = 1
    HIT = 2
    gameplay = PLAYING

    keys_down = {}
    ratos_vivos = 3

    while gameplay != DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                return (state, score, lives)

            if gameplay == PLAYING:
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_UP:
                        player.speedy = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 0
        
        all_sprites.update()

        if gameplay == PLAYING:

            hits = pygame.sprite.spritecollide(player, all_coins, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                ratos_vivos -= 1
                score += 10
                if ratos_vivos == 0:
                    score += 100
                    state = GAME
                    return (state, score, lives)

            hits = pygame.sprite.spritecollide(player, all_cars, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                player.kill()
                lives -= 1
                keys_down = {}
                gameplay = HIT
        
        if gameplay == HIT:
            if lives == 0:
                gameplay = DONE
            else:
                gameplay = PLAYING
                player = Gato(groups, assets)
                all_sprites.add(player)
                car = Carro(assets)
                all_sprites.add(car)
                all_cars.add(car)

    
        window.fill(WHITE)
        #window.blit(assets[BACKGROUND], (0, 0))
        window.blit(assets[GRASS_IMG], (0, 0))
        window.blit(assets[STREET_IMG], (0, 121))
        window.blit(assets[GRASS_IMG], (0, 240))
        window.blit(assets[STREET_IMG], (0, 361))
        window.blit(assets[GRASS_IMG], (0, 480))

        for i in range(7):
            window.blit(assets[GRAVE_IMG], (i*LIFE_WIDTH + (LIFE_WIDTH/5), HEIGHT - LIFE_HEIGHT + (LIFE_HEIGHT/4)))
        for i in range(lives):
            window.blit(assets[LIFE_IMG], (i*LIFE_WIDTH, HEIGHT - LIFE_HEIGHT))

        all_sprites.draw(window)

        window.blit(assets[TREES_IMG], (0, 120))
        window.blit(assets[TREES_IMG], (0, 360))

        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.update()
    state = GAME_OVER
    return (state, score, lives)