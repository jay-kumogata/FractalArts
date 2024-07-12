# 
# Pyxelを使ってEnergy Flows in Swirlsを表示
# 「Energy Flows in Swirls (229 chars, code follows)」を参考にしました．
# cf. https://twitter.com/SkyBerron/status/1582371082517946369
#
# July 12, 2024 ver.1 (PICO-8/LuaからPyxel/Pythonに移植)
#
# -*- coding: utf-8 -*-
import math
import pyxel

def init():
    global h,t,u,v

    h=128
    t=0
    u=0
    v=0

def update():
    """NONE"""
def draw():
    global h,t,u,v
    pyxel.cls(1)
    t+=.05
    for j in range(1,64):
        l=1+j/63
        for i in range(0,256):
            k=i/256
            a=k+l*t
            x=l*math.cos(a)
            y=l*math.sin(a)
            z=math.sin(k+t)
            k=h/(3+y)
            x=h+k*x
            y=h+k*z
            m=j%7+2
            if i>0 and i&m==m:
                pyxel.line(u,v,x,y,1+j%15)
            u=x
            v=y

# メイン
init()
pyxel.init(256,256,title="energy")
pyxel.run(update,draw)

# End of energy.py
