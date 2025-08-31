import pygame
import sys
from settings import *

def main_menu():
    selected = 0
    options = ["Start", "Exit"]

    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        screen.blit(menu_background, (0, 0))

        title_text = title_font_large.render("Between Worlds", True, WHITE)
        subtitle_text = title_font_small.render("Beginning", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 120))
        screen.blit(subtitle_text, (SCREEN_WIDTH//2 - subtitle_text.get_width()//2, 180))

        for i, option in enumerate(options):
            color = YELLOW if i == selected else WHITE
            text_surface = game_font.render(option, True, color)
            screen.blit(text_surface, (SCREEN_WIDTH//2 - text_surface.get_width()//2,
                                       SCREEN_HEIGHT//2 + i*50 + 50))

        author_surface = author_font.render(AUTHOR_TEXT, True, BLACK)
        screen.blit(author_surface, (SCREEN_WIDTH//2 - author_surface.get_width()//2,
                                     SCREEN_HEIGHT - 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        pygame.mixer.music.stop()
                        return
                    elif selected == 1:
                        pygame.quit()
                        sys.exit()
