# 
# Three-Scroll Unified Chaotic System Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 25, 2024 ver.1 (Pyxelで実装)
# Jan 05, 2025 ver.2 (144x144ピクセル，4色で表示)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

def init():
    global grid,size,x,y,z,k,p,n,m,j,t,rad,pal

    # パラメータ
    grid=144
    size=.3
    
    # 初期値
    x=-0.29
    y=-0.25
    z=-0.59
    p={'x':x, 'y':y, 'z':z}
    
    n=10240 # 計算する数
    m=10240 # 表示する数
    j=0
    
    k=.0001 # 単位時間
    t=0 # 時間
    rad=.025 # 角速度

    # 乱択パレット
    pal = [1,rnd.randint(2,6),rnd.randint(7,10),rnd.randint(11,15)]

def update():
    """NONE"""
    global grid,size,x,y,z,k,p,n,m,j,t,rad,pal
    if pyxel.btn(pyxel.KEY_UP): size += .1
    if pyxel.btn(pyxel.KEY_DOWN): size -= .1
    
def draw():
    global grid,size,x,y,z,k,p,n,m,j,t,rad,pal

    # 画面消去
    pyxel.cls(pal[0])

    # 時間経過と回転
    t+=rad
    u=size*math.cos(t)
    v=size*math.sin(t)
    
    # ループ
    for i in range(n):
        l=(j+i)%n
        o=p
        if (i<=m):
            o['x'],o['y'],o['z']=x,y,z

            # アトラクタ
            a = 32.48
            b = 45.84
            c = 1.18
            d = 0.13
            e = 0.57
            f = 14.7
            
            x,y,z=x+k*(a*(y-x)+d*x*z),\
                y+k*(b*x-x*z+f*y),\
                z+k*(c*z+x*y-e*x*x)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[1+l%3])
        
    # 次に進める
    j+=m

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])
    
# メイン
init()
pyxel.init(grid,grid,title="Three-Scroll Unified Chaotic System Attractor")
pyxel.run(update,draw)

# End of threescroll.py
