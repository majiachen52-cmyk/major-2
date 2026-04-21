import pygame
from Character import Player

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player()

walls = [
    pygame.Rect(200, 150, 120, 180)
]

game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    keys = pygame.key.get_pressed()
    player.move(keys, walls)

    screen.fill((30, 30, 30))

    for wall in walls:
        pygame.draw.rect(screen, (200, 50, 50), wall)

    player.draw(screen)

    pygame.draw.rect(screen, (0, 255, 0), player.get_rect(), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()