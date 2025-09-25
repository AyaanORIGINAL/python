import pygame

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Adding images in Pygame")
background_image = pygame.transform.scale(pygame.image.load("pengubg.png").convert(), (SCREENWIDTH, SCREENHEIGHT))
penguin_image = pygame.transform.scale(pygame.image.load('pengu.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 30))

text = pygame.font.Font(None,36).render("hello world", True, pygame.Color("blue"))
text_rect = text.get_rect(center=(SCREENWIDTH // 2, 30))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    game_loop()
