import pygame
import random

pygame.init()

BLUE = pygame.Color("blue")
PINK = pygame.Color("pink")
BLACK = pygame.Color("black")
YELLOW = pygame.Color("yellow")
GREEN = pygame.Color("green")
ORANGE = pygame.Color("orange")
WHITE = pygame.Color("white")
RED = pygame.Color("red")

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Controlled Sprite & Bouncing Sprite")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, is_player=False):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.is_player = is_player
        self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        if not self.is_player:
            self.rect.move_ip(self.velocity)
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.velocity[0] = -self.velocity[0]
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.velocity[1] = -self.velocity[1]

    def change_color(self):
        new_color = random.choice([YELLOW, GREEN, ORANGE, WHITE])
        self.image.fill(new_color)

def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, PINK, BLACK])

allsprites = pygame.sprite.Group()

player = Sprite(RED, 40, 30, is_player=True)
player.rect.center = (250, 200)

bouncer = Sprite(WHITE, 30, 20)
bouncer.rect.x = random.randint(0, WIDTH - 30)
bouncer.rect.y = random.randint(0, HEIGHT - 20)

allsprites.add(player, bouncer)

bg_color = BLUE
clock = pygame.time.Clock()
speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            player.change_color()
            bouncer.change_color()
            change_background_color()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player.rect.x += speed
    if keys[pygame.K_UP]:
        player.rect.y -= speed
    if keys[pygame.K_DOWN]:
        player.rect.y += speed

    player.rect.clamp_ip(screen.get_rect())
    allsprites.update()
    screen.fill(bg_color)
    allsprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
