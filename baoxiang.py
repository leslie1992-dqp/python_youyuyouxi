import jiemian
import canshu
import other_f
import pygame
from Button import button
import sys

def baoxiangyouxi():
    global flag_baoxiang
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    window.fill('white')
    baoxiang = pygame.transform.scale(pygame.image.load('D:/yysc/baoxiang.png'), (100, 100)).convert_alpha()
    button1 = button(position=(150, 200), size=(100, 50), clr=(245, 245, 220), cngclr=(0, 255, 0), func=other_f.fn15,
                     text='No1')
    button2 = button((380, 200), (100, 50), (245, 245, 220), (0, 255, 0), other_f.fn16, 'No2')
    button3 = button((630, 200), (100, 50), (245, 245, 220), (0, 255, 0), other_f.fn17, 'No3')
    button4 = button((380, 450), (100, 50), (245, 245, 220), (255, 0, 0), other_f.fn18, 'Sure')
    window.blit(baoxiang,(100,200))
    window.blit(baoxiang, (300, 200))
    window.blit(baoxiang, (500, 200))
    button_list = [button1, button2,button3,button4]
    pygame.display.flip()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in button_list:
                        if b.rect.collidepoint(pos):
                            b.call_back()
        window.fill('white')
        for b in button_list:
            b.draw(window)
        window.blit(baoxiang, (100, 250))
        window.blit(baoxiang, (330, 250))
        window.blit(baoxiang, (580, 250))
        pygame.display.update()

def zuihouxianshi(first,second,third):

    window = pygame.display.set_mode((800, 600))
    window.fill('white')
    jinbi = pygame.transform.scale(pygame.image.load('D:/yysc/jinbi.png'), (100, 100)).convert_alpha()
    wangguan = pygame.transform.scale(pygame.image.load('D:/yysc/wangguan.png'), (100, 100)).convert_alpha()
    tougu = pygame.transform.scale(pygame.image.load('D:/yysc/tougu.png'), (100, 100)).convert_alpha()
    zhongjiangs = [jinbi, wangguan, tougu]
    jiazhi = ['$ 2000', '$ 20w', '$ 40']
    small_font = pygame.font.SysFont("FangSong", 30)
    if canshu.zhongjiang_flag == 0:
        text = "你最终获得的财富是 ：" + str(jiazhi[first])
    elif canshu.zhongjiang_flag == 1:
        text = "你最终获得的财富是 ：" + str(jiazhi[second])
    else:
        text = "你最终获得的财富是 ：" + str(jiazhi[third])
    text_surface1 = small_font.render(text, True, 'black')
    button1 = button(position=(150, 200), size=(100, 50), clr=(245, 245, 220), cngclr=(245, 245, 220), func=other_f.fn19,
                     text=jiazhi[first])
    button2 = button((380, 200), (100, 50), (245, 245, 220), (245, 245, 220), other_f.fn19, jiazhi[second])
    button3 = button((630, 200), (100, 50), (245, 245, 220), (245, 245, 220), other_f.fn19, jiazhi[third])
    button4 = button((380, 450), (100, 50), (245, 245, 220), (255, 0, 0), other_f.fn20, 'Quit')
    window.blit(zhongjiangs[first], (100, 200))
    window.blit(zhongjiangs[second], (300, 200))
    window.blit(zhongjiangs[third], (500, 200))
    window.blit(text_surface1, (250, 10))
    button_list = [button1, button2, button3, button4]
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in button_list:
                        if b.rect.collidepoint(pos):
                            b.call_back()
        window.fill('white')
        for b in button_list:
            b.draw(window)
        window.blit(zhongjiangs[first], (100, 250))
        window.blit(zhongjiangs[second], (330, 250))
        window.blit(zhongjiangs[third], (580, 250))
        window.blit(text_surface1, (190, 60))
        pygame.display.update()
