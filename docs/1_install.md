## 準備

### 目次
1. Python本体のインストール
1. GitとGitHubアカウントの作成
1. Visual Studio Codeのインストールと設定
1. 開発環境の構築


---
#### 1. Python本体
- Paizaスキルチェックは`3.4.3`を使用しているのでこちらをインストールする（サポート切れなのでその内バージョンアップされるはず）
    - [Windows(64bit版)](https://www.python.org/ftp/python/3.4.3/python-3.4.3.amd64.msi)
    - [Mac](https://www.python.org/ftp/python/3.4.3/python-3.4.3-macosx10.6.pkg)
    - Linux: [ここ](https://www.python.org/downloads/release/python-343/)見て対応して、分からなければ質問ください
- ただしPython 3の最新安定版のバージョンは2019/9/16現在`3.7.4`
    - [Windows(64bit版)](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64-webinstall.exe)
    - [Mac](https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.9.pkg)
    - Linux: [ここ](https://www.python.org/downloads/release/python-374/)見て対応して、分からなければ質問ください
    
- 注意：　Python 3.4では使えない機能の中でテストや競技プログラミングに使いたくなりそうな機能
    - 3.6から
        - f-string
          ```python
          name = "Alice"
          print(f"Hi, {name}! What's up?")  # -> {name}に変数nameの中身である"Alice"が入り "Hi, Alice! What's up?" となる
          ```
        - 変数アノテーション文法
            - `sample_dict: Dict[str, int] = dict()`
        - 数値リテラル内のアンダースコア
            - 桁区切りに使って可読性を上げる（ファイル容量はその分増えることに注意）
            ```python
            want_money = 5_000_000_000_000_000
            print("{:,}円欲しい!!".format(want_money))
            ``` 
        - `enum`の`auto()`    
    - 3.5から
        - `typing`モジュール： コードの見通しを良くするのに使いたい
        - 行列乗算演算子 `@`
        - `dict()`の出力が順不同なので必要に応じて`collections.OrderedDict`を利用する
            - `async`/`await`は利用できるシーンがわからん（シングルスレッドでも使えるけど、非同期処理をどう使えばいいか見えない）

#### 2. GitとGitHubアカウントの作成
1. Gitとは
    - バージョン管理（現在と過去のファイル変更履歴を比較したり）
1．　GitHubとは
    - [GitHub](https://github.com)はGitを利用してコード共有や保管ができるサイト
    - アカウントを作成する
        - プログラマが利用するサービスの認証に使えることがあるアカウントのひとつ
1. ツールのダウンロード
    - [ここから](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
1. (Option) Gitの使い方
    - 時間があるときに[練習サイト](https://learngitbranching.js.org/)を使ってGit操作に慣れるといい
1. (Option) SourceTreeというソフトウェア
    - [SourceTree](https://prog-8.com/blogs/how_to_use_sourcetree)というソフトを使うとGitコマンドを入力せずにマウスクリックだけで操作できる
        - けどコマンドの名前と働きは知っておかないと使えない
        - 最初は`clone`, `pull`, `branch`,  `checkout`, `commit`, `push`が使えたら充分
    - Linuxには対応していないので似たようなものが欲しいなら[GitKraken](https://www.gitkraken.com/)とかいいんじゃないでしょうか
        - 商用する場合はフリーじゃないので注意

#### 3. Visual Studio Codeのインストールと設定
1. インストール
    - [ここからDL](https://code.visualstudio.com/download)
1. 日本語化
    - [ここ参照](https://qiita.com/HiroCh/items/481adfa969dbe689f566)
    - 英語で操作するのが難しいと感じていなくても、他の人と画面をできるだけ合わせる意味で導入
1. Live Shareの有効化
    - [上と似た方法で「VSLiveShare」を検索してインストール](https://qiita.com/mh4gf/items/8f072b2faabba90937d3)
    - ホスト（プログラムを実行するPC）とゲスト（インターネット越しにプログラミングしたりコード読んだりする人）に分かれる
        - 基本的に教える側（私）のPCをホストにするといろんな設定をホストが操作して、面倒なところ以外の本質だけ触れるようにできるはずです
1. GitHubのアカウントでログインする
    - ホストからもらったURLへアクセスするとリモートペアプログラミングが開始できる
    - Microsoftアカウントでも利用できるけど、名前が見えるので本名の人は注意
   
#### 4. 開発環境の構築
1. GitHubのリポジトリから自分のPCに`fork`もしくは`clone`するかzipファイルをダウンロードする
    - `fork`: [ここ](https://github.com/GuitarBuilderClass/Teaching-Assistant-Python)の緑色のボタン（Read the guide)の右下らへんにforkボタンがある
        - 自分のGitHubアカウントにリポジトリが作成される        
    - `clone`: フォルダ/ディレクトリを作りたい場所へ移動してから下記をコピペ
        ```
        git clone https://github.com/GuitarBuilderClass/Teaching-Assistant-Python.git
        git checkout -b <あなたのアカウント名>/feature
        ```
    - DL: Gitがややこしくて使うのが難しいと思ったら[ファイルをダウンロード](https://github.com/GuitarBuilderClass/Teaching-Assistant-Python/archive/master.zip)して解凍してもいいよ
        - Gitを使わないなら以降のGit関連の話すべて無視してね
        - でも仕事ではGitとかSVNとかのツールで管理するのが普通だから覚えると便利
            - `企画書_2(最終版)(決定稿)(改訂版).xlsx.old.コピー(これで提出).xlsx`みたいなの嫌じゃん？
1. `pipenv` のインストールと有効化
    - クローンしたファイルにはPipfileという必要な設定が詰まったファイルが入っているのでpipenvで使えるようにする
        ```
        pip install pipenv
        pipenv install -e .
        pipenv shell
        pipenv install --dev .
        ```
        `pip`もしくは`pipenv`が正しく動かなかったら連絡ください
        - AST関連のパッケージ周辺でエラーが出るけどpytestを使うだけなら支障なさそう？  
        - `-e .` はこの後で出てくるpytestの環境を設定している（setup.pyが裏で動いている）  
        - `--dev .` オプションはdevelop(開発用)のパッケージをインストールするのに必要  
        - その他、何か必要なパッケージがあれば `pipenv install <PACAGE_NAME>`でインストール可能  
            - `pipenv install --dev <PACAGE_NAME>`で開発用環境にだけインストールできる
            - `<PACAGE_NAME>`を`.`と指定すると存在しているPipfileの設定でインストールする
1. インストールの確認
    1. 本体のバージョン確認　　
        ```
        python -V
        ```
        `Python 3.4.3`と出力されたら成功
    1. インストールパッケージの確認
        ```
        pip list
        ```
        
        pytestのバージョンを確認する
        ```
        Package            Version Location
        ------------------ ------- -----------------------------------
        (なんかたくさん)
        pytest             5.0.1
        （なんかたくさん）
        ```
        `5.0.1`以下ならOK
        - VSCodeのリモートペアプログラミング機能にバグがあり、pytestの最新版が使えないため必ず`5.0.1`以下であることを確認する  
    1. gitのブランチを切る
        ```
        git checkout -b <あなたの名前>/<そのブランチでやりたいことが分かりやすい名前>
        ```
        - `clone`した場合は`<自分の名前>/feature/<任意のブランチ名>`は好きに使ってください  
            - 他人のリポジトリや`master`には手を出さないように　　
        - それか自分のアカウントにforkしてください
            - forkしても何か変更する前には`git checkout -b <ブランチ名>`するとミスったとき戻りやすい(参考[GitHub Flow](https://gist.github.com/Gab-km/3705015))
            - リモートの`master`以外のブランチへ`push`してからGitHub上でプルリクエストの依頼をする
                - 依頼先に`GuitarBuilderClass`や教えてくれる人を指定すると、依頼された人がチェックしてコメントくれる仕組み