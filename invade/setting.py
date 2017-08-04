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
        self.ship_limit = 3

        # 飞船子弹
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10

        # 外星人设置
        self.fleet_drop_speed = 5


        # 以什么样的速度加快游戏的节奏
        self.speedup_scale = 1.1
        # 外星点数的提高速度
        self.score_scale = 1.5

        self.init_dynamic_setting()

    def init_dynamic_setting(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = 10
        self.bullet_speed = 10
        self.alien_speed = 5

        # fleet_direction为表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        '''速度提高设置'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)