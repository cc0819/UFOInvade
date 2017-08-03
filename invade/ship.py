#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/8/2 下午4:58
# @Author  : C.C
# @File    : ship.py
import pygame


class Ship():
    def __init__(self, settings, screen):
        '''初始化飞机'''
        self.screen = screen
        self.settings = settings

        # 加载飞机图像并获取外形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每艘飞船摆在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)


        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞机位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.center-= self.settings.ship_speed

        # 根据self.center跟新rect对象
        self.rect.centerx = self.center


    def fix_position(self):
        '''在指定位置绘制飞机'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''飞船居中'''
        self.center = self.screen_rect.centerx