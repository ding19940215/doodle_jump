import pygame.font


class GameOver():
    def __init__(self, screen, msg):
        """初始化界面属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置界面的尺寸和其他属性
        self.width, self.height = 200, 50
        self.over_color = (54, 140, 217)
        self.text_color = (255, 255, 25)
        self.font = pygame.font.SysFont(None, 48)

        # 创建界面的rect对象，并且让其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 创建一次结束界面
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并将其在界面上居中显示"""
        self.msg_images = self.font.render(msg, True, self.text_color, self.over_color)
        self.msg_images_rect = self.msg_images.get_rect()
        self.msg_images_rect.center = self.rect.center

    def draw_over(self):
        # 绘制一个用颜色填充的界面，再绘制文本
        self.screen.fill(self.over_color, self.rect)
        self.screen.blit(self.msg_images, self.msg_images_rect)
