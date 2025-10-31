#
# Clifford Attractorを表示
# 「Joshua Guo's post」を参考にしました
# https://x.com/jshguo/status/1980546634259038538
#
# Oct 22, 2025 ver.1 (Pyxelで実装)
# Oct 27, 2025 ver.2 (アトラクタパラメータを表示)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd
import numpy as np

def init():
    global grid,size,screen,deg,t_x,t_y,t_z,pal
    global x,y,z,k,p,q,n,a,b,c,d
    
    # パラメータ
    grid=144
    size=15
    screen=960

    # 初期値
    x=0
    y=0
    z=0
    p={'x':x, 'y':y, 'z':z}

    n=2048 # 計算する数
    k=.01 # 単位時間
    q=np.full((n,3), 0.0) # 座標群(回転前)
    
    # アトラクタパラメータ(初期値)
    a = -1.4
    b = 1.6
    c = 1.0
    d = 0.7

    # 回転角
    t_x=0
    t_y=0
    t_z=0
    deg=10 # 角速度

    # 乱択パレット
    pal = [1,rnd.randint(2,6),rnd.randint(7,10),rnd.randint(11,15)]

def update():
    global grid,size,screen,deg,t_x,t_y,t_z,pal
    global x,y,z,k,p,q,n,a,b,c,d

    # アトラクタパラメータaを増減
    if pyxel.btn(pyxel.KEY_LEFT): a -= 0.01
    if pyxel.btn(pyxel.KEY_RIGHT): a += 0.01

    # アトラクタパラメータbを増減
    if pyxel.btn(pyxel.KEY_UP): b -= 0.01
    if pyxel.btn(pyxel.KEY_DOWN): b += 0.01

    # アトラクタパラメータcを増減
    if pyxel.btn(pyxel.KEY_Z): c -= 0.01
    if pyxel.btn(pyxel.KEY_X): c += 0.01

    # アトラクタパラメータdを増減
    if pyxel.btn(pyxel.KEY_C): d -= 0.01
    if pyxel.btn(pyxel.KEY_V): d += 0.01    

def draw():
    global grid,size,screen,deg,t_x,t_y,t_z,pal
    global x,y,z,k,p,q,n,a,b,c,d

    # 画面消去
    pyxel.cls(pal[0])

    # ループ
    for i in range(n):
        o=p
        o['x'],o['y'],o['z']=x,y,z
        q[i][0],q[i][1],q[i][2]=x,y,z
        
        # クリフォードアトラクタ
        x,y,z=math.sin(a*y)+c*math.cos(a*x),\
            math.sin(b*x)+d*math.cos(b*y),\
            z
    
    # X,Y,Z軸での回転
    r = Rotation_xyz(q, t_x, t_y, t_z)

    # 点での描画
    for i in range(n):
        _x,_y=project(r[i][0], r[i][1], r[i][2])
        pyxel.circ((grid/2)+_x*size, (grid/2)+_y*size,
                   1, pal[i%3+1])

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])
    
    # アトラクタパラメータを表示
    s = f"a={a:.2f} "
    s += f"b={b:.2f} "
    s += f"c={c:.2f} "
    s += f"d={d:.2f} "
    pyxel.text(16,136,s,pal[3])

# X,Y,Z軸での回転
# 「Deliverate Learning」を参考にしました．
# cf. https://tech-deliberate-jiro.com/pcl-rot/
def Rotation_xyz(pointcloud, theta_x, theta_y, theta_z):
    theta_x = math.radians(theta_x)
    theta_y = math.radians(theta_y)
    theta_z = math.radians(theta_z)
    rot_x = np.array([[ 1,                 0,                  0],
                      [ 0, math.cos(theta_x), -math.sin(theta_x)],
                      [ 0, math.sin(theta_x),  math.cos(theta_x)]])

    rot_y = np.array([[ math.cos(theta_y), 0,  math.sin(theta_y)],
                      [                 0, 1,                  0],
                      [-math.sin(theta_y), 0, math.cos(theta_y)]])

    rot_z = np.array([[ math.cos(theta_z), -math.sin(theta_z), 0],
                      [ math.sin(theta_z),  math.cos(theta_z), 0],
                      [                 0,                  0, 1]])

    rot_matrix = rot_z.dot(rot_y.dot(rot_x))
    rot_pointcloud = rot_matrix.dot(pointcloud.T).T
    return rot_pointcloud

# 疑似3D空間を2D平面に投影
# 「疑似3Dでかんたんアウトラン」を参考にしました．
# cf. https://zenn.dev/sdkfz181tiger/articles/5b96fc307510a3
def project(x, y, z):
    global screen

    # 消失点からスクリーンまでの距離の半分の位置にモデルを置く
    z += screen/2
    
    if z <= 0:
        return 0.0, 0,0
    s = screen / z
    return x*s, y*s

# メイン
init()
pyxel.init(grid,grid,title="Clifford Attractor")
pyxel.run(update,draw)

# End of clifford.py    
