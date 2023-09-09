# Pyxelを使ってMandelbrot集合を表示
# 「morikomorou’s blog
# 【python】matplotlibでフラクタル図形(マンデルブロ集合)を描く」を参考にしました．
# https://mori-memo.hateblo.jp/entry/2022/02/08/012422
#
# Sep 11, 2022 ver.1 (Pyxel対応/拡大縮小)
# Sep 09, 2023 ver.2 (上下左右へ移動)
#
# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# 定数
re_center = 0.0           # 実部(中央)
im_center = 0.0           # 虚部(中央)
diam = 4                  # 空間サイズ(実部/虚部)
grid_size = 64            # 表示サイズ[ピクセル]

# マンデルブロ集合の判定
def mandelbrot(max, comp):
    re, im = comp[0], comp[1]
    #実部がre，虚部がimの複素数を作成
    c = complex(re, im)

    #Z_nの初項は0
    z = complex(0, 0)

    for i in range(max):
        z = z*z + c
        #zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z) >= 2:
            return i
    
    return max     #無限大に発散しない場合にはmaxを返す

# Pyxel初期化
pyxel.init(grid_size, grid_size, title="mandelbrot",fps=10)

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

    Mandelbrot = np.zeros(len(comp))

    #マンデルブロ集合に属するかの計算
    for i, c_point in enumerate(comp):
        Mandelbrot[i] = mandelbrot(100, c_point)

    Mandelbrot = Mandelbrot.reshape((grid_size, grid_size))

    # 表示
    for x in range(grid_size):
        for y in range(grid_size):
            c = int(Mandelbrot[x,y]) % 16
            pyxel.pset(y, x, c)

    # 時間表示
    # s = ( f"t = {pyxel.frame_count :.2f}\n" )
    # pyxel.text(0,0,s,1)

# メイン
pyxel.run(update, draw)

# end of mandelbrot.py
