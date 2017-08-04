#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/2 下午5:20
# @Author  : C.C
# @File    : game_functions.py
from time import sleep

import pygame
import sys

from invade.alien import Alien
from invade.bullet import Bullet


def check_events(settings, screen, start, play_button, sb,ship, aliens, bullets):
    '''相应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, start, play_button,sb, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(settings, screen, start, play_button,sb, ship, aliens, bullets, mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_checked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_checked and not start.game_active:
        settings.init_dynamic_setting()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计数据
        start.reset_start()
        start.game_active = True

        # 充值记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人和飞船居中
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, screen, setting, ship)


def fire_bullet(bullets, screen, setting, ship):
    # 创建新子弹并将其加入到编组bullets中
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


def update_screen(settings, screen, start, sb, ship, aliens, bullets
                  , play_button):
    # 每次循环时都要绘制屏幕
    screen.fill(settings.bg_color)
    # 在飞船和外星人后边绘制所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.fix_position()
    # aliens.fix_position()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处理非活动状态，就绘制Play按钮
    if not start.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(settings, screen,start, sb,  ship, aliens, bullets):
    '''更新子弹的位置，并删除消失的子弹'''
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))

    check_bullet_aliens_collisions(settings, screen, start, sb, ship, aliens, bullets)


def check_high_score(start, sb):
    '''检查是否诞生了最高分'''
    if start.score > start.high_score:
        start.high_score = start.score
        sb.prep_high_score()


def check_bullet_aliens_collisions(settings, screen,start, sb,  ship, aliens, bullets):
    '''检查是否有子弹击中外星人'''
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for temp in collisions.values():
            start.score += settings.alien_points * len(temp)
            sb.prep_score()
        check_high_score(start,sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        settings.increase_speed()

        # 提高等级
        start.level += 1
        sb.prep_level()

        create_fleet(settings, screen, ship, aliens)


def change_fleet_direction(settings, aliens):
    '''将整群外星人下移并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(settings, aliens):
    '''有外星人到达边缘时采取措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def update_aliens(settings, screen, start, sb, ship, aliens, bullets):
    '''检查是否有外星人位于边缘'''
    check_fleet_edges(settings, aliens)
    '''更新外星人群所有人位置'''
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, start, sb,  ship, aliens, bullets)

    # 检测外星飞船是否到底部
    check_aliens_bottom(settings,screen, start, sb, ship, aliens, bullets)


def check_aliens_bottom(settings,screen, start, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            "像飞机被撞一样处理"
            ship_hit(settings,screen, start,sb,  ship, aliens, bullets)
            break


def ship_hit(settings, screen,start,sb, ship, aliens, bullets):
    '''相应被外星人撞到的飞船'''

    if start.ships_left > 0:
        # 将 ship_left减1
        start.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

    else:
        start.game_active = False
        pygame.mouse.set_visible(True)

    # 清理外星飞船和子弹
    aliens.empty()
    bullets.empty()

    # 创建新的外星人，并将飞船放在中间
    create_fleet(settings, screen, ship, aliens)
    ship.center_ship()

    # 暂停
    sleep(0.5)


def create_fleet(settings, screen, ship, aliens):
    '''创建外星人群'''
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(settings, screen)
    number_aliens_x = get_aliens_number_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens,
                         alien_number, row_number)


def get_aliens_number_x(settings, alien_width):
    alien_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(alien_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    alien_space_y = (settings.screen_height -
                     (3 * alien_height) - ship_height)
    number_rows = int(alien_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
