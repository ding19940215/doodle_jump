import sys
import pygame
from pedal import Pedal
import random


def check_events(graffiti):
    """响应按键事件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, graffiti)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, graffiti)


def check_keydown_events(event, graffiti):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        graffiti.moving_right = True
    elif event.key == pygame.K_LEFT:
        graffiti.moving_left = True


def check_keyup_events(event, graffiti):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        graffiti.moving_right = False
    elif event.key == pygame.K_LEFT:
        graffiti.moving_left = False


def update_screen(ai_settings, screen, graffiti, pedals,stats,gameOver,score):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都要重绘屏幕
    screen.fill(ai_settings.bg_color)
    for pedal in pedals.sprites():
        pedal.draw_pedal()
    graffiti.blitme()
    # 绘制分数
    score.show_score()
    # 如果游戏处结束，则绘制结束界面
    if not stats.game_active:
        gameOver.draw_over()
    # 让最近绘制的图像可见
    pygame.display.flip()


def update_pedal(pedals, ai_settings, screen):
    """初始时踏板绘制"""
    pedal = Pedal(ai_settings, screen)
    pedals.add(pedal)
    for num in range(ai_settings.pedal_num):
        pedal = Pedal(ai_settings, screen)
        pedal.rect.centerx = random.randint(0, ai_settings.screen_width)
        pedal.rect.bottom = screen.get_rect().bottom - ai_settings.pedal_gap * num
        pedals.add(pedal)
    print(pedals)

def update_pedals(pedals,ai_settings,screen):
    """实时更新绘制踏板"""
    for pedal in pedals:
        if pedal.rect.bottom>600:
            pedals.remove(pedal)
            pedal_new=Pedal(ai_settings,screen)
            pedal_new.rect.centerx = random.randint(0, ai_settings.screen_width)
            pedal_new.rect.bottom = 0
            pedals.add(pedal_new)