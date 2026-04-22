import pygame


def load_arrow_images():
    arrow_images = {
        "up": pygame.transform.scale(
            pygame.image.load("a1_up.png").convert_alpha(), (30, 30)
        ),
        "down": pygame.transform.scale(
            pygame.image.load("a1_down.png").convert_alpha(), (30, 30)
        ),
        "left": pygame.transform.scale(
            pygame.image.load("a1_left.png").convert_alpha(), (30, 30)
        ),
        "right": pygame.transform.scale(
            pygame.image.load("a1_right.png").convert_alpha(), (30, 30)
        )
    }
    return arrow_images


class Arrow:
    def __init__(self, x, y, direction, arrow_images):
        self.direction = direction
        self.image = arrow_images[direction]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 8

        if direction == "up":
            self.dx = 0
            self.dy = -self.speed
        elif direction == "down":
            self.dx = 0
            self.dy = self.speed
        elif direction == "left":
            self.dx = -self.speed
            self.dy = 0
        elif direction == "right":
            self.dx = self.speed
            self.dy = 0

    def update(self, walls):
        self.rect.x += self.dx
        self.rect.y += self.dy

        for wall in walls:
            if self.rect.colliderect(wall):
                return False

        return True

    def off_screen(self, width, height):
        return (
            self.rect.right < 0 or
            self.rect.left > width or
            self.rect.bottom < 0 or
            self.rect.top > height
        )

    def draw(self, screen):
        screen.blit(self.image, self.rect)