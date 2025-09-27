import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
    pygame.draw.rect(screen, 'green', pygame.Rect(30,30,90,60))
    pygame.display.flip()
