#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/2 下午4:36
# @Author  : C.C
# @File    : setting.py

class Setting():
    # 存储《外星人入侵的所有设置的类》

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 10
        self.ship_limit = 3

        # 飞船子弹
        self.bullet_speed = 10
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10

        # 外星人设置
        self.alien_speed = 10
        self.fleet_drop_speed = 200
        # fleet_direction为表示向右移，为-1表示向左移
        self.fleet_direction = 1


