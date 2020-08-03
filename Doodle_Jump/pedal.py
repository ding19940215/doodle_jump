import pygame
from pygame.sprite import Sprite


class Pedal(Sprite):
    """一个对踏板管理的类"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        # 在(0,0)处生成一个踏板，再设置其位置
        self.rect = pygame.Rect(0, 0, ai_settings.pedal_width, ai_settings.pedal_height)
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom
        self.color = ai_settings.pedal_color

    def draw_pedal(self):
        """在屏幕上绘制踏板"""
        pygame.draw.ellipse(self.screen, self.color, self.rect)
