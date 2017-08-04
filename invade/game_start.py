#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/3 下午7:51
# @Author  : C.C
# @File    : game_start.py

class GameStart():
    '''跟踪游戏的统计信息'''

    def __init__(self, settings):
        '''初始化统计信息'''
        self.settings = settings
        self.reset_start()

        '''游戏刚启动的时候处于活动状态'''
        self.game_active = True

        # 在任何情况下不能充值最高分
        self.high_score = 0

    def reset_start(self):
        '''初始化在游戏期间可能变化的统计信息'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
