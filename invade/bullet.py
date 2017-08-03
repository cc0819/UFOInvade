#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/2 下午8:19
# @Author  : C.C
# @File    : bullet.py
import pygame
from pygame.sprite import Sprite

'''飞船子弹管理类'''
class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        '''在飞船处创建一个子弹的对象'''
        super(Bullet, self).__init__()
        self.screen = screen

        '''在（0，0）处创建一个表示子弹的矩形，在设置正确的位置'''
        self.rect = pygame.Rect(0, 0, settings.bullet_with,settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed


    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y -=self.speed
        # 更新表示子弹的rect位置
        self.rect.y = self.y


    def draw_bullet(self):
        '''绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)



