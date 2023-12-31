import pygame as pg
import sys
from map import *
from player import *
from bullet import *
from camera import  *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES, pygame.RESIZABLE)
        self.bg_img = pygame.image.load('map/bg_7680x4320.png')

        self.tmx_file = "map/NEW MAP no bg.tmx"
        self.tmx_data = pytmx.load_pygame(self.tmx_file)

        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.bullets = []
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.camera = CameraGroup()
    def update(self):
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        #self.map.draw()
        self.player.draw()
        for bullet in self.bullets:
            bullet.draw()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:

            self.check_events()
            self.update()
            self.draw()
            self.player.update()
            for bullet in self.bullets:
                bullet.update()
            self.camera.custom_draw(self.player)

if __name__ == '__main__':
    game = Game()
    game.run()