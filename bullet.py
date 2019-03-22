import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射对子弹对管理的类'''

    def __init__(self,ai_settings,screen,ship):
        #   在飞船所处的位置创建一个子弹对象

        super().__init__()
        self.screen = screen

        #   在（0，0）处创建一个表示子弹的矩形，在设置其正确位置
        