import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pet Food Collection")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player = pygame.Rect(370, 510, 60, 50)
foods = []
score, time_left = 0, 30
start = pygame.time.get_ticks()
playing = True

while playing:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.x, score, time_left = 370, 0, 30
            foods.clear()
            start = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 6
    player.clamp_ip(screen.get_rect())

    if time_left > 0:
        time_left = max(0, 30 - (pygame.time.get_ticks() - start) // 1000)
        if random.randrange(25) == 0:
            foods.append(pygame.Rect(random.randrange(780), 0, 20, 20))
        for food in foods[:]:
            food.y += 4
            if food.colliderect(player):
                foods.remove(food)
                score += 1
            elif food.y > 600:
                foods.remove(food)

    screen.fill((145, 215, 245))
    pygame.draw.rect(screen, (100, 180, 90), (0, 560, 800, 40))
    pygame.draw.rect(screen, (190, 125, 75), player, border_radius=12)
    pygame.draw.circle(screen, (255, 220, 100), (player.centerx, player.y - 5), 18)
    for food in foods:
        pygame.draw.circle(screen, (240, 160, 55), food.center, 10)

    screen.blit(font.render(f"Food: {score}   Time: {time_left}", True, (30, 40, 50)), (20, 20))
    if time_left == 0:
        screen.blit(font.render("Game over! Press SPACE to play again", True, (30, 40, 50)), (130, 280))

    pygame.display.flip()

pygame.quit()
