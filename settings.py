import pygame

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 615
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Between Worlds: Beginning")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

AUTHOR_TEXT = "Made by Jefferson | 2025"

clock = pygame.time.Clock()

# Font

font_path = "assets/fonts/Orbitron-Bold.ttf"
game_font = pygame.font.Font(font_path, 28)
title_font_large = pygame.font.Font(font_path, 48)
title_font_small = pygame.font.Font(font_path, 24)
author_font = pygame.font.Font(font_path, 10)

# Backgrounds
background1 = pygame.image.load("assets/background1.png")
background1 = pygame.transform.scale(background1, (SCREEN_WIDTH, SCREEN_HEIGHT))
background2 = pygame.image.load("assets/background2.png")
background2 = pygame.transform.scale(background2, (SCREEN_WIDTH, SCREEN_HEIGHT))
menu_background = pygame.image.load("assets/menu.png")
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Musics
menu_music = "assets/sounds/menu.mp3"
level1_music = "assets/sounds/level1.mp3"
level2_music = "assets/sounds/level2.ogg"
