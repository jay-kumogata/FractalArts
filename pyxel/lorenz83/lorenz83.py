# 
# Pyxelを使ってLorenz83 Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# cf. https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 17, 2024 ver.1 (Pyxelで実装)
# Dec 30, 2024 ver.2 (144x144ピクセル，4色で表示)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

def init():
    global grid,size,x,y,z,k,p,n,m,j,t,pal

    # パラメータ
    grid=144
    #grid=512
    size=20
    #size=48

    # 初期値
    x=-0.2
    y=-2.82
    z=2.71
    p={'x':x, 'y':y, 'z':z}

    n=5120 # 計算する数
    m=5120 # 表示する数
    j=0

    k=.002 # 単位時間
    t=0 # 時間

    # 乱択パレット
    pal = [1,rnd.randint(2,5),rnd.randint(6,11),rnd.randint(12,15)]
    
def update():
    """NONE"""
def draw():
    global grid,size,x,y,z,k,p,n,m,j,t,pal

    # 画面クリア
    pyxel.cls(pal[0])

    # 時間経過と回転
    t+=k*10
    u=size*math.cos(t)
    v=size*math.sin(t)
    
    # ループ
    for i in range(n):
        l=(j+i)%n
        o=p
        if (i<=m):
            o['x'],o['y'],o['z']=x,y,z

            # ローレンツアトラクタ(1983)
            a = 0.95
            b = 7.91
            f = 4.83
            g = 4.66
            x,y,z=x+k*(-a*x-y*y-z*z+a*f),\
                y+k*(-y+x*y-b*x*z+g),\
                z+k*(-z+b*x*y+x*z)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[l%3+1])
        
    # 次に進める
    j+=m

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])
    
# メイン
init()
pyxel.init(grid,grid,title="Lorenz83 Attractor")
pyxel.run(update,draw)

# End of lorenz83.py
