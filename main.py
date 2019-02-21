import pygame
import random
import time

# Setup
pygame.init()
fps = 60
wight = 480
height = 640
screen = pygame.display.set_mode((wight, height))
pygame.display.set_caption('Rain')
background = pygame.Surface(screen.get_size())


# Rain Drops
class Drop(object):

    __slots__ = ['x', 'y', 'y_speed', 'gravity', 'surface']

    def __init__(self, x, y, y_speed,gravity, surface):
        self.x: float = x
        self.y: float = y
        self.y_speed: float = y_speed
        self.gravity: float = gravity
        self.surface: int  = surface

    def reset(self):
        self.y = 0
        self.x = random.randint(0, wight)
        self.y_speed = random.randint(3, 10)
        self.surface = random.randint(height - height / 5, height)

    def fall(self):
        self.y += self.y_speed
        self.y_speed += self.gravity / 10
        if self.y > height:
            self.reset()

    def draw(self):
        if self.y < self.surface:
            drop.fall()
            pygame.draw.line(background,
                             (138, 43, 226),
                             (self.x, self.y),
                             (self.x, self.y + 10))
        else:
            self.reset()

    def splash(self):
        """Todo: add splash when drop hit """
        pygame.draw.aaline(background,
                            (138, 43, 226),
                            (self.x, self.y),
                            (self.x - random.randint(3, 10),
                             self.y - random.randint(3, 10)))


# Creating rain drops
all_drops = list()

for i in range(300):
    s_x = random.randint(0, wight)
    s_y = random.randint(-200, 0)
    s_speed = random.randint(3, 10)
    s_gravity = random.randint(0, 2)
    surface = random.randint(height - height / 5, height)
    obj = Drop(s_x, s_y, s_speed, s_gravity, surface)

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
    pygame.display.flip()
    print(f'One cpu frame {round(time.time() - start, 5)}')
    clock.tick(fps)

