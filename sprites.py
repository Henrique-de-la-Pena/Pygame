import pygame
import random
from config import *
from assets import *

class Gato(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CAT_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - CAT_HEIGHT
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Carro(pygame.sprite.Sprite):
    def __init__(self, assets, i, score):
        pygame.sprite.Sprite.__init__(self)

        colour = random.randint(1, 3)
        if colour == 1:
            colour = 'r'
        elif colour == 2:
            colour = 'y'
        else:
            colour = 'b'
        
        if i % 2 == 0:
            direcao = 'e'
            posix = WIDTH
            speed = random.randint(-12 - (score//130), -8 - (score//130))
            if i == 0:
                posiy = 95 + PATH_HEIGHT
            else:
                posiy = 335 + PATH_HEIGHT
        else:
            direcao = 'd'
            posix = 0 - CAR_WIDTH
            speed = random.randint(8 + (score//130), 12 + (score//130))
            if i == 1:
                posiy = 145 + PATH_HEIGHT
            else:
                posiy = 385 + PATH_HEIGHT
        
        self.direcao = direcao
        self.image = assets[colour+direcao]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = posix
        self.rect.bottom = posiy
        self.speedx = speed

    def update(self, assets):
        self.rect.x += self.speedx
        
        colour = random.randint(1, 3)
        if colour == 1:
            colour = 'r'
        elif colour == 2:
            colour = 'y'
        else:
            colour = 'b'

        if self.direcao == 'e':
            if self.rect.right < 0:
                self.image = assets[colour+self.direcao]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.x = WIDTH
        else:
            if self.rect.left > WIDTH:
                self.image = assets[colour+self.direcao]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect.right = 0

class Rato(pygame.sprite.Sprite):
    def __init__(self, assets, score):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[COIN_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - COIN_WIDTH)
        self.rect.y = random.randint(0, int(HEIGHT/3))

        if score >= 130*3:
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(-3, 3)

    def update(self, score):
        if score >= 130*3:
            self.rect.x += self.speedx
            self.rect.y += self.speedy

        if self.rect.top < 0 or self.rect.bottom > HEIGHT/3 or self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(-3, 3)
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT/3:
                self.rect.bottom = HEIGHT/3
            if self.rect.left < 0:
                self.rect.left = 0
            if  self.rect.right > WIDTH:
                self.rect.right = WIDTH