## フラクタル芸術作品（2023年編）

### 2023-01-06

この前，科博のディスカバリトークで，お話を聞いた時に研究員の方が言っていたBZ反応について，少し調べてみました．
Processingでの実装[3]を，Pythonに移植しようかなと考えています．

BZ反応は，薬品を混ぜることで現実世界に現れるらしいのです．
が，2009年に「結構簡単な数理モデルで再現できます」という論文[2]が発行されています．
その数理モデルをProcessingで実装している模様です．
簡単に説明すると，A，B，Cという薬品があった時に，

	A + B → 2A
	B + C → 2B
	C + A → 2C

という反応をモデル化するだけで，BZ反応を再現できます．

具体的には，離散的な時刻tにおける薬品A，B，Cの濃度a，b，cは，

	a(t+1) = a(t) + a(t) * ( b(t) - c(t) )
	b(t+1) = b(t) + b(t) * ( c(t) - a(t) )
	c(t+1) = c(t) + c(t) * ( a(t) - b(t) )

というように表現できます．
次に，セルオートマトン上の各セルで，濃度a，b，cを計算して，濃度aを諧調で表示します．
すると，BZ反応の模様が現れるようです．
が，モデルをより複雑化して，A + B，B + C，C + Aの反応率α，β，γを導入すると，より複雑なBZ反応の模様が現れるようです．
まだコード化していないので，詳細は不明です．
ちなみに，BZ反応は，「ベロウソフ・ジャボチンスキー反応」が正式名称ですが，毎回言い間違いをしてしまいます．
科博の研究員の方も，正式名称ではなく，「BZ反応」と呼称していました．

参考文献

