## フラクタル芸術作品

### 2022-05-01

Alan Turingという数学者がいます．
彼の大きな業績としては，Turing Machine(計算モデル)，Turing Test(人工知能)，Turing Bombe(暗号解読)が有名です．
そして，晩年のあまり知られていない業績として，Turing Pattern(セルオートマトン)もあります．
とある偏微分方程式を数値的に解くと，自然界で見られる模様が現れるというものです(産業的な応用は現時点では不明です)．
[Python実装](https://ipython-books.github.io/124-simulating-a-partial-differential-equation-reaction-diffusion-systems-and-turing-patterns/)があるので，練習も兼ねて，Pyxelで表示させてみました．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/turing/screenshots/turing01.gif" width="256" />

最初はランダムな状態から開始されています．
時間が経過していくと，島ができてくるのが分かります．
Pyxelでは，パレットが固定されているので，ヒートマップのような表示はできません．
ここでは，負の値は暗い色で，正の値は明るい色で表示されるように工夫しました．
しかしながら，計算機が遅い時代に手で計算してたAlan Turingは，やはり天才です．

Turing Patternsを表示するには，いろいろなモデルがあるようです．
ここでは，元東京大学教授の南雲仁一氏が考案した「FitzHugh–Nagumoモデル」を利用しています．
他にも，「Gray-Scottモデル」等があるようですが，Pyxelの練習ですでので，これ以上は深入りしないことにします．

### 2022-05-02

[Github Wiki](https://github.com/jay-kumogata/FractalArts/wiki/220217_PyxelNote)の方にも転載しました．
また，[ソースコード](https://github.com/jay-kumogata/FractalArts/tree/main/pyxel/turing)も上げました．
一連のtweetsは，絵的には美しくないので，しばらくしたら削除すると思います(ナウシカのセリフではありませんが)．

### 2022-08-16

2022年5月頃に，Pyxelの練習を兼ねて，Turingパターンデモを作りました．
その時には，「FitzHugh-Nagumoモデル」を利用したのですが，「Gray-Scottモデル」という方程式系のデモも作ってみました．
デモの途中で，「ミャクミャク様」のようなパターンも現れます．少し気持ちが悪いです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_spots01.gif" width="256" />
<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_spots02.gif" width="256" />

なお，書籍「作って動かすALife - 実装を通した人工生命モデル理論入門」の[サンプルコード](https://github.com/alifelab/alife_book_src/tree/master/chap02)を参考にさせていただきました．

### 2022-08-17

「Gray-Scottモデル」に与える初期条件を変えると，現れるパターンも変わってきます．
初期条件でバクテリアVと餌Uを配置して，時間経過でバクテリアVがどう増えてくかと考えると分かりやすいかも（本当かな）．
これは「さまよえる泡（Wandering Bubbles）」という名称みたいです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules01.gif" width="256" />

### 2022-08-27

今週も「Gray-Scottモデル」で少し遊んでました．天気予報の降水量のヒートマップを参考にして，少しパレットを変更してみました．与える初期条件も，縞模様（stripe）という名称のものに変更しています．脳味噌みたいなパターンが現れて，これはこれで気持ちが悪いです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_stripe01.gif" width="256" />

### 2022-09-03

「Gray-Scottモデル」に与える初期条件を変えると，現れるパターンも変わってきます．これは「波模様（waves）」という名称みたいです．
マンデルブロも作ったのですが，動きがなくて面白味がないです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_waves01.gif" width="256" />

### 2022-09-11

今週は，「マンデルブロ集合」を表示させてみました．
ズームインとズームアウトも作ってみました．
大昔に博物館で観たCGデモをイメージしてみましたが，少し違う気がします．
Pyxel 1.7.0を利用しています．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/mandelbrot/screenshots/mandelbrot01.gif" width="256" />

### 2022-12-04

科博を訪問しました．ディスカバリトークで，チューリングパタンの講義がありました．子供が多数いましたが，マニアックな内容でした．
終わった瞬間に，親子連れは退出していました（意味不明だったのだと想像します）．
最後に質問して，理解が深まりました．
また，参考書[1]を紹介されました．

参考文献

- [1] 近藤滋: いきもののカタチ　続・波紋と螺旋とフィボナッチ 多彩なデザインを創り出すシンプルな法則, 学研出版 (2021/09/30).
- [2] 三村 昌泰: パターン形成とダイナミクス, 東京大学出版会 (2006/2/28).

以上