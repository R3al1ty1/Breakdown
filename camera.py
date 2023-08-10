import pygame

class CameraGroup:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.camera_borders = {'left': 5, 'right': 5, 'top': 2.5, 'bottom': 2.5}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = (self.camera_borders['left'] + self.camera_borders['right'])
        h = (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l, t, w, h)

        self.ground_surf = pygame.image.load('map/NEW MAP.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def box_target_camera(self, target):
        if target.x < self.camera_rect.left:
            self.camera_rect.left = target.x * 100
        if target.x > self.camera_rect.right:
            self.camera_rect.right = target.x * 100
        if target.y < self.camera_rect.top:
            self.camera_rect.top = target.y * 100
        if target.y > self.camera_rect.bottom:
            self.camera_rect.bottom = target.y * 100

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def custom_draw(self, player):
        self.box_target_camera(player)

        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)

        player_offset = (player.x - self.offset.x, player.y - self.offset.y)
        self.display_surface.blit(self.ground_surf, player_offset)

