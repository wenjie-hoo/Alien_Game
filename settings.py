class Setting():

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #   外星人设置
        self.fleet_drop_speed = 10


        #   子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10

        #   飞船设置
        self.ship_limit = 3

        #   以什么样的速度加快游戏节奏
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随着游戏进行而变化的设置'''
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 3

        #   fleed_direction为1表示向右边移动，-1代表向左边移动
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale