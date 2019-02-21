import pygame
import random
import time

# Initialization
pygame.init()

# Fps of game
FPS = 20

# Screen resolution
WIGHT = 480
HEIGHT = 640

# Creating screen and setup
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption('Rain')
background = pygame.Surface(screen.get_size())


# Rain Drops class
class Drop(object):

    __slots__ = ['x', 'y', 'y_speed', 'gravity', 'surface', 'thickness']

    def __init__(self, x, y, y_speed, gravity, surface, thickness):
        self.x: float = x
        self.y: float = y
        self.y_speed: float = y_speed
        self.gravity: float = gravity
        self.surface: int = surface
        self.thickness = thickness

    def reset(self):
        # Moving Drop to top of screen and randomizing starting parameters
        self.y = 0
        self.x = random.randint(0, WIGHT)
        self.y_speed = random.randint(3, 5)
        self.surface = random.randint(HEIGHT - HEIGHT // 7, HEIGHT - HEIGHT // 20)
        self.gravity = random.randint(0, 2)
        self.thickness = random.randint(1, 2)

    def fall(self):
        # Moving drop down and increasing speed
        self.y += self.y_speed
        self.y_speed += self.gravity / 20

    def draw(self):
        # Draw water drop of
        if self.y < self.surface:
            drop.fall()
            pygame.draw.line(background,
                                 (138, 43, 226),
                                 (self.x, self.y),
                                 (self.x, self.y + 10),)
        else:
            self.splash()
            self.reset()

    def splash(self):
        """Todo: add splash when drop hit """
        for drops in range(7):
            pygame.draw.line(background,
                                (138, 43, 226),
                                (self.x, self.y),
                                (self.x - random.randint(-8, 8),
                                 self.y - random.randint(0, 8)))


# Creating rain drops
all_drops = list()

for i in range(300):
    s_x = random.randint(0, WIGHT)
    s_y = random.randint(-200, 0)
    s_speed = random.randint(3, 5)
    s_gravity = random.randint(0, 2)
    s_surface = random.randint(HEIGHT - HEIGHT // 7, HEIGHT - HEIGHT // 20)
    s_thickness = random.randint(1, 2)
    obj = Drop(s_x, s_y, s_speed, s_gravity, s_surface, s_thickness)

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
    background.fill((230, 230, 250))
    background = background.convert()
    start = time.time()
    for drop in all_drops:
        drop.draw()
    screen.blit(background, (0, 0))
    pygame.display.update()
    print(f'One cpu frame {round(time.time() - start, 5)}')
    clock.tick(FPS)

