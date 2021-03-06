import pygame
import random
from time import time


def timer(func):
    def timeit(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        print(f'{func.__name__}:  {time() - before}')
        return rv
    return timeit


# Initialization
pygame.init()

# FPS of game
FPS = 30

# Playing sad music

pygame.mixer.music.load('sad.mp3')
pygame.mixer.music.play(-1)

# How many rain drops there is
NUMBER_OF_DROPS = 800

# Window resolution
WIGHT = 800
HEIGHT = 800

# Point list for drawing ground
point_list = [(0, HEIGHT - HEIGHT // 7),
              (WIGHT, HEIGHT - HEIGHT // 7),
              (WIGHT, HEIGHT),
              (0, HEIGHT)]

# Creating screen and setup
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption('Rain')
background = pygame.Surface(screen.get_size())

# WIND_X settings
WIND_X = 0
WIND_Y = 0
WIND_MAX_SPD = 20

# Mouse settings
mouse_x, mouse_y = pygame.mouse.get_pos()

# Colors
WHITE = (255, 255, 255)

# Pepe Size
PEPE_X = 350
PEPE_Y = 274


# Sprite Class
class MyDude(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load("pepe.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


# Rain Drops class
class Drop(object):

#    @timer
    def __init__(self,):
        # Initialization
        self.x: float = random.randint(0, WIGHT)
        self.y: float = random.randint(-HEIGHT, 0)
        self.y_speed: float = random.randint(3, 5)
        self.gravity: float = random.randint(0, 2)
        self.surface: int = (random.randint(HEIGHT - HEIGHT // 7, HEIGHT - HEIGHT // 20))
        self.thickness: int = random.randint(1, 2)
        self.splash_frames: int = 0
        self.is_splash = True

#    @timer
    def reset(self):
        # Moving Drop to top of screen and randomizing starting parameters
        self.x: float = random.randint(0, WIGHT)
        self.y: float = -20
        self.y_speed: float = random.randint(3, 5)
        self.surface: int = random.randint(HEIGHT - HEIGHT // 7, HEIGHT - HEIGHT // 20)
        self.gravity: float = random.randint(0, 2)
        self.thickness: int = random.randint(1, 2)
        self.splash_frames: int = 5
        self.is_splash = True

#    @timer
    def fall(self):
        # Moving drop down and increasing speed
        self.y += self.y_speed + WIND_Y
        self.y_speed += self.gravity / 20
        self.x += WIND_X
        if self.x < 0:
            self.x = WIGHT
        if self.x > WIGHT:
            self.x = 0

#    @timer
    def draw(self):
        # Draw water drop
        self.mouse_interaction()
        if self.y < self.surface:
            drop.fall()
            pygame.draw.line(
                background,
                (141, 190, 214),
                (self.x, self.y),
                (self.x - WIND_X, self.y - self.y_speed))
        else:
            self.splash()
        if 50 < self.x < 250:
            if HEIGHT - 250 < self.y < HEIGHT:
                self.splash()

#    @timer
    def mouse_interaction(self):
        # Splash if touch cursor
        if mouse_x < self.x < mouse_x + 10:
                if mouse_y < self.y < mouse_y + 20:
                    self.splash()

#    @timer
    def splash_size(self):
        if self.is_splash:
            self.is_splash = False
            self.splash_frames = self.y_speed // 3

#    @timer
    def splash(self):
        """Making splash by """
        self.splash_size()
        if self.splash_frames > 0:
            self.splash_frames -= 1
            for drops in range(random.randint(3, 6)):
                pygame.draw.line(
                    background,
                    (141, 190, 214),
                    (self.x, self.y),
                    (self.x - random.randint(-8 - WIND_X // 1.5, 8 - WIND_X // 1.5),
                     self.y - random.randint(0, int(self.y_speed)//2)))
        else:
            self.reset()


# Creating rain drops
all_drops = list()

for i in range(NUMBER_OF_DROPS):
    obj = Drop()
    all_drops.append(obj)

# List for sprites
all_sprites = pygame.sprite.Group()

# Creating pepe
pepe = MyDude(PEPE_X // 2, PEPE_Y // 2)
pepe.rect.x = 0
pepe.rect.y = HEIGHT - PEPE_Y

all_sprites.add(pepe)

# Main Game Loop
loop = True
clock = pygame.time.Clock()

while loop:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Process all keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if WIND_X > -WIND_MAX_SPD:
                    WIND_X -= 2
            if event.key == pygame.K_RIGHT:
                if WIND_X < WIND_MAX_SPD // 2:
                    WIND_X += 2
            if event.key == pygame.K_UP:
                if WIND_Y > 0:
                    WIND_Y -= 2
            if event.key == pygame.K_DOWN:
                if WIND_Y < WIND_MAX_SPD // 2:
                    WIND_Y += 2

    # Draw background and polygon
    background.fill((60, 132, 167))
    background = background.convert()
    pygame.draw.polygon(background, (106, 114, 113), point_list)
    pygame.display.update()

    # Draw pepe
    all_sprites.update()
    all_sprites.draw(background)

    # Process all drops
    for drop in all_drops:
        drop.draw()

    # Update screen
    screen.blit(background, (0, 0))
    clock.tick(FPS)

