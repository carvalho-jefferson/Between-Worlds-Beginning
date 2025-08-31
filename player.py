import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, YELLOW, screen

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = 7
        self.lives = 3
        self.score = 0
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.projectiles = []

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def shoot(self):
        proj_x = self.x + self.width // 2 - 5
        proj_y = self.y
        self.projectiles.append(pygame.Rect(proj_x, proj_y, 5, 10))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        for proj in self.projectiles:
            pygame.draw.rect(screen, YELLOW, proj)
