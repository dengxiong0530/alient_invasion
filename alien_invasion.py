import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_settings.bg_color
    ship = Ship(screen, ai_settings)
    bullets = Group()
    alients = Group()

    while True:
        gf.check_events(ship, bullets, ai_settings, screen)
        ship.update()
        gf.update_bullets(bullets)
        gf.creat_fleet(ai_settings, screen, alients, ship)
        gf.update_screen(screen, bg_color, ship, bullets,alients)


run_game()
