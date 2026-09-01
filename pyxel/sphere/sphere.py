#
# 球体デモを表示
#
# Sep 02, 2026 ver.1 (Pyxelで実装)
#
# -*- coding: utf-8 -*-
import math
import pyxel
import random as rnd
import numpy as np

def init():
    global grid,size,screen,p,t,deg,t_x,t_y,t_z,pal

    # パラメータ
    grid=144
    size=20.0
    screen=30.0

    # データの生成（球面座標 (theta, phi) ）
    u = np.linspace(0, 2 * np.pi, 20)
    v = np.linspace(0, np.pi, 20)
    
    # 半径
    r = 1.2

    # 直交座標 (x, y, z) への変換
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    # 球体
    p = np.column_stack((x.flatten(), y.flatten(), z.flatten()))
    
    # 初期値
    t=0    # 時間
    deg=10 # 角速度

    # 回転角度
    t_x=10
    t_y=20
    t_z=30

    # 乱択パレット
    pal = [1,rnd.randint(2,6),rnd.randint(7,10),rnd.randint(11,15)]

def update():
    global grid,size,screen,p,t,deg,t_x,t_y,t_z,pal

    # X軸での回転
    if pyxel.btn(pyxel.KEY_LEFT): t_x -= deg
    if pyxel.btn(pyxel.KEY_RIGHT): t_x += deg

    # Y軸での回転
    if pyxel.btn(pyxel.KEY_UP): t_y -= deg
    if pyxel.btn(pyxel.KEY_DOWN): t_y += deg

    # Z軸での回転
    if pyxel.btn(pyxel.KEY_Z): t_z -= deg
    if pyxel.btn(pyxel.KEY_X): t_z += deg

def draw():
    global grid,size,screen,p,t,deg,t_x,t_y,t_z,pal

    # 画面消去
    pyxel.cls(pal[0])

    # X,Y,Z軸での回転
    q = Rotation_xyz(p, t_x, t_y, t_z)

    # 描画
    for n in range(len(q)-1):
        _x1,_y1=project(q[n][0], q[n][1], q[n][2])
        _x2,_y2=project(q[n+1][0], q[n+1][1], q[n+1][2])

        # 円での描画
        pyxel.circ((grid/2)+_x1*size, (grid/2)+_y1*size, 1, pal[1+n%3])

        # 点での描画
        #pyxel.pset((grid/2)+_x1*size, (grid/2)+_y1*size, pal[1+n%3])

        # 線での描画
        #pyxel.line((grid/2)+_x1*size, (grid/2)+_y1*size, 
        #           (grid/2)+_x2*size, (grid/2)+_y2*size, pal[1+n%3])

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])

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
pyxel.init(grid,grid,title="Sphere demo")
pyxel.run(update,draw)

# End of sphere.py

