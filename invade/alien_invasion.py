#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/2 下午3:12
# @Author  : C.C
# @File    : alien_invasion.py

import pygame

import invade.game_functions as gf
from invade.button import Button
from invade.game_start import GameStart
from invade.scoreboard import Scorebroard
from invade.setting import Setting
from invade.ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕的对象
    pygame.init()
    settings = Setting()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("UFO Invasion")

    # 创建一个存储游戏统计信息的实例
    start = GameStart(settings)
    sb = Scorebroard(settings, screen, start)

    # 创建一艘飞船
    ship = Ship(settings, screen)
    # 创建子弹
    aliens = Group()
    bullets = Group()

    # 创建外星人群
    gf.create_fleet(settings, screen, ship, aliens)
    # # 创建一个外星人
    # alien = Alien(settings, screen)

    # 创建Play按钮
    play_button = Button(settings, screen, "Play")

    # 开始游戏的主循环
    while True:
        gf.check_events(settings, screen, start, play_button,sb, ship, aliens, bullets)

        if start.game_active:
            ship.update()
            gf.update_bullets(settings, screen,start,sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen,  start, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, start,sb, ship, aliens, bullets
                         , play_button)


run_game()
