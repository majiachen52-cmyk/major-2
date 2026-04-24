import pygame
from Character import Player
from Arrow import Arrow, load_arrow_images
from MeleeWeapon import MeleeWeapon, load_melee_images

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Test")
clock = pygame.time.Clock()

player = Player()
arrow_images = load_arrow_images()
arrows = []

melee_images = load_melee_images()
melee_weapons = []

walls = [
    pygame.Rect(200, 150, 120, 180),
    pygame.Rect(500, 300, 100, 150)
]

game_active = True
while game_active:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                x, y = player.get_center()
                arrows.append(Arrow(x, y, player.direction, arrow_images))

            if event.key == pygame.K_q:
                x, y = player.get_center()
                melee_weapons.append(MeleeWeapon(x, y, player.direction, melee_images))

    keys = pygame.key.get_pressed()
    player.move(keys, walls)

    for arrow in arrows[:]:
        alive = arrow.update(walls)
        if not alive or arrow.off_screen(WIDTH, HEIGHT):
            arrows.remove(arrow)

    for weapon in melee_weapons[:]:
        alive = weapon.update()
        if not alive:
            melee_weapons.remove(weapon)

    screen.fill((30, 30, 30))

    for wall in walls:
        pygame.draw.rect(screen, (120, 120, 120), wall)

    player.draw(screen)

    for arrow in arrows:
        arrow.draw(screen)

    for weapon in melee_weapons:
        weapon.draw(screen)

    pygame.display.flip()

pygame.quit()