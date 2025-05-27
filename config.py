from os import path

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')

WIDTH = 1200
HEIGHT = 600
FPS = 60

PATH_WIDTH = 1200
PATH_HEIGHT = 120
CAT_WIDTH = 64
CAT_HEIGHT = 64
CAR_WIDTH = 150
CAR_HEIGHT = 150
COIN_WIDTH = 50
COIN_HEIGHT = 50
LIFE_WIDTH = 75
LIFE_HEIGHT = 75
GRAVE_WIDTH = 50
GRAVE_HEIGHT = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

INIT = 0
GAME = 1
GAME_OVER = 2
QUIT = 3