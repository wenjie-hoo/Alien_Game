import sys
import pygame
from settings import Setting
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #   初始化游戏并创造一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #   创建一个飞船
    ship = Ship(ai_settings,screen)

    #   创建一个用于储存子弹的编组
    bullets = Group()
    aliens = Group()
    #   创建外星群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #   开始游戏的主循环
    while True:
        #   监听鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_aliens(ai_settings,aliens)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
