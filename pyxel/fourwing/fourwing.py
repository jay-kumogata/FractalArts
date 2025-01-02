# 
# Four-Wing Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# cf. https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 26, 2024 ver.1 (Pyxelで実装)
# Jan 02, 2025 ver.2 (144x144ピクセル，4色で表示)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

def init():
    global grid,size,x,y,z,k,p,n,m,j,t,rad,pal

    # パラメータ
    grid=144
    size=14

    # 初期値
    x=1.3
    y=-0.18
    z=0.01
    p={'x':x, 'y':y, 'z':z}

    n=5120 # 計算する数
    m=5120 # 表示する数
    j=0
    
    k=.01 # 単位時間
    t=0 # 時間
    rad=.025 # 角速度
    
    # 乱択パレット
    pal = [1,rnd.randint(2,6),rnd.randint(7,10),rnd.randint(11,15)]

def update():
    """NONE"""
    global grid,size,x,y,z,k,p,n,m,j,t,rad,pal
    if pyxel.btn(pyxel.KEY_UP): size += 1
    if pyxel.btn(pyxel.KEY_DOWN): size -= 1
    
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
            a = 0.2
            b = 0.01
            c = -0.4
            x,y,z=x+k*(a*x+y*z),\
                y+k*(b*z+c*y-x*z),\
                z+k*(-z-x*y)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[l%4])
        
    # 次に進める
    j+=m

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])

# メイン
init()
pyxel.init(grid,grid,title="Four-Wing Attractor")
pyxel.run(update,draw)

# End of four_wing.py
