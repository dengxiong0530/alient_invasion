import sys
import pygame

from alien import Alien
from bullet import Bullet


def check_events(ship, bullets, ai_settings, screen):
    '''监听操作'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and len(bullets) <= ai_settings.bullet_allowed:
        bullet = Bullet(ai_settings, ship, screen)
        bullets.add(bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(screen, bg_color, ship, bullets, aliens):
    '''更新屏幕'''
    screen.fill(bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def creat_fleet(ai_settings, screen, alients, ship):
    alient = Alien(screen, ai_settings)
    alient_width = alient.rect.width
    number_alient_x = get_number_alient_x(ai_settings, alient_width)
    print(number_alient_x)
    rows = get_number_rows(ai_settings, ship.rect.height, alient.rect.height)

    for row in range(rows):
        for aliens_number in range(number_alient_x):
            create_alien(ai_settings, screen, alients, aliens_number, rows)


def get_number_alient_x(ai_settings, alient_width):
    availbale_space_x = ai_settings.screen_width - 2 * alient_width
    number_alient_x = int(availbale_space_x / (2 * alient_width))
    return number_alient_x


def create_alien(ai_settings, screen, alients, aliens_number, rows_number):
    alient = Alien(screen, ai_settings)
    alient_width = alient.rect.width
    alient.x = alient_width + 2 * alient_width * aliens_number
    alient.rect.x = alient.x
    alient.y = alient.rect.height + 2 * alient.rect.height * rows_number
    alients.add(alient)


def get_number_rows(ai_settings, ship_height, alient_height):
    availbale_space_y = ai_settings.screen_height - 3 * alient_height - ship_height
    rows = int(availbale_space_y / (2 * alient_height))
    return rows
