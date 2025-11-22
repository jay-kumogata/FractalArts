# 
# Aizawa Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Nov 19, 2025 ver.1 (Pyxelで実装)
# Nov 22, 2025 ver.2 (144x144ピクセル，4色で表示)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

def init():
    global grid,size,x,y,z,k,p,n,t,rad,pal

    # パラメータ
    grid=144
    size=30
    
    # 初期値
    x=0.1
    y=1.00
    z=0.01
    p={'x':x, 'y':y, 'z':z}
    
    n=4096 # 計算する数
    k=.01 # 単位時間

    t=0 # 時間
    rad=.02 # 角速度

    # 乱択パレット
    pal = [1,rnd.randint(2,6),rnd.randint(7,10),rnd.randint(11,15)]

def update():
    """NONE"""
    global grid,size,x,y,z,k,p,n,t,rad,pal
    if pyxel.btn(pyxel.KEY_UP): size += .1
    if pyxel.btn(pyxel.KEY_DOWN): size -= .1
    
def draw():
    global grid,size,x,y,z,k,p,n,t,rad,pal

    # 画面消去
    pyxel.cls(pal[0])

    # 時間経過と回転
    t+=rad
    u=size*math.cos(t)
    v=size*math.sin(t)
    
    # ループ
    for i in range(n):
        o=p
        o['x'],o['y'],o['z']=x,y,z

        # アトラクタ
        a = 0.95
        b = 0.7
        c = 0.6
        d = 3.5
        e = 0.25
        f = 0.1
            
        x,y,z=x+k*((z-b)*x-d*y),\
            y+k*(d*x+(z-b)*y),\
            z+k*(c+a*z-(z*z*z/3)-(x*x+y*y)*(1+e*z)+f*z*x*x*x)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],
                   (grid/2)+size*o['y'],1,pal[1+i%3])
        
    # 次に進める
    #j+=m

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])
    
# メイン
init()
pyxel.init(grid,grid,title="Aizawa Attractor")
pyxel.run(update,draw)

# End of aizawa.py
