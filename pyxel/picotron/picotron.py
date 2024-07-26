# 
# Pyxelを使って「Picotronのデモ」を表示
# https://twitter.com/euphoria6611/status/1810718359035773350
#
# jul 26, 2024 ver.1 (PICO-8/LuaからPyxel/Pythonに移植)
#
# -*- coding: utf-8 -*-
import random
import math
import pyxel

def update():
    """NONE"""
def draw():
    pyxel.cls(0)
    for y in range(-20, 240, 12):
        for x in range(-20, 240, 4):
            dx = x - 120
            dy = y - 120
            dd = math.sqrt(dx*dx + dy*dy)
            t = pyxel.frame_count
            q = math.sin(dd/40 - t/8)*24
            pyxel.circ(40+x+q, 40+y-q, 1, 8+int(dd/8)%8)

# メイン
pyxel.init(320, 320, title="picotron", fps=20)
pyxel.run(update, draw)

# End of picotron.py
