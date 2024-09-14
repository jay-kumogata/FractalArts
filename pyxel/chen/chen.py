# 
# Chen Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 12, 2024 ver.1 (Pyxelで実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random

# パラメータ
grid=144
size=3

# 初期値
x=-0.1
y=0.5
z=-0.6
p={'x':x, 'y':y, 'z':z}

n=10240 # 計算する数
m=10240 # 表示する数
j=0

k=.002 # 単位時間
t=0 # 時間

def update():
    """NONE"""
def draw():
    global grid,size,x,y,z,k,p,n,m,j,t

    # Xanadu風パレット
    pal = [1,5,10,12]
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

            # チェンアトラクタ
            alpha=5.0
            beta=-10.0
            delta=-0.38
            x,y,z=x+k*(alpha*x-y*z),\
                y+k*(beta*y+x*z),\
                z+k*(delta*z+x*y/3)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[l%3+1])
        
    # 次に進める
    j+=m

# メイン
pyxel.init(grid,grid,title="Chen Attractor")
pyxel.run(update,draw)

# End of chen.py
