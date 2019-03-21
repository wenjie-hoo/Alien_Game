import sys
import pygame

def check_keydown_event(event,ship):
    '''按键响应'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_event(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''响应键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ship)
        elif event.type ==pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(ai_settings,screen,ship):
    #   每次循环时都刷新
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #   让最近绘制的屏幕可见
    pygame.display.flip()