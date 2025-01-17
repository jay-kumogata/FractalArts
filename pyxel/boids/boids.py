# 
# Pyxelを使ってBoidsシミュレーションを表示
# 「作って動かすALife - 実装を通した人工生命モデル理論入門」サンプルコード を参考にしました．
# cf. https://github.com/alifelab/alife_book_src/blob/master/chap04/boids.py
#
# Jan 17, 2024 ver.1 (Pyxel/Pythonに移植)
#
# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import math
import pyxel
import random as rnd

# 初期化
def init():
    global N,COHESION_FORCE,SEPARATION_FORCE,ALIGNMENT_FORCE
    global COHESION_DISTANCE,SEPARATION_DISTANCE,ALIGNMENT_DISTANCE
    global COHESION_ANGLE,SEPARATION_ANGLE,ALIGNMENT_ANGLE,MIN_VEL,MAX_VEL
    global BOUNDARY_FORCE,x,v,dv_coh,dv_sep,dv_ali,dv_boundary,pal
    global t,u_sin,u_cos,pal,grid
    
    # シミュレーションパラメタ
    N = 256
    # 力の強さ
    COHESION_FORCE = 0.008
    SEPARATION_FORCE = 0.4
    ALIGNMENT_FORCE = 0.06
    # 力の働く距離
    COHESION_DISTANCE = 0.5
    SEPARATION_DISTANCE = 0.05
    ALIGNMENT_DISTANCE = 0.1
    # 力の働く角度
    COHESION_ANGLE = np.pi / 2
    SEPARATION_ANGLE = np.pi / 2
    ALIGNMENT_ANGLE = np.pi / 3
    # 速度の上限/下限
    MIN_VEL = 0.005
    MAX_VEL = 0.03
    # 境界で働く力（0にすると自由境界）
    BOUNDARY_FORCE = 0.001
    
    # 位置と速度
    x = np.random.rand(N, 3) * 2 - 1
    v = (np.random.rand(N, 3) * 2 - 1 ) * MIN_VEL
    
    # cohesion, separation, alignmentの３つの力を代入する変数
    dv_coh = np.empty((N,3))
    dv_sep = np.empty((N,3))
    dv_ali = np.empty((N,3))
    # 境界で働く力を代入する変数
    dv_boundary = np.empty((N,3))

    # 回転
    t = 0
    
    # 乱択パレット
    pal = [1,rnd.randint(2,5),rnd.randint(6,11),rnd.randint(12,15)]
    grid = 144

def update():
    global N,COHESION_FORCE,SEPARATION_FORCE,ALIGNMENT_FORCE
    global COHESION_DISTANCE,SEPARATION_DISTANCE,ALIGNMENT_DISTANCE
    global COHESION_ANGLE,SEPARATION_ANGLE,ALIGNMENT_ANGLE,MIN_VEL,MAX_VEL
    global BOUNDARY_FORCE,x,v,dv_coh,dv_sep,dv_ali,dv_boundary,pal
    global t,u_sin,u_cos,pal,grid

    for i in range(N):
        # ここで計算する個体の位置と速度
        x_this = x[i]
        v_this = v[i]
        # それ以外の個体の位置と速度の配列
        x_that = np.delete(x, i, axis=0)
        v_that = np.delete(v, i, axis=0)
        # 個体間の距離と角度
        distance = np.linalg.norm(x_that - x_this, axis=1)
        angle = np.arccos(np.dot(v_this, (x_that-x_this).T) / (np.linalg.norm(v_this) * np.linalg.norm((x_that-x_this), axis=1)))
        # 各力が働く範囲内の個体のリスト
        coh_agents_x = x_that[ (distance < COHESION_DISTANCE) & (angle < COHESION_ANGLE) ]
        sep_agents_x = x_that[ (distance < SEPARATION_DISTANCE) & (angle < SEPARATION_ANGLE) ]
        ali_agents_v = v_that[ (distance < ALIGNMENT_DISTANCE) & (angle < ALIGNMENT_ANGLE) ]
        # 各力の計算
        dv_coh[i] = COHESION_FORCE * (np.average(coh_agents_x, axis=0) - x_this) if (len(coh_agents_x) > 0) else 0
        dv_sep[i] = SEPARATION_FORCE * np.sum(x_this - sep_agents_x, axis=0) if (len(sep_agents_x) > 0) else 0
        dv_ali[i] = ALIGNMENT_FORCE * (np.average(ali_agents_v, axis=0) - v_this) if (len(ali_agents_v) > 0) else 0
        dist_center = np.linalg.norm(x_this) # 原点からの距離
        dv_boundary[i] = - BOUNDARY_FORCE * x_this * (dist_center - 1) / dist_center if (dist_center > 1) else 0
    # 速度のアップデートと上限/下限のチェック
    v += dv_coh + dv_sep + dv_ali + dv_boundary
    for i in range(N):
        v_abs = np.linalg.norm(v[i])
        if (v_abs < MIN_VEL):
            v[i] = MIN_VEL * v[i] / v_abs
        elif (v_abs > MAX_VEL):
            v[i] = MAX_VEL * v[i] / v_abs
    # 位置のアップデート
    x += v

    # 時間経過(Y軸中心での座標回転)
    t += 0.02
    u_sin = math.sin(t)
    u_cos = math.cos(t)
    
def draw():
    global N,COHESION_FORCE,SEPARATION_FORCE,ALIGNMENT_FORCE
    global COHESION_DISTANCE,SEPARATION_DISTANCE,ALIGNMENT_DISTANCE
    global COHESION_ANGLE,SEPARATION_ANGLE,ALIGNMENT_ANGLE,MIN_VEL,MAX_VEL
    global BOUNDARY_FORCE,x,v,dv_coh,dv_sep,dv_ali,dv_boundary,pal
    global t,u_sin,u_cos,pal,grid

    # 画面消去
    pyxel.cls(pal[0])
    
    # すべてのboidsを表示
    for n in range(N):
        _x = x[n][0]; _px = _x - v[n][0]
        _y = x[n][1]; _py = _y - v[n][1]
        _z = x[n][2]; _pz = _z - v[n][2]
        pyxel.line((grid/4)*(u_cos*_x-u_sin*_z)+(grid/2), (grid/4)*_y+(grid/2),
                   (grid/4)*(u_cos*_px-u_sin*_pz)+(grid/2), (grid/4)*_py+(grid/2),
                   pal[n%3+1])

    # 色見本
    pyxel.circ(8,8,4,pal[0])
    pyxel.circ(20,8,4,pal[1])
    pyxel.circ(32,8,4,pal[2])
    pyxel.circ(44,8,4,pal[3])

# メイン
init()
pyxel.init(grid,grid,title="Boids")
pyxel.run(update,draw)

# End of boids.py
