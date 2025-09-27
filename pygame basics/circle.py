import pygame

pygame.init()
window = pygame.display.set_mode((400, 500))
window.fill((255, 255, 255))
red = (255, 0, 0)

pygame.draw.circle(window, red , (300, 300), 50)
pygame.draw.circle(window, red , (300, 300), 50, 3)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
