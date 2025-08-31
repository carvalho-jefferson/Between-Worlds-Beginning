import pygame
import random
import sys

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

AUTHOR_TEXT = "Made by Jefferson | 2025" # Teste

clock = pygame.time.Clock()

# Fonte
font_path = "assets/fonts/Orbitron-Bold.ttf"
game_font = pygame.font.Font(font_path, 28)
title_font_large = pygame.font.Font(font_path, 48)  # Título grande
title_font_small = pygame.font.Font(font_path, 24)  # Subtítulo pequeno
author_font = pygame.font.Font(font_path, 10)  # Teste

# backgrounds
background1 = pygame.image.load("assets/background1.png")
background1 = pygame.transform.scale(background1, (SCREEN_WIDTH, SCREEN_HEIGHT))
background2 = pygame.image.load("assets/background2.png")
background2 = pygame.transform.scale(background2, (SCREEN_WIDTH, SCREEN_HEIGHT))
menu_background = pygame.image.load("assets/menu.png")
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# musics
menu_music = "assets/sounds/menu.mp3"
level1_music = "assets/sounds/level1.mp3"
level2_music = "assets/sounds/level2.ogg"

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


def main_menu():
    selected = 0  # 0 = Start, 1 = Exit
    options = ["Start", "Exit"]

    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)  # loop

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

        author_surface = author_font.render(AUTHOR_TEXT, True, BLACK) # Teste
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

def game_over_screen(score):
    pygame.mixer.music.stop()
    screen.fill(BLACK)
    game_over_text = game_font.render(f"Game Over! Score: {score}", True, WHITE)
    info_text = game_font.render("Press ENTER", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                 SCREEN_HEIGHT // 2))
    screen.blit(info_text, (SCREEN_WIDTH // 2 - info_text.get_width() // 2,
                            SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def run_game():
    player = Player()
    enemies = []
    enemy_spawn_rate = 30
    phase = 1
    start_time = pygame.time.get_ticks()

    pygame.mixer.music.load(level1_music)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        clock.tick(60)
        current_time = (pygame.time.get_ticks() - start_time) // 1000

        if current_time >= 40 and phase == 1:
            phase = 2
            pygame.mixer.music.stop()
            pygame.mixer.music.load(level2_music)
            pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Spawn
        if random.randint(1, enemy_spawn_rate) == 1:
            x_pos = random.randint(0, SCREEN_WIDTH - 50)
            if phase == 1:
                enemies.append(Enemy(x_pos, -50))
            else:
                # fase 2 → escolhe entre inimigo normal ou inimigo2
                if random.choice([True, False]):
                    enemies.append(Enemy(x_pos, -50))
                else:
                    enemies.append(Enemy2(x_pos, -50))

        # Refresh enemies
        active_enemies = []
        for enemy in enemies:
            enemy.move()
            enemy.shoot()
            if enemy.y < SCREEN_HEIGHT:
                active_enemies.append(enemy)
        enemies = active_enemies

        # Refresh proj.
        active_projectiles = []
        for proj in player.projectiles:
            proj.y -= 10
            if proj.y > 0:
                active_projectiles.append(proj)
        player.projectiles = active_projectiles

        # Collision proj. enemy
        for proj in player.projectiles[:]:
            for enemy in enemies[:]:
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
                if proj.colliderect(enemy_rect):
                    player.projectiles.remove(proj)
                    enemies.remove(enemy)
                    player.score += 5
                    break

        # Enemy proj.
        for enemy in enemies:
            active_enemy_proj = []
            for proj in enemy.projectiles:
                proj.y += 7
                if proj.y < SCREEN_HEIGHT:
                    active_enemy_proj.append(proj)
                player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
                if proj.colliderect(player_rect):
                    player.lives -= 1
                    if proj in active_enemy_proj:
                        active_enemy_proj.remove(proj)
            enemy.projectiles = active_enemy_proj

        # Collis. player × enemies
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            if player_rect.colliderect(enemy_rect):
                enemies.remove(enemy)
                player.lives -= 1

        if player.lives <= 0:
            running = False

        # Draw bg
        screen.blit(background1 if phase == 1 else background2, (0, 0))
        player.draw()
        for enemy in enemies:
            enemy.draw()

        score_text = game_font.render(f"Score: {player.score}", True, WHITE)
        lives_text = game_font.render(f"Lives: {player.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

        pygame.display.flip()

    game_over_screen(player.score)
    main_menu()
    run_game()


if __name__ == "__main__":
    main_menu()
    run_game()
