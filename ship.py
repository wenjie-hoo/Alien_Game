import pygame

class Ship():

    def __init__(self,screen):
        self.screen = screen

        #   加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = pygame.image.get_rect()
        self.screen = screen.get_rect()

        #   将每艘飞船放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.botom

    def blitme(self):
        #   在指定的位置绘制飞船
        self.screen.blit(self.image,self.rect)
