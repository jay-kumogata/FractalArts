# Pyxelを使ってJulia集合を表示
#
# 書籍「Pythonではじめる数学の冒険―プログラミングで図解する代数、幾何学、三角関数」を参考にしました．
# https://www.oreilly.co.jp/books/9784873119304/
#
# Aug 04, 2024 ver.1 (Pyxel対応/拡大縮小)
# Aug 06, 2024 ver.2 (矢印キーでパラメータを操作)
#
# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# 定数
re_center = 0.0           # 中央(実部)
im_center = 0.0           # 中央(虚部)
diam = 2                  # 空間サイズ(実部/虚部)
grid_size = 64            # 表示サイズ[ピクセル]
re_param = -0.4           # パラメータ(実部)
im_param = 0.6            # パラメータ(虚部)

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
pyxel.init(grid_size, grid_size, title="julia",fps=60)

def update():
    global re_center,im_center,diam,re_param,im_param

    # パラメータ(実部/虚部)を変更
    if pyxel.btn(pyxel.KEY_LEFT):
        re_param -= .01
    if pyxel.btn(pyxel.KEY_RIGHT):
        re_param += .01
    if pyxel.btn(pyxel.KEY_DOWN):
        im_param += .01
    if pyxel.btn(pyxel.KEY_UP):
        im_param -= .01

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
    global re_center,im_center,diam,re_param,im_param

    # 画面の座標に変換
    re_min = re_center - diam
    re_max = re_center + diam
    im_min = im_center - diam
    im_max = im_center + diam
    
    re = np.linspace(re_min, re_max, grid_size)
    im = np.linspace(im_max, im_min, grid_size)

    # 実部と虚部の組み合わせを作成
    Re, Im = np.meshgrid(re, im)
    comp = np.c_[Re.ravel(), Im.ravel()]

    Julia = np.zeros(len(comp))

    # ジュリア集合に属するかの計算
    for i, c_point in enumerate(comp):
        Julia[i] = julia(100, c_point, [re_param,im_param])

    Julia = Julia.reshape((grid_size, grid_size))

    # 4色パレット(ゲームボーイ風)
    pal = [1,3,11,14] # 

    # 表示
    for x in range(grid_size):
        for y in range(grid_size):
            #c = int(Julia[x,y]) % 15 + 1
            c = pal[int(Julia[x,y]) % 4]
            pyxel.pset(y, x, c)

    # 時間表示
    s = f"c = {re_param :.2f}"
    if 0 <= im_param: s += "+"
    s += f"{im_param :.2f}i"
    #pyxel.text(0,0,s,7)
    pyxel.text(0,0,s,14)
    
# メイン
pyxel.run(update, draw)

# End of julia.py
