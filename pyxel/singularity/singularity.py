# 
# Pyxelを使ってLooking inside the singularityを表示
# 「Looking inside the singularity (267 chars, code follows)」を参考にしました．
# https://twitter.com/SkyBerron/status/1583329400598077440
#
# Apr 16, 2023 ver.1 (PICO-8/LuaからPyxel/Pythonに移植)
#
# -*- coding: utf-8 -*-
import random
import math
import pyxel

m=128

# Pyxel初期化
pyxel.init(256,256,title="Singularity",fps=60)
pyxel.cls(1)

def update():
    """NONE"""
def draw():
    s=pyxel.frame_count
    c=s/128
    d=1.5+math.sin(s/64)
    a=d*math.cos(c)
    b=d*math.sin(c)
    n=s%28
    n=3+min(n,28-n)

    for i in range(0,4800):
        x=random.randint(0,255)
        y=random.randint(0,255)
        u=x/m-1
        v=y/m-1
        u,v=a*u+b*v,a*v-b*u
        d=math.sqrt(u*u+v*v)+.001
        e=m/d-m
        u*=e
        v*=e

        pyxel.pset(x,y,((int(u/4)-int(v/8))%15+1))      # 15色(黒以外)
#        pyxel.pset(x,y,((int(u/4)-int(v/8))%16))        # 16色
#        pyxel.pset(x,y,((int(u/4)-int(v/8))%8+8))       # 8色(明色)
#        pyxel.pset(x,y,((int(u/4)-int(v/8))%8+0))       # 8色(暗色)

# メイン
pyxel.run(update,draw)

# End of singularity.py
