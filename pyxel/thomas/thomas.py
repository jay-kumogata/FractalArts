# 
# Thomas Attractorデモを表示
# 「Dynamic Mathematics / Strange Attractors」を参考にしました．
# https://www.dynamicmath.xyz/strange-attractors/
#
# Sep 09, 2024 ver.1 (Pyxelで実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel

# パラメータ
grid=144
size=14

# 初期値
x=0
y=1
z=0
p={'x':x, 'y':y, 'z':z}

n=5120 # 計算する数
m=5120 # 表示する数
j=0

k=.2 # 単位時間
t=0 # 時間

def update():
    """NONE"""
def draw():
    global grid,size,x,y,z,k,p,n,m,j,t

    # GameBoy風パレット
    pal = [1,3,11,14]
    pyxel.cls(pal[0])

    # 時間経過と回転
    t+=k*.1
    u=size*math.cos(t)
    v=size*math.sin(t)
    
    # ループ
    for i in range(n):
        l=(j+i)%n
        o=p
        if (i<=m):
            o['x'],o['y'],o['z']=x,y,z

            # トーマスアトラクタ
            b = 0.208186
            x,y,z=x+k*(math.sin(y)-b*x),\
                y+k*(math.sin(z)-b*y),\
                z+k*(math.sin(x)-b*z)

        # 点描
        pyxel.circ((grid/2)+u*o['x']-v*o['z'],(grid/2)+size*o['y'],1,pal[l%3+1])
        
    # 次に進める
    j+=m

# メイン
pyxel.init(grid,grid,title="Thomas Attractor")
pyxel.run(update,draw)

# End of thomas.py
