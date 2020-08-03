import sys
import pygame
from settings import Settings
from graffiti import Graffiti
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from score import Score
from game_over import GameOver


def run_game():
    """"初始化游戏并创建一个窗口"""
    # 初始化背景设置
    pygame.init()
    ai_settings = Settings()
    # 创建显示窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Goodle Jump')
    graffiti = Graffiti(screen, ai_settings)
    # 创建一个保存所有踏板的编组
    pedals = Group()
    gf.update_pedal(pedals, ai_settings, screen)
    # 创建一个结束状态
    stats = GameStats()
    # 创建一个结束界面
    gameOver = GameOver(screen, "Game Over")
    # 创建一个得分
    score = Score(screen, stats, ai_settings)
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(graffiti)
        if stats.game_active:
            gf.update_pedals(pedals, ai_settings, screen)
            graffiti.update(ai_settings, pedals, stats)
            score.prep_scroe()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, graffiti, pedals, stats, gameOver, score)


run_game()
