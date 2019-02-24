import pygame
import random
import time

# Initialization
pygame.init()

# FPS of game
FPS = 30

# How many rain drops there is
NUMBER_OF_DROPS = 600

# Screen resolution
WIGHT = 600
HEIGHT = 600

# Point list for drawing ground
point_list = [(0, HEIGHT - HEIGHT // 7),
              (WIGHT, HEIGHT - HEIGHT // 7),
              (WIGHT, HEIGHT),
              (0, HEIGHT)]

# Creating screen and setup
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption('Rain')
background = pygame.Surface(screen.get_size())

# WIND settings
WIND = 0
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

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load("pepe.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


# Rain Drops class
class Drop(object):

    def __init__(self,):
        # Initialization
        self.x: float = random.randint(0, WIGHT)
        self.y: float = random.randint(-HEIGHT, 0)
        self.y_speed: float = random.randint(3, 5)
        self.gravity: float = random.randint(0, 2)
        self.surface: int = (random.randint
                             (HEIGHT - HEIGHT // 7,
                              HEIGHT - HEIGHT // 20))
        self.thickness: int = random.randint(1, 2)
        self.splash_frames: int = 0
        self.is_splash = True

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

    def fall(self):
        # Moving drop down and increasing speed
        self.y += self.y_speed
        self.y_speed += self.gravity / 20
        self.x += WIND
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
                (self.x - WIND, self.y - self.y_speed))
        else:
            self.splash()
        if 50 < self.x < 250:
            if HEIGHT - 250 < self.y < HEIGHT:
                self.splash()

    def mouse_interaction(self):
        # Splash if touch cursor
        if mouse_x < self.x < mouse_x + 10:
                if mouse_y < self.y < mouse_y + 20:
                    self.splash()

    def splash_size(self):
        if self.is_splash:
            self.is_splash = False
            self.splash_frames = self.y_speed // 3

    def splash(self):
        self.splash_size()
        if self.splash_frames > 0:
            self.splash_frames -= 1
            for drops in range(random.randint(3, 6)):
                pygame.draw.line(
                    background,
                    (141, 190, 214),
                    (self.x, self.y),
                    (self.x - random.randint(-8 - WIND // 1.5, 8 - WIND // 1.5),
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
    start = time.time()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.display.update()

    # Process all keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if WIND > -WIND_MAX_SPD:
                    WIND -= 2
            if event.key == pygame.K_RIGHT:
                if WIND < WIND_MAX_SPD:
                    WIND += 2

    # Draw background and polygon
    background.fill((60, 132, 167))
    background = background.convert()
    pygame.draw.polygon(background, (106, 114, 113), point_list)

    # Draw pepe
    all_sprites.update()
    all_sprites.draw(background)

    # Process all drops
    for drop in all_drops:
        drop.draw()

    # Update screen
    screen.blit(background, (0, 0))

    print(f'One cpu frame {round(time.time() - start, 4)}')
    clock.tick(FPS)

