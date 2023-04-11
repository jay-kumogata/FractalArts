# 
# Pyxelを使ってLorenzデモを表示
# 「Lorenz system (274 chars, code follows)」を参考にしました．
# https://twitter.com/SkyBerron/status/1586638426887098371
#
# Apr 11, 2023 ver.1 (changed graphics library to pyxel)
#
# -*- coding: utf-8 -*-
import math
import pyxel

x=0
y=1
z=0
k=.005
p={'x':x, 'y':y, 'z':z-30}
n=32000
m=8000
j=-1
t=0

# Pyxel初期化
pyxel.init(256,256,title="Lorenz Attractor")

def update():
    """NONE"""
def draw():
    global x,y,z,k,p,n,m,j,t
    pyxel.cls(1)
    t+=k
    u=4*math.cos(t)
    v=4*math.sin(t)
    for i in range(1,n):
        l=(j+i)%n+1
        o=p
        if (i<=m):
            # p=10, r=28, b=8/3
            o['x'],o['y'],o['z']=x,y,z-30
            x,y,z=x+k*10*(y-x),y+x*(k*28-k*z)-k*y,z+k*x*y-z*k*8/3
        pyxel.pset(128+u*o['x']-v*o['z'],128+4*o['y'],8+l%8)
    j+=m

# メイン
pyxel.run(update,draw)

# End of lorenz.py

