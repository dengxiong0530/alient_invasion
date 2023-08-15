import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.image = pygame.image.load("alien_invasion/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
