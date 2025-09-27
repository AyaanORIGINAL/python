import pygame

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 480
display_surface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))


pygame.display.set_caption("My first game screen")


RECT_COLOR = (0, 104, 69)
rect_width, rect_height = 200, 100
rect = pygame.Rect(0, 0, rect_width, rect_height)
rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)

font = pygame.font.Font(None, 40)
text = font.render("Hello Pygame!", True, pygame.Color("white"))
text_rect = text.get_rect(center=(SCREENWIDTH // 2, 50))

BG_COLOR = (0, 0, 0)

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill(BG_COLOR)

        pygame.draw.rect(display_surface, RECT_COLOR, rect)

        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
