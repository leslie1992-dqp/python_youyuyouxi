import baoxiang
from collections import Counter
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
    if len(canshu.jilu) == 1:
        canshu.diannan = random.randint(0,2)
    else:
        results = Counter(canshu.jilu)
        max = results.most_common(1)[0][0]
        if max == 0:
            canshu.diannao = 1
        elif max == 1:
            canshu.diannao = 2
        else:
            canshu.diannao = 0


    '''
    if canshu.huihe > 0 :
        if canshu.jilu[canshu.huihe - 1] == 0:
            if canshu.wanjia == 0:
                canshu.cishu['jiandao'][0] += 1
            elif canshu.wanjia == 1:
                canshu.cishu['jiandao'][1] += 1
            else:
                canshu.cishu['jiandao'][2] += 1
        elif canshu.jilu[canshu.huihe - 1] == 1:
            if canshu.wanjia == 0:
                canshu.cishu['shitou'][0] += 1
            elif canshu.wanjia == 1:
                canshu.cishu['shitou'][1] += 1
            else:
                canshu.cishu['shitou'][2] += 1
        elif canshu.jilu[canshu.huihe - 1] == 2:
            if canshu.wanjia == 0:
                canshu.cishu['bu'][0] += 1
            elif canshu.wanjia == 1:
                canshu.cishu['bu'][1] += 1
            else:
                canshu.cishu['bu'][2] += 1

        if canshu.jilu[canshu.huihe - 1] == 0:
            huoqu = canshu.cishu.get('jiandao')
            if huoqu[0] >= huoqu[1] and huoqu[0] >= huoqu[2]:
                max = 0
            elif huoqu[1] >= huoqu[0] and huoqu[1] >= huoqu[2]:
                max = 1
            else:
                max = 2
        elif canshu.jilu[canshu.huihe - 1] == 1:
            huoqu = canshu.cishu.get('shitou')
            if huoqu[0] >= huoqu[1] and huoqu[0] >= huoqu[2]:
                max = 0
            elif huoqu[1] >= huoqu[0] and huoqu[1] >= huoqu[2]:
                max = 1
            else:
                max = 2
        elif canshu.jilu[canshu.huihe - 1] == 2:
            huoqu = canshu.cishu.get('bu')
            if huoqu[0] >= huoqu[1] and huoqu[0] >= huoqu[2]:
                max = 0
            elif huoqu[1] >= huoqu[0] and huoqu[1] >= huoqu[2]:
                max = 1
            else:
                max = 2

        if max == 0:
            canshu.diannao = 1
        elif max == 1:
            canshu.diannao = 2
        elif max == 2:
            canshu.diannao = 0
    else:
        canshu.diannao = random.randint(0,2)
    '''
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