import pygame



pygame.init()
width =800
height = 600
window = pygame.display.set_mode((width, height))
ico = pygame.image.load("D:/yysc/ico.png")
pygame.display.set_icon(ico)
pygame.display.set_caption('鱿鱼游戏')
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("D:/yysc/Segoe Print", 30)
small_font = pygame.font.SysFont("FangSong", 40)

bg_surface = pygame.transform.scale(pygame.image.load('D:/yysc/bg.png'),(800,600)).convert()
man_movement = 0.0
man_status = 0
move_speed = 0.5
move_timer = 10

otherman_status = 0
score = 0

#木头人的变量
bili = pygame.image.load('D:/yysc/bili.png')
keyizou_sound = pygame.mixer.Sound('D:/yysc/coin.wav')
siwang_sound = pygame.mixer.Sound('D:/yysc/bomb.wav')
huitou_sound = pygame.mixer.Sound('D:/yysc/song.wav')
man_run1 = pygame.transform.scale(pygame.image.load('D:/yysc/man_1.png'),(25,35)).convert_alpha()
man_run2 = pygame.transform.scale(pygame.image.load('D:/yysc/man_2.png'),(25,35)).convert_alpha()
man_run3 = pygame.transform.scale(pygame.image.load('D:/yysc/man_3.png'),(25,35)).convert_alpha()
man_run4 = pygame.transform.scale(pygame.image.load('D:/yysc/man_4.png'),(25,35)).convert_alpha()
man_run5 = pygame.transform.scale(pygame.image.load('D:/yysc/man_5.png'),(25,35)).convert_alpha()
man_run6 = pygame.transform.scale(pygame.image.load('D:/yysc/man_6.png'),(25,35)).convert_alpha()
man_run7 = pygame.transform.scale(pygame.image.load('D:/yysc/man_7.png'),(25,35)).convert_alpha()
biggirl_run0 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_0.png'),(50,90)).convert_alpha()
biggirl_run1 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_1.png'),(50,90)).convert_alpha()
biggirl_run2 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_2.png'),(50,90)).convert_alpha()
biggirl_run3 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_3.png'),(50,90)).convert_alpha()
biggirl_run4 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_4.png'),(50,90)).convert_alpha()
biggirl_run5 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_5.png'),(50,90)).convert_alpha()
biggirl_run6 = pygame.transform.scale(pygame.image.load('D:/yysc/girl_6.png'),(50,90)).convert_alpha()

man_frames = [man_run1, man_run2, man_run3, man_run4, man_run5, man_run6, man_run7]
man_index = 0
gameover_status = 0
man_surface = man_frames[0]
man_rect = man_surface.get_rect(center=(100, 500))
manFLAP = pygame.USEREVENT + 1
pos_x = 100
pos_y = 500
#每个一段时间去做一件事
pygame.time.set_timer(manFLAP, 20)
light_status = 0

biggirl_frames = [biggirl_run6, biggirl_run5, biggirl_run4, biggirl_run3, biggirl_run2, biggirl_run1, biggirl_run0,
                  biggirl_run0, biggirl_run0, biggirl_run1, biggirl_run2, biggirl_run3, biggirl_run4, biggirl_run5,
                  biggirl_run6]
biggirl_index = 0
biggirl_surface = biggirl_frames[0]
biggirl_rect = biggirl_surface.get_rect(center=(480, 320))
biggirlFLAP = pygame.USEREVENT + 2
pygame.time.set_timer(biggirlFLAP, 200)
gameover_status = 0
score_sound_countdown = 100



#转盘的变量
ctime = 10
r = -90
flag = 0
timer_event = pygame.USEREVENT + 1
tick = pygame.time.Clock()
anniu = pygame.transform.scale(pygame.image.load("D:/yysc/anniu1.png"), (120, 80)).convert()
siwang = pygame.transform.scale(pygame.image.load("D:/yysc/siwang.png"), (800, 600)).convert()
dianzan = pygame.transform.scale(pygame.image.load("D:/yysc/dianzan.png"), (200, 200)).convert()
zhizhen = pygame.transform.scale(pygame.image.load("D:/yysc/zhizhen.png"), (60, 200)).convert_alpha()
zhuanpan = pygame.transform.scale(pygame.image.load("D:/yysc/zhuanpan.png"), (400, 99)).convert()
suger1 = pygame.transform.scale(pygame.image.load("D:/yysc/suger1.png"), (200, 200)).convert()
suger2 = pygame.transform.scale(pygame.image.load("D:/yysc/suger2.png"), (200, 200)).convert()
suger3 = pygame.transform.scale(pygame.image.load("D:/yysc/suger3.png"), (200, 200)).convert()
suger4 = pygame.transform.scale(pygame.image.load("D:/yysc/suger4.png"), (200, 200)).convert()
suger5 = pygame.transform.scale(pygame.image.load("D:/yysc/suger5.png"), (200, 200)).convert()
sugers = [suger1, suger2, suger3, suger4, suger5]


#迷宫的变量
flag_renwu = 0

#猜拳的变量
caiquan = pygame.transform.scale(pygame.image.load("D:/yysc/caiquan.png"),(500,100)).convert()
jiandao = pygame.transform.scale(pygame.image.load("D:/yysc/jiandao.png"),(100,100)).convert()
shitou = pygame.transform.scale(pygame.image.load("D:/yysc/shitou.png"),(100,100)).convert()
bu = pygame.transform.scale(pygame.image.load("D:/yysc/bu.png"),(100,100)).convert()
kongbai = pygame.transform.scale(pygame.image.load("D:/yysc/kongbai.png"),(100,100)).convert()
wanjia_quans = [jiandao,shitou,bu,kongbai]
diannao_quans = [jiandao,shitou,bu,kongbai]
diannao = 3
wanjia = 3
wanjia_score = 0
diannao_score = 0
yingderen = 0
huihe = 0
jilu = [0,]
cishu = {'jiandao':[0,0,0],'shitou':[0,0,0],'bu':[0,0,0]}

#宝箱的变量
flag_baoxiang = 0
zhongjiang1 = 0
zhongjiang2 = 0
zhongjiang_flag = 0