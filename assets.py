import pygame
import os
from config import *

BACKGROUND = 'background'
CAT_IMG = 'cat_img'
CAR_IMG = 'car_img'
COIN_IMG = 'coin_img'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, '')).convert()
    assets[CAT_IMG] = pygame.image.load(os.path.join(IMG_DIR, '')).convert_alpha()
#    assets[CAT_IMG] = pygame.transform.scale(assets[CAT_IMG], (CAT_WIDTH, CAT_HEIGHT))
    assets[CAR_IMG] = pygame.image.load(os.path.join(IMG_DIR, '')).convert_alpha()
#    assets[CAR_IMG] = pygame.transform.scale(assets[CAR_IMG], (CAR_WIDTH, CAR_HEIGHT))
    assets[COIN_IMG] = pygame.image.load(os.path.join(IMG_DIR, '')).convert_alpha()
#    assets[COIN_IMG] = pygame.transform.scale(assets[COIN_IMG], (COIN_WIDTH, COIN_HEIGHT))
    return assets