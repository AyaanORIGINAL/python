import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENTSPEED = 5
FONT_SIZE = 72

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("images.jpeg")  , (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('pink'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

spr1 = Sprite(pygame.Color('blue'), 20, 30)
spr1.rect.x, spr1.rect.y = random.randint(0, SCREEN_WIDTH - spr1.rect.width), random.randint(0, SCREEN_HEIGHT - spr1.rect.height)
all_sprites.add(spr1)

spr2 = Sprite(pygame.Color('red'), 20, 30)
spr2.rect.x, spr2.rect.y = random.randint(0, SCREEN_WIDTH - spr2.rect.width), random.randint(0, SCREEN_HEIGHT - spr2.rect.height)
all_sprites.add(spr2)

running,won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENTSPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENTSPEED
        spr1.move(x_change, y_change)

        if pygame.sprite.collide_rect(spr1, spr2):
            all_sprites.remove(spr2)
            won = True
    
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You Win!", True, pygame.Color('black'))
        screen.blit(win_text, (0.0))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()