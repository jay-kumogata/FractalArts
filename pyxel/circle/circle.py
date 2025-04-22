import pyxel
import math
import random

class App:
    def __init__(self):
        pyxel.init(500, 500, title="Buzz of circle", fps=10)
        self.f = 0
        # ノイズ用のグリッドを初期化
        self.grid_size = 30
        self.noise_grid = {}
        pyxel.run(self.update, self.draw)

    def update(self):
        self.f += 1

    def smooth_noise(self, x, y):
        """簡易的な2Dノイズ生成"""
        # グリッド座標
        grid_x = int(x // self.grid_size)
        grid_y = int(y // self.grid_size)
        
        # グリッド上のランダム値（キャッシュ使用）
        def get_random_val(gx, gy):
            key = (gx, gy)
            if key not in self.noise_grid:
                self.noise_grid[key] = random.random()
            return self.noise_grid[key]

        # 周囲4点の値を取得
        v00 = get_random_val(grid_x, grid_y)
        v10 = get_random_val(grid_x + 1, grid_y)
        v01 = get_random_val(grid_x, grid_y + 1)
        v11 = get_random_val(grid_x + 1, grid_y + 1)

        # グリッド内での相対位置
        fx = (x % self.grid_size) / self.grid_size
        fy = (y % self.grid_size) / self.grid_size

        # 滑らかな補間（cosine interpolation）
        def interpolate(a, b, t):
            ft = (1 - math.cos(t * math.pi)) * 0.5
            return a * (1 - ft) + b * ft

        # 2D補間
        top = interpolate(v00, v10, fx)
        bottom = interpolate(v01, v11, fx)
        return interpolate(top, bottom, fy)

    def draw(self):
        pyxel.cls(1)
        
        for x in range(0, 500, 9):
            for y in range(0, 500, 9):
                r = math.sqrt((250 - x) ** 2 + (250 - y) ** 2)
                i = math.atan2(y - 250, x - 250)
                # 位置に基づく滑らかなノイズ
                noise_val = self.smooth_noise(x / 30, y / 30)
                color_val = int(15 * noise_val * (math.sin((self.f + r * r) / 30 + i) + 1))
                color_val = min(max(color_val, 0), 15)
                pyxel.rect(x, y, 7, 7, color_val)

App()

# End of circle.py
