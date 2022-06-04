from Button import button
from mazes import *
from Hero import *
import jiemian
import canshu
import other_f


def migongyouxi(cfg):
    
    # 初始化
    pygame.mixer.init()
    pygame.font.init()
    font = pygame.font.SysFont('Consolas', 15)
    qiehuan = button(position=(650, 380), size=(120, 52), clr=(255, 215, 0), cngclr=(255, 255, 0), func=other_f.fn8,
                     text='change role')
    while True:

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(cfg.SCREENSIZE)
        maze_now = RandomMaze(cfg.MAZESIZE, cfg.BLOCKSIZE, cfg.BORDERSIZE)
        hero_now = Hero(cfg.renwu[canshu.flag_renwu], [0, 0], cfg.BLOCKSIZE, cfg.BORDERSIZE)
        num_steps = 0
        while True:
            clock.tick(cfg.FPS)
            screen.fill((255, 255, 224))
            is_move = False
            x = hero_now.coordinate[0]
            y = hero_now.coordinate[1]
            hero_now = Hero(cfg.renwu[canshu.flag_renwu], [x, y], cfg.BLOCKSIZE, cfg.BORDERSIZE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(-1)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        is_move = hero_now.move('up', maze_now)
                        canshu.keyizou_sound.play()
                    elif event.key == pygame.K_DOWN:
                        is_move = hero_now.move('down', maze_now)
                        canshu.keyizou_sound.play()
                    elif event.key == pygame.K_LEFT:
                        is_move = hero_now.move('left', maze_now)
                        canshu.keyizou_sound.play()
                    elif event.key == pygame.K_RIGHT:
                        is_move = hero_now.move('right', maze_now)
                        canshu.keyizou_sound.play()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if qiehuan.rect.collidepoint(pos):
                            qiehuan.call_back()

            num_steps += int(is_move)
            hero_now.draw(screen)
            maze_now.draw(screen)
            qiehuan.draw(screen)
            showText(screen, font, 'STEPS: %s' % num_steps, (255, 0, 0), (570, 100))
            showText(screen, font, "MAX steps : 500", (0, 0, 0), (570, 150))
            showText(screen, font, 'S: birthing place', (0, 0, 0), (570, 200))
            showText(screen, font, 'D: finishing place', (0, 0, 0), (570, 250))
            # ----判断游戏是否胜利
            if num_steps > 500:
                jiemian.enddd()
            if (hero_now.coordinate[0] == cfg.MAZESIZE[1] - 1) and (hero_now.coordinate[1] == cfg.MAZESIZE[0] - 1):
                jiemian.endd2()
            pygame.display.update()
