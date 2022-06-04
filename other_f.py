import baoxiang
import caiquan
import jiemian
import mi_gong
import mutouren
import zhuanpan
import canshu
import random
import cfg
import pygame
import sys
import baoxiang

#按钮的操做
def fn1():
    jiemian.enddd()

def fn2():
    jiemian.disanguan()

def fn3():
    jiemian.dierguan()

def fn4():
    zhuanpan.zhuanpanyouxi()

def fn5():
    mutouren.mutouren1()

def fn6():
    jiemian.diyiguan()

def fn7():
    mi_gong.migongyouxi(cfg)

def fn8():

    if canshu.flag_renwu == 4:
        canshu.flag_renwu = -1
    canshu.flag_renwu += 1

def fn9():
    jiemian.disiguan()

def fn10():
    caiquan.caiquanyouxi()

def fn11():
    canshu.wanjia = 0


def fn12():
    canshu.wanjia = 1


def fn13():
    canshu.wanjia = 2

def fn_sure():

    canshu.jilu.append(canshu.wanjia)
    '''
    if jilu[huihe] == 0:
        if wanjia ==0:
            cishu['jiandao'][0] += 1
        elif wanjia ==1:
            cishu['jiandao'][1] += 1
        else:
            cishu['jiandao'][2] += 1
    elif jilu[huihe] == 1:
        if wanjia ==0 :
            cishu['shitou'][0] += 1
        elif wanjia == 1:
            cishu['shitou'][1] += 1
        else:
            cishu['shitou'][2] += 1
    elif jilu[huihe] == 2:
        if wanjia == 0:
            cishu['bu'][0] += 1
        elif wanjia == 1:
            cishu['bu'][1] += 1
        else:
            cishu['bu'][2] += 1

    if jilu[huihe] == 0:
        huoqu = cishu.get('jiandao')
        if huoqu[0] >= huoqu[1] and huoqu[0] >= huoqu[2]:
            max = 0
        elif huoqu[1] >= huoqu[0] and huoqu[1] >= huoqu[2]:
            max = 1
        else:
            max = 2
    elif jilu[huihe] == 1 :
        huoqu = cishu.get('shitou')
        if huoqu[0] >= huoqu[1] and huoqu[0] >= huoqu[2]:
            max = 0
        elif huoqu[1] >= huoqu[0] and huoqu[1] >= huoqu[2]:
            max = 1
        else:
            max = 2
    elif jilu[huihe] == 2:
        huoqu = cishu.get('bu')
        if huoqu[0] >= huoqu[1] and huoqu[0] >= huoqu[2]:
            max = 0
        elif huoqu[1] >= huoqu[0] and huoqu[1] >= huoqu[2]:
            max = 1
        else:
            max = 2

    if max == 0:
        diannao = 1
    elif max == 1:
        diannao = 2
    elif max == 2:
        diannao = 0
    '''
    canshu.diannao = 2
    if caiquan.panduan(canshu.wanjia,canshu.diannao) == 0 :
        canshu.huihe += 1
        canshu.wanjia_score += 1
    elif caiquan.panduan(canshu.wanjia,canshu.diannao) == 2:
        canshu.huihe += 1
        canshu.diannao_score += 1
    else:
        canshu.huihe += 1

def fn14():
    jiemian.youxijieshao()

def fn15():

    canshu.flag_baoxiang = 0

def fn16():

    canshu.flag_baoxiang = 1

def fn17():

    canshu.flag_baoxiang = 2

def fn18():

    if canshu.flag_baoxiang == 0:
        canshu.zhongjiang1 = random.randint(1, 2)
        if canshu.zhongjiang1 == 1:
            canshu.zhongjiang2 == 2
        else :
            canshu.zhongjiang2 == 1

    elif canshu.flag_baoxiang == 1:
        seq = [0,2]
        canshu.zhongjiang1 = random.choice(seq)
        if canshu.zhongjiang1 == 0:
            canshu.zhongjiang2 == 2
        else:
            canshu.zhongjiang2 == 0
    else:
        canshu.zhongjiang1 = random.randint(0, 1)
        if canshu.zhongjiang1 == 0:
            canshu.zhongjiang2 == 1
        else:
            canshu.zhongjiang2 == 0

    if canshu.flag_baoxiang == 0:
        canshu.zhongjiang_flag = 0
        baoxiang.zuihouxianshi(canshu.flag_baoxiang, canshu.zhongjiang1, canshu.zhongjiang2)
    elif canshu.flag_baoxiang == 1:
        canshu.zhongjiang_flag = 1
        baoxiang.zuihouxianshi(canshu.zhongjiang1, canshu.flag_baoxiang, canshu.zhongjiang2)
    else:
        canshu.zhongjiang_flag = 2
        baoxiang.zuihouxianshi(canshu.zhongjiang1, canshu.zhongjiang2, canshu.flag_baoxiang)


def fn19():
    print("已完成")

def fn20():
    pygame.quit()
    sys.exit()
def fn21():
    baoxiang.baoxiangyouxi()