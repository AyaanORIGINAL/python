import pygame
import random

pygame.init()

BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")

YELLOW = pygame.Color("yellow")
MAGENTA = pygame.Color("magenta")
ORANGE = pygame.Color("orange")
WHITE = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]

    def update(self):
        self.rect.move_ip(self.velocity)
        if self.rect.left <= 0  or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            self.change_color()
            change_background_color()
        if self.rect.top <= 0  or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[1]
            self.change_color()
            change_background_color()

    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

allsprites = pygame.sprite.Group()
sp1 = Sprite(WHITE, 30, 20)
sp1.rect.x = random.randint(0, 470)
sp1.rect.y = random.randint(0, 480)
sp2 = Sprite(WHITE, 30, 20)
sp2.rect.x = random.randint(0, 470)
sp2.rect.y = random.randint(0, 480)
allsprites.add(sp1, sp2)

screen = pygame.display.set_mode((500, 400))
bg_color = BLUE
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    allsprites.update()
    screen.fill(bg_color)
    allsprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(120)
        
pygame.quit()
