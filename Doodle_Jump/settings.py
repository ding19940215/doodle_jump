class Settings():
    """储存游戏的所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 400
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 涂鸦设置
        # 移动速度
        self.graffiti_speed_factor = 0.2
        # 跳起高度速度
        self.graffiti_jump_factor = 0.05
        # 踏板设置
        self.pedal_width = 70
        self.pedal_height = 15
        self.pedal_color = 110, 182, 22
        self.pedal_num = 15
        # 踏板高度间隙
        self.pedal_gap = 45
        # 踏板的跳起高度
        self.pedal_jump_height = 60