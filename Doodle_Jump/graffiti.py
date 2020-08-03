import pygame
import time


class Graffiti():
    def __init__(self, screen, ai_settings):
        """初始化涂鸦并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载涂鸦图像并获取其外接矩形
        self.image = pygame.transform.scale(pygame.image.load('images/Ainsley.bmp'), (40, 55))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将涂鸦放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - ai_settings.pedal_height

        # 设置cenrer属性保存小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 向上跳跃标志
        self.moving_top = True
        # 当次跳跃的距离
        self.moving_topNum = 0
        # 距离窗口底部的距离
        self.moving_fraction = 0

    def blitme(self):
        """在指定位置绘制涂鸦"""
        self.screen.blit(self.image, self.rect)

    def jump(self, ai_settings, pedals, stats):
        """小涂鸦向上跳跃"""
        if self.moving_top:
            self.moving_topNum += ai_settings.graffiti_jump_factor
            self.rect.bottom = self.screen_rect.bottom - ai_settings.pedal_height - \
                               self.moving_topNum - self.moving_fraction
            if round(self.moving_topNum) == ai_settings.pedal_jump_height:
                self.moving_top = False
        elif self.moving_top is False:
            self.moving_topNum -= ai_settings.graffiti_jump_factor
            self.rect.bottom = self.screen_rect.bottom + ai_settings.pedal_height \
                               - self.moving_topNum - self.moving_fraction
            # 向下移动时判断碰撞
            collisions = pygame.sprite.spritecollideany(self, pedals, False)
            if collisions:
                # if self.rect.bottom == collisions.rect.top:
                if self.rect.bottom - collisions.rect.top == 1:
                    self.moving_topNum = 0
                    self.moving_fraction = self.screen_rect.bottom - self.rect.bottom
                    self.moving_top = True
                self.pedals_moving(collisions, pedals, ai_settings, stats)

    def pedals_moving(self, collisions, pedals, ai_settings, stats):
        """踏板跟随屏幕向下移动"""
        if collisions.rect.bottom < ai_settings.screen_height * 0.8:
            for pedal in pedals:
                pedal.rect.bottom += ai_settings.pedal_jump_height
            stats.score += ai_settings.pedal_jump_height

    def update(self, ai_settings, pedals, stats):
        # 更新center值，最后将center值赋给self.rect.cenrerx中
        # 在踏板跳跃
        self.jump(ai_settings, pedals, stats)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.graffiti_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.graffiti_speed_factor
        elif self.moving_right and self.rect.right == self.screen_rect.right:
            self.center = 0
        elif self.moving_left and self.rect.left == 0:
            self.center = self.screen_rect.right
        self.rect.centerx = self.center
        if self.rect.top > 600:
            stats.game_active = False
