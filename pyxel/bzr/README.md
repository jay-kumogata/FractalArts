# Belousov-Zhabotinsky (BZ) Reaction

## Introduction

Since I found [a Processing implementation](https://discovery.ucl.ac.uk/id/eprint/17241/1/17241.pdf) of the Belousov-Zhabotinski reaction, 
that is introduced in the National Museum of Nature and Science, I ported it to Pyxel/Python. 
This is the result at α=1.2, β=γ=1.0. You can see how the pattern disappears and a circular pattern appears.

![](https://github.com/jay-kumogata/LifeMathematics/raw/main/pyxel/bzr/screenshots/bzr01.gif)

## How to Run

Please execute the following from the Pyxel (version 1.7.0) environment.
Or you can play [here](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.bzr.bzr&packages=numpy).

	> python bzr.py
  
## Remarks

You can see how the pattern stabilizes as time passes. 
Once stabilized, the same pattern appears.
In the real world BZ reaction, the chemical is consumed and it eventually stops.
For the reaction parameters α, β, and γ, I referred to [Qiita's article](https://qiita.com/STInverSpinel/items/a7dcfbde0a08063f4d41).

![](https://github.com/jay-kumogata/LifeMathematics/raw/main/pyxel/bzr/screenshots/bzr02.gif)
