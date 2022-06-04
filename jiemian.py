
from Button import button
from canshu import *
from other_f import *



def kaishijiemian():
    kaishi = pygame.transform.scale(pygame.image.load('D:/yysc/youyu.png'), (800, 600)).convert_alpha()
    window.blit(kaishi, (0, 0))
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn14, 'next')

    button_list = [button1, button2]
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

        window.blit(kaishi, (0, 0))
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def youxijieshao():
    jieshao = pygame.transform.scale(pygame.image.load('D:/yysc/jieshao.png'), (600, 450)).convert_alpha()
    window.fill('white')
    window.blit(jieshao, (100, 0))
    button1 = button(position=(250, 500), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 500), (100, 50), (245, 245, 220), (0, 255, 0), fn6, 'next')
    button_list = [button1, button2]
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
        window.blit(jieshao, (100, 0))
        for b in button_list:
            b.draw(window)
        pygame.display.update()



def diyiguan():
    jqdyl = pygame.transform.scale(pygame.image.load('D:/yysc/chuchang1.png'), (600, 150)).convert_alpha()
    window.fill('white')
    window.blit(jqdyl, (100, 150))
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn5, 'start')
    button_list = [button1, button2]
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
        window.blit(jqdyl, (100, 150))
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def dierguan():

    mrdfy = pygame.transform.scale(pygame.image.load('D:/yysc/chuchang2.png'),(600,150)).convert_alpha()
    window.fill('white')
    window.blit(mrdfy,(100,150))
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn4, 'start')
    button_list = [button1, button2]
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
        window.blit(mrdfy, (100, 150))
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def disanguan():
    cmddn = pygame.transform.scale(pygame.image.load('D:/yysc/chuchang3.png'), (600, 150)).convert_alpha()
    window.fill('white')
    window.blit(cmddn, (100, 150))
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn7, 'start')
    button_list = [button1, button2]
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
        window.blit(cmddn, (100, 150))
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def disiguan():
    ohdyq = pygame.transform.scale(pygame.image.load('D:/yysc/chuchang4.png'), (600, 150)).convert_alpha()
    window.fill('white')
    window.blit(ohdyq, (100, 150))
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn10, 'start')
    button_list = [button1, button2]
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
        window.blit(ohdyq, (100, 150))
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def diwuguan():
    gxtg = pygame.transform.scale(pygame.image.load('D:/yysc/chuchang5.png'), (600, 350)).convert_alpha()
    window.fill('white')
    window.blit(gxtg, (100, 30))
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn21, 'start')
    button_list = [button1, button2]
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
        window.blit(gxtg, (100, 30))
        for b in button_list:
            b.draw(window)
        pygame.display.update()


def endd2():
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn9, 'next')

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
        window.blit(dianzan, (320, 200))
        window.blit(ft2_surf, [window.get_width() / 2 - ft2_surf.get_width() / 2, 100])
        for b in button_list:
            b.draw(window)
        pygame.display.update()

def enddd():
    siwang_sound.play()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        font = pygame.font.SysFont("ziti.ttf", 50)
        window.fill('white')
        text3 = "You have died!!"
        text4 = "Game over"
        ft3_surf = font.render(text3, True, 'red')
        ft4_surf = font.render(text4, True, 'red')
        window.blit(siwang, (0, 0))
        window.blit(ft3_surf, [window.get_width() / 2 - ft3_surf.get_width() / 2, 120])
        window.blit(ft4_surf, [window.get_width() / 2 - ft3_surf.get_width() / 2 + 40, 200])
        pygame.display.update()

#第一关成功后的选择界面
def endd1():
    button1 = button(position=(250, 470), size=(100, 50), clr=(245, 245, 220), cngclr=(255, 0, 0), func=fn1,
                     text='give up')
    button2 = button((530, 470), (100, 50), (245, 245, 220), (0, 255, 0), fn3, 'next')

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
        window.blit(dianzan, (320, 200))
        window.blit(ft2_surf, [window.get_width() / 2 - ft2_surf.get_width() / 2, 100])
        for b in button_list:
            b.draw(window)
        pygame.display.update()
