# 
# Pyxelを使ってAlterd Toroidデモを表示
# 「Altered Toroid (278 chars, code follows)」を参考にしました．
# https://twitter.com/SkyBerron/status/1588293399026843654
#
# Nov 06, 2022 ver.1 (changed graphics library to pyxel)
# Apr 07, 2023 ver.2 (code refactoring)
#
# -*- coding: utf-8 -*-
import pyxel
import math

# Pyxel初期化
pyxel.init(128, 128, title="Toroid", fps=30)

def update():
    """NONE"""

def draw():
    h=64
    pyxel.cls(1)
    
    # 速度: 8→16 (大きくすると遅くなる)
    w=pyxel.frame_count/16           
    a=math.cos(w/4)
    b=math.cos(a)
    c=math.sin(a)

    # 帯長: 40→80 (大きくすると帯が長くなる)
    for i in range(1,80):
        k=i/40
        a=k+w
        n=w%9
        n=min(n,9-n)
        d=math.cos(a)
        e=math.sin(a)
        u=16
        v=0
        f=0
        g=(1+math.cos(n*k+2*w))/h
        
        # 捩り: 20→40 (大きくすると捩りが多くなる)
        for j in range(1,40):        
            for l in range(-1,1,2):
                x=d*u
                y=e*u
                z=l*v
                z,y=c*y+b*z,b*y-c*z+20
                k=h/y
                pyxel.pset(h+k*x,h+k*z,8+i%7)

                u,v=u-math.sin(f),v+math.cos(f)
                f+=g
# メイン
pyxel.run(update, draw)

# End of toroid.py
