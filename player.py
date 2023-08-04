import pygame
import math
from consts import *
from bullet import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.is_shooting = False
        self.diag_move_corr = 1 / math.sqrt(2)


    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        num_key_pressed = 0
        if keys[pygame.K_d]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_a]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_w]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_s]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        if pygame.mouse.get_pressed()[0]:
            self.is_shooting = True
        else:
            self.is_shooting = False

        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]:
             self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
             self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
         return (x, y) not in self.game.map.world_map

    def shoot(self):
        bullet = Bullet(self.game, self.x, self.y, self.angle)
        self.game.bullets.append(bullet)

    def check_wall_collision(self, dx, dy):
         scale = PLAYER_SIZE_SCALE / self.game.delta_time
         if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
         if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.move()
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_x = mouse_x - self.x * 100
            delta_y = mouse_y - self.y * 100
            self.angle = math.atan2(delta_y, delta_x)
            self.angle %= math.tau
            self.shoot()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)