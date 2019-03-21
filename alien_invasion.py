import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf

def run_game():
    #   初始化游戏并创造一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heiht))
    pygame.display.set_caption("Alien Invasion")

    #   创建一个飞船
    ship = Ship(ai_settings,screen)
    #   创建背景颜色
    bg_color = (230,230,230)

    #   开始游戏的主循环
    while True:
        #   监听鼠标和键盘事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()
