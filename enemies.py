import pygame
import random
from settings import RED, SCREEN_HEIGHT, screen

class Enemy:
    def __init__(self, x, y, speed=3):
        self.width = 60
        self.height = 60
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.projectiles = []

    def move(self):
        self.y += self.speed

    def shoot(self):
        if random.randint(1, 60) == 1:
            proj_x = self.x + self.width // 2 - 5
            proj_y = self.y + self.height
            self.projectiles.append(pygame.Rect(proj_x, proj_y, 5, 10))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        for proj in self.projectiles:
            pygame.draw.rect(screen, RED, proj)


class Enemy2:
    def __init__(self, x, y, speed=4):
        self.width = 50
        self.height = 50
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("assets/enemy2.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.projectiles = []

    def move(self):
        self.y += self.speed

    def shoot(self):
        if random.randint(1, 50) == 1:
            proj_x = self.x + self.width // 2 - 5
            proj_y = self.y + self.height
            self.projectiles.append(pygame.Rect(proj_x, proj_y, 5, 10))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        for proj in self.projectiles:
            pygame.draw.rect(screen, RED, proj)
