import pygame
import sys

pygame.init()

screen_width, screen_height = 1400, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move, Shoot, and Aim")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.color = WHITE
        self.speed = 5

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Circle:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = RED
        self.speed = 20
        self.dx = target_x - x
        self.dy = target_y - y
        distance = max(1, int((self.dx ** 2 + self.dy ** 2) ** 0.5))
        self.dx /= distance
        self.dy /= distance

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    clock = pygame.time.Clock()
    player = Square(screen_width // 2, screen_height - 100)
    bullets = []
    bullet_cooldown = 0
    bullet_cooldown_time = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Move the player with arrow keys
        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx -= player.speed
        if keys[pygame.K_d]:
            dx += player.speed
        if keys[pygame.K_w]:
            dy -= player.speed
        if keys[pygame.K_s]:
            dy += player.speed

        player.move(dx, dy)

        # Shoot bullets with mouse click
        if pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
            if bullet_cooldown <= 0:  # Check if the cooldown time has passed
                target_x, target_y = pygame.mouse.get_pos()
                bullet = Circle(player.x + player.size // 2, player.y, target_x, target_y)
                bullets.append(bullet)

                # Reset the cooldown time
                bullet_cooldown = bullet_cooldown_time

            # Reduce the cooldown time on each iteration
        if bullet_cooldown > 0:
            bullet_cooldown -= clock.get_rawtime()

            # Move and remove bullets
        for bullet in bullets[:]:
            bullet.move()
            if bullet.x < 0 or bullet.x > screen_width or bullet.y < 0 or bullet.y > screen_height:
                bullets.remove(bullet)

            # Update the screen
        screen.fill((0, 0, 0))
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()