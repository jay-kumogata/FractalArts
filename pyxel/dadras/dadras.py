# 
# Dadras Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 11, 2024 ver.1 (Pyxelで実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel

# パラメータ
grid=144
size=4

# 初期値
x=0
y=1
z=0
p={'x':x, 'y':y, 'z':z}

n=5120 # 計算する数
m=5120 # 表示する数
j=0

k=.005 # 単位時間
t=0 # 時間

def update():
    """NONE"""
def draw():
    global grid,size,x,y,z,k,p,n,m,j,t

    # 赤系パレット
    pal = [1,2,8,14]
    pyxel.cls(pal[0])

    # 時間経過と回転
    t+=k*4
    u=size*math.cos(t)
    v=size*math.sin(t)
    
    # ループ
    for i in range(n):
        l=(j+i)%n
        o=p
        if (i<=m):
            o['x'],o['y'],o['z']=x,y,z

            # ダドラスアトラクタ
            a=3.0
            b=2.7
            c=1.7
            d=2.0
            e=9.0
            x,y,z=x+k*(y-a*x+b*y*z),\
                y+k*(c*y-x*z+z),\
                z+k*(d*x*y-e*z)
                    
        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[l%3+1])
        
    # 次に進める
    j+=m

# メイン
pyxel.init(grid,grid,title="Dadras Attractor")
pyxel.run(update,draw)

# End of dadras.py
