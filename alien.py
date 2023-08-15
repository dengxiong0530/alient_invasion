import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("alien_invasion/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.alien_speed_factor

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)
