# Pyxelを使ってJulia集合を表示
#
# 書籍「Pythonではじめる数学の冒険―プログラミングで図解する代数、幾何学、三角関数」を参考にしました．
# https://www.oreilly.co.jp/books/9784873119304/
#
# Aug 04, 2024 ver.1 (Pyxel対応/拡大縮小)
#
# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# 定数
re_center = 0.0           # 実部(中央)
im_center = 0.0           # 虚部(中央)
diam = 4                  # 空間サイズ(実部/虚部)
grid_size = 128            # 表示サイズ[ピクセル]

# ジュリア集合の判定
def julia(max, z, c):
    
    # 引数z,引数cから複素数を作成
    z1 = complex(z[0],z[1])
    c1 = complex(c[0],c[1])
    
    for i in range(max):
        z1 = z1*z1 + c1
        # zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z1) >= 2:
            return i
    
    return max     # 無限大に発散しない場合にはmaxを返す

# Pyxel初期化
pyxel.init(grid_size, grid_size, title="julia",fps=30)

def update():
    global re_center,im_center,diam

    # 画面サイズの1/10だけ上下左右
    if pyxel.btn(pyxel.KEY_LEFT):
        re_center -= diam / 10.0
    if pyxel.btn(pyxel.KEY_RIGHT):
        re_center += diam / 10.0
    if pyxel.btn(pyxel.KEY_DOWN):
        im_center -= diam / 10.0
    if pyxel.btn(pyxel.KEY_UP):
        im_center += diam / 10.0

    # 画面サイズの1%だけ拡大縮小
    if pyxel.btn(pyxel.KEY_Z):
        diam *= 0.99
    if pyxel.btn(pyxel.KEY_X):
        diam /= 0.99

    # 現時点のパラメタ表示（綺麗な箇所を発見した場合に記録）
    if pyxel.btn(pyxel.KEY_SPACE):
        print (re_center, im_center, diam)

# 表示
def draw():
    global re_center,im_center,diam

    # 画面の座標に変換
    re_min = re_center - diam
    re_max = re_center + diam
    im_min = im_center - diam
    im_max = im_center + diam
    
    re = np.linspace(re_min, re_max, grid_size)
    im = np.linspace(im_max, im_min, grid_size)

    #実部と虚部の組み合わせを作成
    Re, Im = np.meshgrid(re, im)
    comp = np.c_[Re.ravel(), Im.ravel()]

    Julia = np.zeros(len(comp))

    #マンデルブロ集合に属するかの計算
    for i, c_point in enumerate(comp):
        #Julia[i] = julia(100, c_point)
        Julia[i] = julia(100, c_point, [-0.4, 0.6])

    Julia = Julia.reshape((grid_size, grid_size))

    # 表示
    for x in range(grid_size):
        for y in range(grid_size):
            c = int(Julia[x,y]) % 16
            pyxel.pset(y, x, c)

# メイン
pyxel.run(update, draw)

# End of julia.py
