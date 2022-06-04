import pygame

class button:
    '''
    position为位置
    clr为颜色和透明度
    cngclr为触碰后的背景颜色变化
    默认和按钮本身相同
    func为点击后的功能
    font为字体颜色
    text为按钮内容
    font_size为字体的大小
    font_clr为字体的颜色
    '''
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=[0, 0, 0]):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)

       #设置触碰后的背景颜色，若没有定义，默认为按钮背景的颜色
        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        #设置透明度，默认为255，0为完全透明
        if len(clr) == 4:
            self.surf.set_alpha(clr[3])


        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

    #画出按钮
    def draw(self, screen):
        self.mouseover()
        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    #触碰后的背景颜色变换
    def mouseover(self):
        self.curclr = self.clr
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr

   #点击后的功能显示
    def call_back(self, *args):
        if self.func:
            return self.func(*args)
