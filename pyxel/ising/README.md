# Ising Model

## Introduction

I made the Ising model, which is indispensable for quantum annealing, into pixel art. 
Since 2-values are plain, 9-values are expressed using the same number of cells as the 4-neighborhood values. 
At first, it's still chaotic. 
I referred to [the article](https://oimokihujin.hatenablog.com/entry/2015/10/30/180435) of "Oimo Kifujin Blog".

<img src="https://github.com/jay-kumogata/LifeMathematics/blob/main/pyxel/ising/screenshots/ising01.gif" width="200">

## How to Run

Please execute the following from the Pyxel (version 1.7.0) environment.
Or you can play [here](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.ising.ising&packages=numpy).

	> python ising.py
  
## Remarks

You can see how it separates into dark blue (spin: -1) and orange (spin: 1) regions over time. 

<img src="https://github.com/jay-kumogata/LifeMathematics/blob/main/pyxel/ising/screenshots/ising02.gif" width="200">

It is completely separated into dark blue (spin: -1) and orange (spin: 1) regions. In the vicinity, the spins are almost aligned.

<img src="https://github.com/jay-kumogata/LifeMathematics/blob/main/pyxel/ising/screenshots/ising03.gif" width="200">
