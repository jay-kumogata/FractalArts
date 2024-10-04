# 
# Halvorsen Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 19, 2024 ver.1 (Pyxelで実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

# パラメータ
grid=144
size=4

# 初期値
x=-1.48
y=-1.51
z=2.04
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
    global grid,size,x,y,z,k,p,n,m,j,t,rad
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

            # ハルヴォルセンアトラクタ
            a = 1.89
            x,y,z=x+k*(-a*x-4*y-4*z-y*y),\
                y+k*(-a*y-4*z-4*x-z*z),\
                z+k*(-a*z-4*x-4*y-x*x)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[l%3+1])
        
    # 次に進める
    j+=m

# メイン
pyxel.init(grid,grid,title="Halvorsen Attractor")
pyxel.run(update,draw)

# End of halvorsen.py
