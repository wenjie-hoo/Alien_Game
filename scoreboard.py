import pygame.font

class Scporeboard():
    '''显示得分信息的类'''
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen.rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #   显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #   准备初时得分的图像

    def prep_score(self):
        '''将得分渲染为图像'''
        score_str = str(self.stats.score)
        self.score_img =  self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)