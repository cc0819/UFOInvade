#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/2 下午3:12
# @Author  : C.C
# @File    : alien_invasion.py
from pygame.sprite import Group

import invade.game_functions as gf
import pygame

from invade.game_start import GameStart
from invade.setting import Setting
from invade.ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕的对象
    pygame.init()
    settings = Setting()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("UFO Invasion")

    # 创建一个存储游戏统计信息的实例
    start = GameStart(settings)

    # 创建一艘飞船
    ship = Ship(settings, screen)
    # 创建子弹
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(settings, screen, ship, aliens)
    # # 创建一个外星人
    # alien = Alien(settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(settings,screen,ship,bullets)

        if start.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(settings, start, screen, ship, aliens, bullets)

        gf.update_screen(settings, screen, ship, aliens, bullets)

run_game()
