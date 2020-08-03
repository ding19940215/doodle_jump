import pygame.font


class Score():
    """显示得分信息类"""

    def __init__(self, screen, stats, ai_settings):
        """初始化得分信息"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_settings = ai_settings

        # 显示得分信息的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 44)

        # 准备初始得分图像
        self.prep_scroe()

    def prep_scroe(self):
        """将得分信息渲染为图像"""
        score_str = str(self.stats.score)
        self.score_imge = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在右上角
        self.score_rect = self.score_imge.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示分数"""
        self.screen.blit(self.score_imge, self.score_rect)
