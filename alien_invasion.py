import sys
import pygame
import ship

def run_game():
    #   初始化游戏并创造一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #   创建一个飞船
    ship = Ship
    #   创建背景颜色
    bg_color = (230,230,230)

    #   开始游戏的主循环
    while True:
        #   监听鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #   每次循环时都刷新
        screen.fill(bg_color)
        ship.blitme()

        #   让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
