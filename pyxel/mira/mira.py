#
# Pyxelを使ってグモウスキー・ミラ写像を表示
#
# Mar 12, 2023 ver.1 (initial release)
#

# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# モデルの各パラメタ(実数)
A = 0.7
B = 0.9998
C = 2.0 - 2.0 * A
X = 0.0
Y = 12.1
W = A * X + C * X * Y / ( 1 + X * X );

# モデルの各パラメタ(整数)
P = 120

# 初期化
u = np.ones((300, 300))

# Pyxel初期化
pyxel.init(300,300, title="mira")

def update():
    global A, B, C, X, Y, Z, U, W, P

    for n in range(P):
        if ( pyxel.frame_count > 10 ):
            x = int(X*10)
            y = int(Y*10)
            u[x  ][y  ] = n % 7 + 8
            u[x+1][y  ] = n % 7 + 8 
            u[x  ][y+1] = n % 7 + 8 
            u[x-1][y  ] = n % 7 + 8 
            u[x  ][y-1] = n % 7 + 8 
            
            Z = X
            X = B * Y + W
            U = X * X;
            W = A * X + C * U / ( 1 + U )
            Y = W - Z

def draw():
    for x in range(300):
        for y in range(300):
            pyxel.pset(x,y,int(u[x,y]) )
        
# メイン
pyxel.run(update, draw)

# end of mira.py
