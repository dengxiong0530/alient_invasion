class Settings:
    ''' 设置 '''

    def __init__(self):
        '''屏幕'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5  # 飞船速度

        '''子弹'''
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        '''外星人'''
        self.alien_speed_factor = 1
