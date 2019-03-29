import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_event(event,ai_settings,screen,ship,bullets):
    '''按键响应'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #   创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
        #   按q结束游戏
    elif event.key == pygame.K_q:
        exit()

def check_keyup_event(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    '''响应键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type ==pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    '''每次循环时都刷新'''
    screen.fill(ai_settings.bg_color)
    #   在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #   让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    # 删除已消失的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def update_alien(aliens):
    '''更新外星人群中所有的外星人位置'''
    aliens.update()

def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''
    #   创建一个外星人，并计算一行可容纳多少个外星人
    #   外星人的间距为外星人的宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #   创建外星群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行可容纳多少个外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并将它放在当前行'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取对应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将外星人整体下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens):
    '''检查是否有外星人位于屏幕边缘，并更新整群外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()