import sys
import pygame
import random
from settings import *
from player import Player
from enemies import Enemy, Enemy2
from menu import main_menu

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

        if random.randint(1, enemy_spawn_rate) == 1:
            x_pos = random.randint(0, SCREEN_WIDTH - 50)
            if phase == 1:
                enemies.append(Enemy(x_pos, -50))
            else:
                enemies.append(Enemy(x_pos, -50) if random.choice([True, False]) else Enemy2(x_pos, -50))

        active_enemies = []
        for enemy in enemies:
            enemy.move()
            enemy.shoot()
            if enemy.y < SCREEN_HEIGHT:
                active_enemies.append(enemy)
        enemies = active_enemies

        active_projectiles = []
        for proj in player.projectiles:
            proj.y -= 10
            if proj.y > 0:
                active_projectiles.append(proj)
        player.projectiles = active_projectiles

        for proj in player.projectiles[:]:
            for enemy in enemies[:]:
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
                if proj.colliderect(enemy_rect):
                    player.projectiles.remove(proj)
                    enemies.remove(enemy)
                    player.score += 5
                    break

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

        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            if player_rect.colliderect(enemy_rect):
                enemies.remove(enemy)
                player.lives -= 1

        if player.lives <= 0:
            running = False

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
