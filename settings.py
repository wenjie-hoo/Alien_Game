class Setting():

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #   外星人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 30
        #   fleed_direction为1表示向右边移动，-1代表向左边移动
        self.fleet_direction = 1

        #   子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #   飞船设置
        self.ship_limit = 3
        self.ship_speed_factor = 1.5