class GameStats():
    """跟踪游戏的状态信息"""
    def __init__(self):
        # 游戏刚启动时处于活动状态
        self.game_active = True
        self.score = 0