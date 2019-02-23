import pygame
import random
import time

# Initialization
pygame.init()

# FPS of game
FPS = 60

# How many rain drops there is
NUMBER_OF_DROPS = 2800

# Screen resolution
WIGHT = 1280
HEIGHT = 720

# Point list for ground
point_list = [(0, HEIGHT - HEIGHT // 7),
              (WIGHT, HEIGHT - HEIGHT // 7),
              (WIGHT, HEIGHT),
              (0, HEIGHT)]

# Creating screen and setup
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption('Rain')
background = pygame.Surface(screen.get_size())

# Wind settings
wind = 0


# Rain Drops class
class Drop(object):

    __slots__ = ['x', 'y', 'y_speed', 'gravity', 'surface', 'thickness', 'splash_frames']

    def __init__(self,
                 x, y,
                 y_speed,
                 gravity,
                 surface,
                 thickness,
                 splash_frames):

        self.x: float = x
        self.y: float = y
        self.y_speed: float = y_speed
        self.gravity: float = gravity
        self.surface: int = surface
        self.thickness: int = thickness
        self.splash_frames: int = splash_frames

    def reset(self):
        # Moving Drop to top of screen and randomizing starting parameters
        self.x: float = random.randint(0, WIGHT)
        self.y: float = -20
        self.y_speed: float = random.randint(3, 5)
        self.surface: int = random.randint(HEIGHT - HEIGHT // 7, HEIGHT - HEIGHT // 20)
        self.gravity: float = random.randint(0, 2)
        self.thickness: int = random.randint(1, 2)
        self.splash_frames: int = 5

    def fall(self):
        # Moving drop down and increasing speed
        self.y += self.y_speed
        self.y_speed += self.gravity / 20
        self.x += wind
        if self.x < 0:
            self.x = WIGHT
        if self.x > WIGHT:
            self.x = 0

    def draw(self):
        # Draw water drop of
        self.mouse_interaction()
        if self.y < self.surface:
            drop.fall()
            pygame.draw.line(
                background,
                (141, 190, 214),
                (self.x, self.y),
                (self.x - wind, self.y - self.y_speed))
        else:
            self.splash()

    def mouse_interaction(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x < self.x < mouse_x + 10:
                if mouse_y < self.y < mouse_y + 20:
                    self.splash()

    def splash(self):
        if self.splash_frames > 0:
            self.splash_frames -= 1
            for drops in range(random.randint(3, 6)):
                pygame.draw.line(
                    background,
                    (141, 190, 214),
                    (self.x, self.y),
                    (self.x - random.randint(-8 - wind//2, 8 - wind),
                     self.y - random.randint(0, int(self.y_speed)//2)))
        else:
            self.reset()


# Creating rain drops
all_drops = list()

for i in range(NUMBER_OF_DROPS):
    s_x = random.randint(0, WIGHT)
    s_y = random.randint(-500, -20)
    s_speed = random.randint(3, 5)
    s_gravity = random.randint(0, 2)
    s_surface = random.randint(HEIGHT - HEIGHT // 7, HEIGHT - HEIGHT // 20)
    s_thickness = random.randint(1, 2)
    s_splash_frames = 5
    obj = Drop(s_x, s_y,
               s_speed,
               s_gravity,
               s_surface,
               s_thickness,
               s_splash_frames)
    all_drops.append(obj)


# Main Game Loop
loop = True
clock = pygame.time.Clock()

while loop:
    start = time.time()
    start_w = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wind -= 1
            if event.key == pygame.K_RIGHT:
                wind += 1
    background.fill((60, 132, 167))
    background = background.convert()
    pygame.draw.polygon(background, (106, 114, 113), point_list)

    for drop in all_drops:
        drop.draw()

    screen.blit(background, (0, 0))
    pygame.display.update()
    print(f'One cpu frame {round(time.time() - start, 5)}')
    clock.tick(FPS)

