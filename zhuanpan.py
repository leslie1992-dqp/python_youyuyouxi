import jiemian
from Button import button
import sys
from canshu import *
import math
import other_f


def end(suger):
    global r, ft1_surf, ctime, flag,timer_event
    while True:
        font1 = pygame.font.SysFont("ziti.ttf", 28)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == timer_event:
                ctime -= 1
                text1 = "Last: " + str(ctime)
                ft1_surf = font1.render(text1, True, 'red')
                if ctime == 0:
                    pygame.time.set_timer(timer_event,0)

            if event.type == pygame.KEYDOWN:
                start1()

        if flag == 4 and ctime >= -1 :
            endd()
        if ctime <= 1:
            jiemian.enddd()

        text1 = "Last: " + str(ctime)
        ft1_surf = font1.render(text1, True, 'red')
        text_score = "score: " + str(flag)
        ft_surf = font1.render(text_score, True, 'black')
        #围绕着一个点转的秘诀
        posx = 400 + int(150 * math.sin(r * math.pi / 180))
        posy = 300 + int(150 * math.cos(r * math.pi / 180))
        window.fill('white')
        zhizhen1 = pygame.transform.rotate(zhizhen, r)
        newRect = zhizhen1.get_rect(center=(posx, posy))
        window.blit(suger, (300, 350))
        window.blit(zhuanpan, (200, 0))
        window.blit(zhizhen1, newRect)
        window.blit(ft1_surf, [window.get_width() / 2 - ft1_surf.get_width() / 2, 100])
        window.blit(ft_surf, (620, 250))
        pygame.display.update()


def start1():
    global r,ft1_surf,ctime,flag,timer_event
    text1 = "Last: " + str(ctime)

    r = -90
    font1 = pygame.font.SysFont("ziti.ttf", 28)
    text_score = "score: " + str(flag)
    ft_surf = font1.render(text_score, True, 'black')
    window.blit(ft_surf, (500, 250))
    ft1_surf = font1.render(text1, True, 'red')
    while True:
        posx = 400 + int(150 * math.sin(r * math.pi / 180))
        posy = 300 + int(150 * math.cos(r * math.pi / 180))
        print(posx,posy)
        ft1_surf = font1.render(text1, True, 'red')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == timer_event:
                ctime -= 1
                text1 = "Last: " + str(ctime)
                ft1_surf = font1.render(text1, True, 'red')
                if ctime == 0:
                    pygame.time.set_timer(timer_event,0)
            if event.type == pygame.KEYDOWN:

                if r <= -165 and r >= -195:
                    flag += 1
                    end(sugers[flag])
                else:
                    end(sugers[flag])

        if flag == 4 and ctime >= -1:
            endd()
        if ctime <= 1 :

            jiemian.enddd()
        text_score = "score: " + str(flag)
        ft_surf = font1.render(text_score, True, 'black')
        window.fill('white')
        r += -12
        zhizhen1 = pygame.transform.rotate(zhizhen, r)
        newRect = zhizhen1.get_rect(center=(posx, posy))
        window.blit(sugers[flag], (300, 350))
        window.blit(zhuanpan,(200,0))
        window.blit(zhizhen1, newRect)
        window.blit(ft1_surf, [window.get_width() / 2 - ft1_surf.get_width() / 2, 100])
        window.blit(ft_surf, (620, 250))
        tick.tick(10)
        pygame.display.update()





def endd():
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=other_f.fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), other_f.fn2, 'next')

    button_list = [button1, button2]
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


        font = pygame.font.SysFont("ziti.ttf", 50)
        window.fill('white')
        text2 = "You Are Alive!!"
        ft2_surf = font.render(text2, True, 'green')
        window.blit(dianzan,(320,200))
        window.blit(ft2_surf, [window.get_width() / 2 - ft2_surf.get_width() / 2, 100])
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def zhuanpanyouxi():
    global  ctime,timer_event,tick,r,flag
    window.fill('white')
    pygame.time.set_timer(timer_event, 1000)
    font = pygame.font.SysFont("ziti.ttf", 28)
    text1 = "Last: " + str(ctime)
    ft1_surf = font.render(text1, True, 'red')
    window.blit(ft1_surf, [window.get_width() / 2 - ft1_surf.get_width() / 2, 100])
    pygame.display.flip()

    while True:
        font1 = pygame.font.SysFont("ziti.ttf", 28)
        text_score = "score: " + str(flag)
        ft_surf = font1.render(text_score, True, 'black')
        window.blit(ft_surf, (620, 250))
        posx = 400 + int(150 * math.sin(r * math.pi / 180))
        posy = 300 + int(150 * math.cos(r * math.pi / 180))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == timer_event:
                ctime -= 1
                text1 = "Last: " + str(ctime)
                ft1_surf = font.render(text1, True, 'red')
                if ctime == 0:
                    pygame.time.set_timer(timer_event, 0)
            if event.type == pygame.KEYDOWN:
                if r <= -175 and r >= -185:
                    flag += 1
                    end(sugers[flag])
                else:
                    end(sugers[flag])

        if flag == 4 and ctime >= -1:
            endd()
        if ctime <= 1:
            jiemian.enddd()
        window.fill('white')
        r += -12
        zhizhen1 = pygame.transform.rotate(zhizhen, r)
        newRect = zhizhen1.get_rect(center=(posx, posy))
        text_score = "score: " + str(flag)
        ft_surf = font1.render(text_score, True, 'black')
        window.blit(sugers[0], (300, 350))
        window.blit(zhuanpan, (200, 0))
        window.blit(zhizhen1, newRect)
        window.blit(ft1_surf, [window.get_width() / 2 - ft1_surf.get_width() / 2, 100])
        window.blit(ft_surf, (620, 250))
        tick.tick(10)
        pygame.display.flip()