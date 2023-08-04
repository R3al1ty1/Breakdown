import pygame
import sys
import player
from consts import *

class Bullet:
    def __init__(self, target_x, target_y, game):
        self.game = game
        self.x = x
        self.y = y
        self.radius = 10
        self.speed = 20
        self.dx = target_x - x
        self.dy = target_y - y
        distance = max(1, int((self.dx ** 2 + self.dy ** 2) ** 0.5))
        self.dx /= distance
        self.dy /= distance

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self):
        pygame.draw.circle(self.game.screen, 'red', (int(self.x), int(self.y)), self.radius)

    def makeShots(self):
        clock = pygame.time.Clock()
        playerS = player.Player(WIDTH // 2, HEIGHT - 100)
        bullets = []
        bullet_cooldown = 0
        bullet_cooldown_time = 10

        if pygame.mouse.get_pressed()[0]:
            if bullet_cooldown <= 0:
                target_x, target_y = pygame.mouse.get_pos()
                bullet = player.Player(player.x + player.size // 2, player.y, target_x, target_y)
                bullets.append(bullet)

                bullet_cooldown = bullet_cooldown_time

        if bullet_cooldown > 0:
            bullet_cooldown -= clock.get_rawtime()

        for bullet in bullets[:]:
            bullet.move()
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                bullets.remove(bullet)