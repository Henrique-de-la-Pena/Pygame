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