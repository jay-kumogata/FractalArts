## フラクタル芸術作品（2024年編）

### 2024-07-12

SkyBerron氏の[Energy Flows in Swirls](https://twitter.com/SkyBerron/status/1582370900980080641)をPyxelに写経してみました．
またもや別物になってしまい，お蔵入りしていたのですが，これはこれで面白いので公開します． 

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/energy/screenshots/energy01.gif" width=256 />

### 2024-08-04

Pyxelでジュリア集合をPICO-8仕様(128x128ピクセル，16階調）で描画してみました．[Z][X]キーでズームイン/アウトができます．
「Pythonではじめる数学の冒険」という書籍を参考にしました．ソースコードも公開しました．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/julia/screenshots/julia01.gif)

ジュリア集合について，簡単に説明しておきます．
ジュリア集合というは，次の漸化式

$Z_{n+1} = Z_{n} + C$

で定義される複素数列において $C$ を固定して， $Z_{n}$ の初期値を変化させ $n → ∞$ の極限で無限大に発散しないという条件を満たす複素数 $Z$ 全体が作る集合です．
収束域（ジュリア集合）だけでなく，発散域（その周辺）も無限大に発散する速度（計算回数）を色で描画しています．
また，パラメータ $C$ も表示しています．

### 2024-08-07

Pyxel（64x64ピクセル，4階調）でジュリア集合を描画してみました．矢印キーでパラメータCを変えると，ジュリア集合の形状も変わります．「Pythonではじめる数学の冒険」という書籍を参考にしました．ソースコードも公開しました．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/julia/screenshots/julia02.gif)

### 2024-08-12

128x128ピクセル，4階調(ザナドゥ風)でジュリア集合を描画してみました．
お盆前に，アルフォスのドットを置いていたので，それに触発されました．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/julia/screenshots/julia03.gif)

### 2024-09-01

試行錯誤の結果，13タイトルはブラウザ内で描画できるようになりました．

- [bzr](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.bzr.bzr&packages=numpy)
- [energy](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.energy.energy&packages=numpy)
- [grayscott](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.grayscott.grayscott&packages=numpy)
- [ising](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.ising.ising&packages=numpy)
- [julia](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.julia.julia&packages=numpy)
- [koch](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.koch.koch&packages=numpy)
- [lorenz](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.lorenz.lorenz&packages=numpy)
- [mandelbrot](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.mandelbrot.mandelbrot&packages=numpy)
- [mira](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.mira.mira&packages=numpy)
- [picotron](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.picotron.picotron&packages=numpy)
- [singularity](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.singularity.singularity&packages=numpy)
- [toroid](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.toroid.toroid&packages=numpy)
- [turing](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.turing.turing&packages=numpy)

### 2024-09-09

「ストレンジアトラクタ」の一種である「トーマスアトラクタ」を，Pyxelで描いてみました．
GameBoy仕様を意識して，144x144ピクセル，4色縛りです．
[リンク](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.thomas.thomas)から，ブラウザでも動かせます．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/thomas/screenshots/thomas01.gif)

トーマスアトラクタの常微分方程式は，以下で示されます．

$\dfrac{dx}{dt} = sin(y) - bx$<br>
$\dfrac{dy}{dt} = sin(z) - by$<br>
$\dfrac{dz}{dt} = sin(x) - bz$<br>
$where \ b \ is \ a \ constant.$<br>

パラメータとしては，b = 0.208186，初期条件としては，x = 0，y = 1，z = 0 を与えています．

### 2024-09-11

「ストレンジアトラクタ」の一種である「ダドラスアトラクタ」を，Pyxelで描いてみました．
GameBoy仕様を意識して，144x144ピクセル，4色縛りです．
[リンク](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.dadras.dadras)から，ブラウザでも動かせます．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/dadras/screenshots/dadras01.gif)

ダドラスアトラクタの常微分方程式は，以下で示されます．

$\dfrac{dx}{dt} = y - ax + byz$<br>
$\dfrac{dy}{dt} = cy - xz + z$<br>
$\dfrac{dz}{dt} = dxy - ez$<br>
$where \ a, \ b, \ c, \ d, \ and \ e \ are \ constants.$<br>

パラメータとしては，a=3.0，b=2.7，c=1.7，d=2.0，e=9.0，初期条件としては，x = 0，y = 1，z = 0 を与えています．

### 2024-09-12

「ストレンジアトラクタ」の一種である「チェンアトラクタ」を，Pyxelで描いてみました．
GameBoy仕様を意識して，144x144ピクセル，4色縛りです．
[リンク](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.chen.chen)から，ブラウザでも動かせます．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/chen/screenshots/chen01.gif)

チェンアトラクタの常微分方程式は，以下で示されます．

$\dfrac{dx}{dt} = ay - ax$<br>
$\dfrac{dy}{dt} = (c - a)x - xz + cy$<br>
$\dfrac{dz}{dt} = xy - bz$<br>
$where \ a, \ b, \ and \ c \ are \ constants.$<br>

パラメータとしては，a=5.0，b=-10.0，c=-0.38，初期条件としては，x = -0.1，y = 0.5，z = -0.6 を与えています．

### 2024-09-19

「ストレンジアトラクタ」の一種である「ハルヴォルセンアトラクタ」を，Pyxelで描いてみました．
GameBoy仕様を意識して，144x144ピクセル，4色縛りです．
[リンク](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.halvorsen.halvorsen)から，ブラウザでも動かせます．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/halvorsen/screenshots/halvorsen01.gif)

ハルヴォルセンアトラクタの常微分方程式は，以下で示されます．

$\dfrac{dx}{dt} = -ax - 4y - 4z - y^2$<br>
$\dfrac{dy}{dt} = -ay - 4z - 4x - z^2$<br>
$\dfrac{dz}{dt} = -az - 4x - 4y - x^2$<br>
$where \ a \ is \ a \ constant.$<br>

パラメータとしては，a=1.89，初期条件としては，x = -1.48，y = -1.51，z = 2.04 を与えています．

### 2024-09-20

「ストレンジアトラクタ」の一種である「スプロットアトラクタ」を，Pyxelで描いてみました．
GameBoy仕様を意識して，144x144ピクセル，4色縛りです．
[リンク](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.FractalArts.pyxel.sprott.sprott)から，ブラウザでも動かせます．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/sprott/screenshots/sprott01.gif)

スプロットアトラクタの常微分方程式は，以下で示されます．

$\dfrac{dx}{dt} = y + ay + xz$<br>
$\dfrac{dy}{dt} = 1 - bx^2+yz$<br>
$\dfrac{dz}{dt} = x - x^2 - y^2$<br>
$where \ a \ and \ b \ are \ constants.$<br>

パラメータとしては，a=2.07, b=1.79，初期条件としては，x = 0.63，y = 0.47，z = -0.54 を与えています．

### 2024-11-02

『昔のフォルダを整理していたら』シリーズの第5弾（その6）です．
SkyBerron氏のEnergy Flows in Swirlsを，またPyxelで描いてみました．
GameBoy仕様を意識して，128x128ピクセル，4色縛りにしています．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/energy/screenshots/energy03.gif)

### 2024-11-03

Pyxelで動作するEnergy Flows in Swirlsの
[ソースリスト](https://github.com/jay-kumogata/FractalArts/tree/main/pyxel/energy)
を公開しました．

以上
