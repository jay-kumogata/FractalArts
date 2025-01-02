# 
# Rossler Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 18, 2024 ver.1 (Pyxelで実装)
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
    #grid=512
    size=2
    #size=6
    
    # 初期値
    x=10.0
    y=0.00
    z=10.0
    p={'x':x, 'y':y, 'z':z}

    n=5120 # 計算する数
    m=5120 # 表示する数
    j=0

    k=.015 # 単位時間
    t=0 # 時間
    rad=.025 # 角速度

    # 乱択パレット
    pal = [1,rnd.randint(2,5),rnd.randint(6,11),rnd.randint(12,15)]

def update():
    """NONE"""
def draw():
    global grid,size,x,y,z,k,p,n,m,j,t,rad,pal

    # 画面クリア
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

            # レスラーアトラクタ
            a = 0.2
            b = 0.2
            c = 5.7
            x,y,z=x+k*(-y - z),\
                y+k*(x + a*y),\
                z+k*(b + z*(x-c))

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
pyxel.init(grid,grid,title="Rossler Attractor")
pyxel.run(update,draw)

# End of rossler.py
