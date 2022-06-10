
import sys
import jiemian
from canshu import *


#女孩的运动变换
def biggirl_animation():
    new_girl = biggirl_frames[biggirl_index]
    new_girl_rect = new_girl.get_rect(center=(biggirl_rect.centerx, biggirl_rect.centery))
    return new_girl, new_girl_rect

#男孩的运动变换
def man_animation():
    new_man = man_frames[man_index]
    new_man_rect = new_man.get_rect(center=(man_rect.centerx, man_rect.centery))
    return new_man, new_man_rect

#男孩站着不动时的状态
def man_stand():
    new_man = man_frames[0]
    new_man_rect = new_man.get_rect(center=(man_rect.centerx, man_rect.centery))
    return new_man, new_man_rect


def redlight_display(light_status):
    if light_status == 1:
        score_surface = game_font.render("RED LIGHT", True, (255, 0, 0))
    else:
        score_surface = game_font.render("GREEN LIGHT", True, (0, 255, 0))

    score_rect = score_surface.get_rect(center=(400, 100))
    window.blit(score_surface, score_rect)


def gameover_display(gameover_status):
    if gameover_status == 1:
        jiemian.enddd()

    if gameover_status == 2:
        jiemian.endd1()



def mutouren1():
    global biggirl_surface,biggirl_rect,biggirl_index,otherman_status,gameover_status,man_surface,man_rect,man_status,man_index,pos_x,pos_y
    while True:
        clock.tick(100)
        if biggirl_index >= 5 and biggirl_index <= 10:
            light_status = 1
            otherman_status = 0
        else:
            light_status = 0
            otherman_status = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    man_status = 1
                    keyizou_sound.play()
                if event.key == pygame.K_SPACE:
                    man_status = 0
                    keyizou_sound.play()

            elif event.type == manFLAP:
                #不断变换图像，实现走动的效果
                if man_index < 6:
                     man_index = man_index + 1
                else:
                    man_index = 0
                #当状态为 1 时，走动；当状态为 0 时，站住不动
                if man_status == 1:
                    man_surface, man_rect = man_animation()
                else:
                    man_surface, man_rect = man_stand()

            elif event.type == biggirlFLAP:
                if gameover_status == 0:
                    if biggirl_index < 14:
                        biggirl_index = biggirl_index + 1
                    else:
                        biggirl_index = 0
                        huitou_sound.play()
                biggirl_surface, biggirl_rect = biggirl_animation()

        #判断游戏的状态，若为 0 ，则游戏继续；若为  1 ，则为结束
        if gameover_status == 0:
            window.blit(bg_surface, (0, 0))
            window.blit(biggirl_surface, biggirl_rect)
            window.blit(bili, (380, 290))
            window.blit(bili, (550, 330))
            window.blit(man_surface, man_rect)

            if man_status == 1:
                #人物斜着走的秘诀
                pos_x = pos_x + move_speed
                pos_y = pos_y - move_speed / 2
                man_rect.centerx = pos_x
                man_rect.centery = pos_y

            if man_status == 1 and light_status == 1:
                gameover_status = 1
                siwang_sound.play()
                gameover_display(gameover_status)

            #判断是否走到终点
            if (pos_y < 345):
                gameover_status = 2
                gameover_display(gameover_status)
            redlight_display(light_status)
        else:
            gameover_display(gameover_status)

        pygame.display.update()
