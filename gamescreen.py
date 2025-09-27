import pygame

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

font = pygame.font.SysFont("comicsansms", 36)
text = font.render("my first ever gamescreen", True, pygame.Color("pink"))
text_rect = text.get_rect(center=(SCREENWIDTH // 2, 30))

BG_COLOR = (58, 58, 58)

lebron_image = pygame.transform.scale(
    pygame.image.load("lebron.jpeg").convert_alpha(), (300, 300)
)
lebron_rect = lebron_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        display_surface.fill(BG_COLOR)

        display_surface.blit(lebron_image, lebron_rect)

        display_surface.blit(text, text_rect)

        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
