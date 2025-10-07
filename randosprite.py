import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Custom Event - Move & Change Color")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, color, movable=False):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))
        self.movable = movable
        self.speed = 5

    def change_color(self):
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        self.image.fill(self.color)

    def move(self, keys):
        if self.movable:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

sprite1 = Box(200, 200, (255, 120, 100), movable=False) 
sprite2 = Box(400, 200, (100, 160, 255), movable=True)   

all_sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    keys = pygame.key.get_pressed()
    sprite2.move(keys)

    
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
