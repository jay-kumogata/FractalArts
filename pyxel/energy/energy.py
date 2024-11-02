# 
# Pyxelを使ってEnergy Flows in Swirlsを表示
# 「Energy Flows in Swirls (229 chars, code follows)」を参考にしました．
# cf. https://twitter.com/SkyBerron/status/1582371082517946369
#
# Jul 12, 2024 ver.1 (PICO-8/LuaからPyxel/Pythonに移植)
# Oct 30, 2024 ver.2 (128x128ピクセル，4色で表示)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd

def init():
    global h,t,u,v,pal

    h=64
    t=0
    u=0
    v=0

    # 乱択パレット
    pal = [1,rnd.randint(2,5),rnd.randint(6,11),rnd.randint(12,15)]

def update():
    """NONE"""
def draw():
    global h,t,u,v,pal
    pyxel.cls(1)
    t+=.05
    for j in range(1,64):
        l=1+j/63
        for i in range(0,128):
            k=i/128
            a=k+l*t
            x=l*math.cos(a)
            y=l*math.sin(a)
            z=math.sin(k+t)
            k=h/(3+y)
            x=h+k*x
            y=h+k*z
            m=j%7+2
            if i>0 and i&m==m:
                pyxel.line(u,v,x,y,pal[1+j%3])
            u=x
            v=y
    
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])
            
# メイン
init()
pyxel.init(128,128,title="energy")
pyxel.run(update,draw)

# End of energy.py
