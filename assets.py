import pygame
import os
from config import *

BACKGROUND = 'background'
STREET_IMG = 'street'
GRASS_IMG = 'grass'
TREES_IMG = 'trees'
CAR_RD = 'rd'
CAR_YD = 'yd'
CAR_BD = 'bd'
CAR_RE = 're'
CAR_YE = 'ye'
CAR_BE = 'be'
CAT_IMG = 'cat_img'
COIN_IMG = 'coin_img'
LIFE_IMG = 'life_img'
GRAVE_IMG = 'grave_img'

SCORE_FONT = 'score_font'
TEXT_FONT = 'text_font'

MIAU_PONTO = 'ponto_snd'
MIAU_MORTE = 'morte_snd'

def load_assets():
    assets = {}
    #assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, '')).convert()
    assets[STREET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'rua.png')).convert_alpha()
    assets[STREET_IMG] = pygame.transform.scale(assets[STREET_IMG], (PATH_WIDTH, PATH_HEIGHT))
    assets[GRASS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'grama.png')).convert_alpha()
    #assets[GRASS_IMG] = pygame.transform.scale(assets[GRASS_IMG], (PATH_WIDTH, PATH_HEIGHT))
    assets[TREES_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'arvores.png')).convert_alpha()
    #assets[TREES_IMG] = pygame.transform.scale(assets[TREES_IMG], (PATH_WIDTH, PATH_HEIGHT))
    assets[CAT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'gato_sentado_frente.png')).convert_alpha()
    assets[CAT_IMG] = pygame.transform.scale(assets[CAT_IMG], (CAT_WIDTH, CAT_HEIGHT))
    assets[CAR_RD] = pygame.image.load(os.path.join(IMG_DIR, 'carro_rd.png')).convert_alpha()
    assets[CAR_RD] = pygame.transform.scale(assets[CAR_RD], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_YD] = pygame.image.load(os.path.join(IMG_DIR, 'carro_yd.png')).convert_alpha()
    assets[CAR_YD] = pygame.transform.scale(assets[CAR_YD], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_BD] = pygame.image.load(os.path.join(IMG_DIR, 'carro_bd.png')).convert_alpha()
    assets[CAR_BD] = pygame.transform.scale(assets[CAR_BD], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_RE] = pygame.image.load(os.path.join(IMG_DIR, 'carro_re.png')).convert_alpha()
    assets[CAR_RE] = pygame.transform.scale(assets[CAR_RE], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_YE] = pygame.image.load(os.path.join(IMG_DIR, 'carro_ye.png')).convert_alpha()
    assets[CAR_YE] = pygame.transform.scale(assets[CAR_YE], (CAR_WIDTH, CAR_HEIGHT))
    assets[CAR_BE] = pygame.image.load(os.path.join(IMG_DIR, 'carro_be.png')).convert_alpha()
    assets[CAR_BE] = pygame.transform.scale(assets[CAR_BE], (CAR_WIDTH, CAR_HEIGHT))
    assets[COIN_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'rato.png')).convert_alpha()
    assets[COIN_IMG] = pygame.transform.scale(assets[COIN_IMG], (COIN_WIDTH, COIN_HEIGHT))
    assets[LIFE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'gato_rosto.png')).convert_alpha()
    assets[LIFE_IMG] = pygame.transform.scale(assets[LIFE_IMG], (LIFE_WIDTH, LIFE_HEIGHT))
    assets[GRAVE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'lapide.png')).convert_alpha()
    assets[GRAVE_IMG] = pygame.transform.scale(assets[GRAVE_IMG], (GRAVE_WIDTH, GRAVE_HEIGHT))

    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    assets[TEXT_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'LuckiestGuy-Regular.ttf'), 28)
    
    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica.mp3'))
    pygame.mixer.music.set_volume(0.5)
    assets[MIAU_PONTO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pega_rato.wav'))
    assets[MIAU_MORTE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'atropelado.mp3'))

    return assets