- [1] STInverSpinel: [BZ反応のシミュレーション](https://qiita.com/STInverSpinel/items/a7dcfbde0a08063f4d41)
- [2] A. Turner: [A simple model of the Belousov-Zhabotinsky reaction from first principles](https://discovery.ucl.ac.uk/id/eprint/17241/1/17241.pdf), 2009. 
- [3] A. Turner: [BZ reaction by Alasdair Turner OpenProcessing](https://openprocessing.org/sketch/1263)

### 2023-01-08

国立科学博物館のディスカバリートークで紹介されたベロウソフ・ジャボチンスキー反応について，Processing実装[3]を発見したので，Pyxel/Pythonに移植してみました．α=1.2，β=γ=1.0での結果です．一旦模様が消えて，円形の模様が現れる様子が分かります．

<img src="https://github.com/jay-kumogata/LifeMathematics/blob/main/pyxel/bzr/screenshots/bzr01.gif" width="256" />

さらに時間が経過すると，模様が安定する様子が分かります．一旦安定すると同じ模様が現れますが，現実のBZ反応では，薬品が消費されて反応は停止するそうです．なお，反応パラメータα，β，γについては，Qiitaの記事[1]を参考にさせていただきました．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/bzr/screenshots/bzr02.gif" width="256" />

### 2023-01-09

BZ反応について，茨城県の女子高生が書いた論文が，米国の物理化学学会の論文誌に掲載されたそうです．
10年以上前の[記事](https://www.chem-station.com/blog/2011/11/post-314.html)ですが，茨城県の女子高生恐るべしです．
さらに時間を経過させても，同じ模様しか現れません．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/bzr/screenshots/bzr03.gif" width="256" />

### 2023-01-20

最近，量子アニーリングで使うイジングモデルを調べています．
量子アニーリングの方は，最近噂を聞きませんが，イジングモデルをピクセルアートにできないかなと考えています．
イジングモデルを，そのままピクセルアート化してみましたが，結構地味な仕上がりにしかなりませんでした．
量子アニーリングについては，日立の[CMOSアニーリング](https://www.hitachi.co.jp/products/it/finance/insights/essay/2109-cmos_01.html)等は継続しているようです．

### 2023-01-24

量子アニーリングには欠かせないイジングモデルをピクセルアートにしてみました．2値だと地味なので，4近傍の値と同じセル数を利用して，9値で表現しています．最初は，まだ混沌とした状態です．「おいも貴婦人ブログ」さんの[記事](https://oimokihujin.hatenablog.com/entry/2015/10/30/180435)を参考にしました．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/ising/screenshots/ising01.gif" width="256" />

### 2023-01-25

イジングモデルの続きです．時間が経過して，紺色(スピン: -1)と橙色(スピン: 1)の領域に分離していく様子が分かります．量子アニーリングについては，加州のD-WAVE社が有名ですが，国内企業(例: 東芝の[シミュレーテッド分岐マシン](https://www.jstage.jst.go.jp/article/vss/63/3/63_20180508/_pdf)等)も研究開発は続けているようです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/ising/screenshots/ising02.gif" width="256" />

### 2023-01-28

イジングモデルの続きです．さらに時間が経過して，紺色(スピン: -1)と橙色(スピン: 1)の領域に完全に分離されています．各セルの近傍では，ほぼスピンが揃った状態です．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/ising/screenshots/ising03.gif" width="256" />

### 2023-02-11

昔書いたソースリストを整理していたら，コッホ曲線を描く[C言語プログラム](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/koch/koch.c)が出てきました．
動きがよく分からないので，Pythonで書き書き直してみることにします．

### 2023-02-12

C言語プログラムの方は，よく分かりませんでした．
Pyxelライブラリで表示してみました．
いわゆるコッホ曲線です．
morikomorou’s blogの[記事](https://mori-memo.hateblo.jp/entry/2022/02/05/172505)を参考にさせていただきました．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/koch/screenshots/koch01.gif" width="256" />

### 2023-03-12

『昔のフォルダを整理していたら』シリーズの第3弾です．
グモウスキー・ミラ写像を描くCソースが出てきたので，Pythonで書き直して，Pyxelで表示させてみました．
金平糖をイメージした色使いにしてみました．
色には数学的な意味はありません．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/mira/screenshots/mira01.gif" width="256" />

### 2023-04-05

リポジトリ名は，[フラクタルアーツ(Fractal Arts)](https://github.com/jay-kumogata/FractalArts)にしました．
本当は，Art（芸術）が正しいことは理解していたんですが，Arts（技法）の方が語感がいいかなと変更しました．
Game Artsに似ているのと，Artworksの省略という理由もあります．
YouTubeでウェザーニュースを見ていて，「[ジェネレーティブアート(Generative Art)](https://ja.wikipedia.org/wiki/%E3%82%B8%E3%82%A7%E3%83%8D%E3%83%AC%E3%83%BC%E3%83%86%E3%82%A3%E3%83%96%E3%82%A2%E3%83%BC%E3%83%88)」という分野があることを知りました．
お天気解説をされている方が，趣味にしているそうです．
そういった意味では，リポジトリ名は，ジェネレーティブアーツ(Generative Arts)の方がふさわしいのかも知れません．

### 2023-04-06

自分には芸術の才能はないのですが，憧憬はあるのでしょう．
その憧憬を数学や理科で解決する手段が，エミュレーション🎮であったり，ジェネリティブアート🎨なのだと考えています．

### 2023-04-07

『昔のフォルダを整理していたら』シリーズの第5弾です．
SkyBerron氏の[Altered Toroid](https://twitter.com/SkyBerron/status/1588293399026843654)をPyxelに写経してみました．
PICO-8とLuaについて，私の知識が不足しており，別物になってしまいました．
お蔵入りしていたのですが，これはこれで面白いので公開します．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/toroid/screenshots/toroid01.gif" width="256" />

### 2023-04-08

オリジナルのAltered Toroidの[リンク](https://twitter.com/SkyBerron/status/1588293399026843654)🔗を記します．
また，Pyxelで動くAltered Toroid🖼️の[ソースリスト](https://github.com/jay-kumogata/FractalArts/tree/main/pyxel/toroid)🧑‍💻も公開しました．

### 2023-04-09

「数式でアートが作れるなら，数式で遊びが作れるのだろうか．」と考えながら散歩をしました．多分できません．数式でできるのは，あくまでシミュレーションまでです．それを遊びにするのは，ホモ・ルーデンスである我々ということなのだと思います．例えば，月面着陸船の挙動を数式で表して，それを月面着陸シミュレーションにすることはできます．でも，それを月面着陸の訓練と思うか，「ルナ・ランダー」という遊びと思うかは，あくまで我々ということです．

そう考えると，数式でアートが作れるというのも，数式でシミュレーション（もしくは，単なる模様）が作れるだけなのです．それを美しい芸術と認識するのは我々ということです．何を芸術と思うか，何を遊びと考えるかを，他のホモ・ルーデンスと共有できれば，それらは芸術や遊びとして成立するということです．「数式で遊びが作れるか．」という奇妙な問いについて，少し考えてみました．

### 2023-04-11

SkyBerron氏の[Lorenz system](https://twitter.com/SkyBerron/status/1586638426887098371)をPyxelに写経してみました．
有名なローレンツアトラクタです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/lorenz/screenshots/lorenz01.gif" width="256" />

### 2023-04-12

このデモのアルゴリズムも理解したので，簡単に説明していきます．
まず，3次元空間(x,y,z)に，ローレンツアトラクタを描画することを考えます．
ローレンツアトラクタは，ローレンツ方程式という常微分方程式の解として与えらえます．
ローレンツ方程式を次に示します．

$\dfrac{dx}{dt} = p(y - x)$<br>
$\dfrac{dy}{dt} = x(r - z) - y$<br>
$\dfrac{dz}{dt} = -bz + xy$<br>
$where \ p = 10, r = 28, b = 8/3$<br>

### 2023-04-13

ローレンツ方程式を数値解析アルゴリズムで解けば，ローレンツアトラクタが描画できることになります．
このデモでは，数値解析アルゴリズムとして，ルンゲクッタ法を用いました．
まず，微小時間 $\Delta t$ が経過した時に， $x,y,z$ がどのように変化するか(変化量)を計算します．
ローレンツ方程式の変化量は，次の式で表されます．

$\Delta x = \Delta t \ p(y - x)$<br>
$\Delta y = \Delta t \ x(r - z) - \Delta t \ y$<br>
$\Delta z = -\Delta t \ bz + \Delta t \ xy$<br>
$where \ p = 10, \ r = 28, \ b = 8/3$<br>

具体的なアルゴリズムを示します．
Pyxelのdraw()関数では，1フレーム分の画面を描画します．
微小時間 $\Delta$ を繰り返し経過させ， $x,y,z$ を漸次的に変化させ，3次元空間に点描する処理を実行しています．

	draw():
	  for i in range(n):
	    x += dt * p * (y - x)
	    y += dt * x * (r - z) - dt * y
	    z += -dt * b * z + dt * x * y
	    pset(x,y,z)

これにより，3次元空間(x,y,z)に，ローレンツアトラクタを描画できます．
ただ，Pyxelでは，pset(x,y,z)のように，3次元空間に直接点描することはできませんので，
3次元座標(x,y,z)を2次元座標(x',y')に変換させてから，点描する必要があります．

### 2023-04-14

さらに，このデモでは，y軸を軸にして，x-z平面を回転させています．
回転角を $\theta$ とすると，3次元座標(x, y, z)から2次元座標(x',y')への変換は，次の式で表されます．

$x' = x \ cos \theta - z \ sin \theta$<br>
$y' = y$<br>

回転角を変数th,回転角の増分(1フレーム分)を変数dthで表すと，具体的なアルゴリズムは，以下のようになります．

	draw():
	  th += dth
	  for i in range(n):
	    x += dt * p * (y - x)
	    y += dt * x * (r - z) - dt * y
	    z += -dt * b * z + dt * x * y
	    pset( x * cos(th) - z * sin(th), y)

### 2023-04-18

SkyBerron氏の[Looking inside the singularity](https://twitter.com/SkyBerron/status/1583329400598077440)をPyxelに写経してみました．
特異点(Singularity)の内部を覗いた様子とのこと．ウルトラセブンのオープニングではないようです．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/singularity/screenshots/singularity01.gif" width="256" />

### 2023-08-19

パレットの値を乱数で決めたら，都度都度カラフルなピクセルアートができるのではないかというアイディアを考案しました．
過去に紹介した「Gray-Scottモデル」の「さまよえる泡（wandering bubbles）」に実装していました．
ただ，さほど印象が変わらないことが判明しました．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules02.gif" width="256" />
<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules03.gif" width="256" />
<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules04.gif" width="256" />
<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules05.gif" width="256" />
<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules06.gif" width="256" />
<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules07.gif" width="256" />

### 2023-08-27

結構有名なマンデルブロ集合です．
Hiroyuki Inou氏の「[マンデルブロート集合とさまざまなジュリア集合](https://www.math.kyoto-u.ac.jp/~inou/opencampus/mandelbrot.pdf)」を参考にしました．

<img src="https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/mandelbrot/screenshots/mandelbrot03.png" width="256" />

### 2023-09-02

以前作成した「マンデルブロ集合」を改良してみました．ズームインとズームアウトに加えて，上下左右に移動できるようにしました．
また，解像度を64x64ピクセルに下げることで，スムーズに移動できるようにしています．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/mandelbrot/screenshots/mandelbrot02.gif)

### 2023-11-10

GameBoy風に，「Gray-Scottモデル」の「さまよえる泡(Wondering Bubble)」を描いてみました．
144x144ピクセル，4色縛りにしてみました．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules08.gif)
![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules09.gif)

### 2023-11-18

続きです．美術館で，同じモチーフで色違いとかがよくあります．私みたいな素人には，よく分からなかったが，あれも，いろいろな色を試している間に，沢山できてしまうのだろうと想像します．自分も同じことをしていると，なんか納得してしまいます．

![](https://github.com/jay-kumogata/FractalArts/blob/main/pyxel/grayscott/screenshots/grayscott_wanderingbubbules10.gif)

以上