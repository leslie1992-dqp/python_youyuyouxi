import jiemian
from Button import button
import canshu
import other_f
import pygame
import sys

def panduan(wanjia,diannao):
    if (wanjia == 0 and diannao ==2) or (wanjia == 1 and diannao == 0) or (wanjia ==2 and diannao == 1):
        yingderen = 0
        return yingderen
    elif wanjia == diannao:
        yingderen = 1
        return yingderen
    else:
        yingderen = 2
        return yingderen


def caiquanyouxi():

    font = pygame.font.SysFont("ziti.ttf", 28)
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((canshu.width, canshu.height))
    window.fill((255, 255, 224))
    text1 = "player: " + str(canshu.wanjia_score)
    text2 = "computer: " + str(canshu.diannao_score)
    text3 = "roles: " + str(canshu.huihe)
    text4 = "Who has 10 score who win"
    ft1_surf = font.render(text1, True, 'black')
    ft2_surf = font.render(text2, True, 'black')
    ft3_surf = font.render(text3, True, 'black')
    ft4_surf = font.render(text4,True,'red')
    window.blit(ft1_surf, (450, 120))
    window.blit(ft2_surf, (450, 120))
    window.blit(ft3_surf, (450, 120))
    window.blit(ft4_surf,(450,120))
    button1 = button(position=(120, 250), size=(100, 50), clr=(255, 215, 0), cngclr=(255, 255, 0), func=other_f.fn11,
                     text='scissors')
    button2 = button((120, 340), (100, 50), (255, 215, 0), (255, 255, 0), other_f.fn12, 'stone')
    button3 = button((120, 430), (100, 50), (255, 215, 0), (255, 255, 0), other_f.fn13, 'cloth')
    button_sure = button((400, 520), (100, 50), (255, 215, 0), (255, 255, 0), other_f.fn_sure, 'sure')
    button_list = [button1, button2, button3, button_sure]
    window.blit(canshu.caiquan, (150, 0))
    window.blit(canshu.wanjia_quans[canshu.wanjia], (250, 300))
    window.blit(canshu.diannao_quans[canshu.diannao], (550, 300))
    pygame.display.flip()
    while True:
        clock.tick(20)
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

        if canshu.wanjia_score == 10:
            jiemian.diwuguan()
        if canshu.diannao_score == 10:
            jiemian.enddd()
        text1 = "player: " + str(canshu.wanjia_score)
        text2 = "computer: " + str(canshu.diannao_score)
        text3 = "roles: " + str(canshu.huihe)
        text4 = "Who has 10 score who win"
        ft1_surf = font.render(text1, True, 'black')
        ft2_surf = font.render(text2, True, 'black')
        ft3_surf = font.render(text3, True, 'black')
        ft4_surf = font.render(text4, True, 'red')
        window.fill((255, 255, 224))
        for b in button_list:
            b.draw(window)
        window.blit(canshu.caiquan, (150, 0))
        window.blit(canshu.wanjia_quans[canshu.wanjia], (250, 300))
        window.blit(canshu.diannao_quans[canshu.diannao], (550, 300))
        window.blit(ft1_surf, (550, 150))
        window.blit(ft2_surf, (550, 180))
        window.blit(ft3_surf, (550, 210))
        window.blit(ft4_surf,(550,240))
        pygame.display.flip()