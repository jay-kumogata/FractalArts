#
# Pyxelを使ってKoch曲線を表示
# 「【python】matplotlibでフラクタル図形(コッホ曲線)を描く」を参考にしました．
# https://mori-memo.hateblo.jp/entry/2022/02/05/172505
#
# Feb 12, 2023 ver.1 (changed graphics library to pyxel)
# Feb 15, 2023 ver.2 (code refactoring)
#

# -*- coding: utf-8 -*-
import numpy as np
import pyxel

import math

th = math.pi * 60 / 180   # 正三角形の角度をラジアン化
a = (0.0, 0.0)
b = (100.0, 0.0)
n = 0  # 繰り返し数
points = [a]  # 各点の座標を入れておくリスト(最終的にこれをプロット)

def koch(a, b, n):
    if n == 0:
        return
    s = (a[0] + (b[0] - a[0]) / 3, a[1] + (b[1] - a[1]) / 3)
    t = (a[0] + (b[0] - a[0]) * 2 / 3, a[1] + (b[1] - a[1]) * 2 / 3)
    u = (s[0] + (t[0] - s[0]) * math.cos(th) - (t[1] - s[1]) * math.sin(th),
         s[1] + (t[0] - s[0]) * math.sin(th) + (t[1] - s[1]) * math.cos(th))
    koch(a, s, n - 1)
    points.append(s)
    koch(s, u, n - 1)
    points.append(u)
    koch(u, t, n - 1)
    points.append(t)
    koch(t, b, n - 1)

# Pyxel初期化
pyxel.init(100, 100, title="koch",fps=1)
def update():
    """NONE"""
def draw():
    pyxel.cls(1)
    global a,b,n,points

    a = (0.0, 0.0)
    b = (100.0, 0.0)
    n += 1  # 繰り返し数
    points = [a]  # 各点の座標を入れておくリスト(最終的にこれをプロット)
    
    koch(a, b, n)
    points.append(b)

    for i in range(len(points)-1):
        x1 = int( points[i][0] )
        y1 = 50 - int( points[i][1] ) 
        x2 = int( points[i+1][0] )
        y2 = 50 - int( points[i+1][1] )
        pyxel.line(x1, y1, x2, y2, 7)

        # カラフルバージョン        
        #for j in range(10):
        #    dy = -20+j*5
        #    c = j+2
        #    pyxel.line(x1, y1+dy, x2, y2+dy, c)

# メイン
pyxel.run(update, draw)

# end of koch.py
