#
# Pyxelを使ってBZ反応を表示
# 「A SIMPLE MODEL OF THE BELOUSOV-ZHABOTINSKY REACTION FROM FIRST PRINCIPLES」
# サンプルコードを参考にしました．
# https://discovery.ucl.ac.uk/id/eprint/17241/1/17241.pdf
#
# Jan 08, 2022 ver.1 (initial release)
#

# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# 濃度配列のサイズ
grid = 100

# 薬品A,B,Cの濃度配列a,b,c
a = np.zeros((grid,grid,2))
b = np.zeros((grid,grid,2))
c = np.zeros((grid,grid,2))

# 時刻t,t+1の指定
p = 0
q = 1

# 反応パラメータ
alpha = 1.2 # α: 薬品A+Bの反応パラメータ
beta  = 1.0 # β: 薬品B+Cの反応パラメータ
gamma = 1.0 # γ: 薬品C+Aの反応パラメータ

# 初期値として乱数を格納
for x in range(grid):
    for y in range(grid):
        a[x][y][p] = np.random.rand()
        b[x][y][p] = np.random.rand()
        c[x][y][p] = np.random.rand()

# Pyxel初期化        
pyxel.init(grid, grid, title="bzr", fps=3)

# 閾値(0.0以上1.0未満)に制限
def constrain(d):
    if d<0.0:
        d=0.0
    elif d>1.0:
        d=1.0
    return d

# シミュレーションステップ
def update():
    global a,b,c,p,q
    for x in range(grid):
        for y in range(grid):
            # あるセル(x,y)と周辺8セルとの平均を求める
            c_a = c_b = c_c = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    i=(i+grid)%grid
                    j=(j+grid)%grid
                    c_a += a[i][j][p]
                    c_b += b[i][j][p]
                    c_c += c[i][j][p]
            c_a /= 9.0
            c_b /= 9.0
            c_c /= 9.0
            a[x][y][q] = constrain(c_a+c_a*(alpha*c_b-gamma*c_c))
            b[x][y][q] = constrain(c_b+c_b*(beta *c_c-alpha*c_a))
            c[x][y][q] = constrain(c_c+c_c*(gamma*c_a-beta *c_b))

    # 時刻t,t+1のインデックスを交換
    if p==0:
        p = 1; q = 0
    else:
        p = 0; q = 1

# 画面描画ステップ
def draw():
    global a,b,c,p,q
    for x in range(grid):
        for y in range(grid):
            # 濃度配列aを表示(パレット1から14まで)
            col = int(a[x][y][q] * 13.0)+1
            pyxel.pset(x, y, col)
    # 時間表示
    s = ( f"t = {pyxel.frame_count:.2f}\n" )
    pyxel.text(0,0,s,0)

# メイン
pyxel.run(update, draw)

# end of bzr.py
            
            
