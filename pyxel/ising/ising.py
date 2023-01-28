# -*- coding: utf-8 -*-
import copy

import numpy as np
#import matplotlib.pyplot as plt
import pyxel

class Ising2D:
    def __init__(self,x=50,y=50,seed=0):
        np.random.seed(seed)
        self.dimx = x
        self.dimy = y
        self.xy = np.random.choice([-1,1],x*y)
        self.xy = self.xy.reshape(x,y)
        self.E = 0
        self.h = 0
        self.J = 1
        self.neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
        self.T = 1

 #   def main(self):
 #       self.MC(500)
        
    def calcE(self,xy):
        E = 0
        for x in range(self.dimx):
            for y in range(self.dimx):
                for neighbor in self.neighbors:
                    nx = (x + neighbor[0]) % self.dimx
                    if(nx < 0):
                        nx = self.dimx
                    ny = (y + neighbor[1]) % self.dimy
                    if(ny < 0):
                        ny = self.dimy
                    E += -self.J*xy[x][y]*xy[nx][ny]
        return E

    def MC(self,loop):
        for i in range(loop):
            mp = np.random.randint(0,self.dimx,2)
            txy = copy.deepcopy(self.xy)
            txy[mp[0],mp[1]] = -txy[mp[0],mp[1]]
            Epre = self.calcE(self.xy)
            Eafter = self.calcE(txy)
            if Eafter < Epre:
                self.xy = txy
            else:
                pro = np.random.random()
                if pro < np.exp(-(Eafter-Epre)/self.T):
                    self.xy = txy
#            self.show(i)
        
#    def show(self,index):
#        fig = plt.figure()
#        ax = fig.add_subplot(111)
#        ax.matshow(self.xy)
#        filename = "ising%05d.png" % (index)
#        plt.savefig(filename)


#if __name__ == "__main__":
#    tmp = Ising2D()
#    tmp.main()

o = Ising2D()

# Pyxel初期化
pyxel.init(50,50, title="ising")

def update():
    global o
#    o.MC(1)
    o.MC(10)

def draw():
    global o
    pyxel.cls(0)
    for x in range(50):
        for y in range(50):
#            c = o.xy[x][y] + 2

            c = 5
            for neighbor in o.neighbors:
                nx = (x + neighbor[0]) % o.dimx
                if(nx < 0):
                    nx = o.dimx
                ny = (y + neighbor[1]) % o.dimy
                if(ny < 0):
                    ny = o.dimy
                if (o.xy[x][y] == o.xy[nx][ny]):
                    c += o.xy[x][y]

            pyxel.pset(x,y,c)

    # 時間表示
    s = ( f"t = {pyxel.frame_count:.2f}\n" )
    pyxel.text(0,0,s,0)

# メイン
pyxel.run(update, draw)

# end of grayscott.py
