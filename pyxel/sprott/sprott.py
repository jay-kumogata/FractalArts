# 
# Sprott Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 20, 2024 ver.1 (Pyxelで実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

# パラメータ
grid=144
size=42

# 初期値
x=0.63
y=0.47
z=-0.54
p={'x':x, 'y':y, 'z':z}

n=15000 # 計算する数
m=15000 # 表示する数
j=0

k=.001 # 単位時間
t=0 # 時間
rad=.05 # 角速度

# 乱択パレット
pal = [1,rnd.randint(2,6),rnd.randint(7,11),rnd.randint(12,15)]

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

            # スプロットアトラクタ
            a = 2.07
            b = 1.79
            x,y,z=x+k*(y+a*x*y+x*z),\
                y+k*(1-b*x*x+y*z),\
                z+k*(x-x*x-y*y)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],2,pal[l%3+1])
        
    # 次に進める
    j+=m

# メイン
pyxel.init(grid,grid,title="Sprott Attractor")
pyxel.run(update,draw)

# End of sprott.py
