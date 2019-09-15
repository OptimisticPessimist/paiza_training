## 準備

1. Python本体
    - Python 3の最新安定版のバージョンは`3.7.4`
        - [Windows(64bit版)](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64-webinstall.exe)
        - [Mac](https://www.python.org/ftp/python/3.7.4/python-3.7.4-macosx10.9.pkg)
        - Linux: 個別対応します

1. GitとGitHubアカウントの作成
    1. Gitとは
        - バージョン管理（現在と過去のファイル変更履歴を比較したり）
    1. ツールのダウンロード
        - [ここから](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    1. (時間があるときに) Gitの使い方
        - [練習サイト](https://learngitbranching.js.org/)
    1. (便利なツール) SourceTree
        - [SourceTree](https://prog-8.com/blogs/how_to_use_sourcetree)というソフトを使うとGitのコマンドを自分で打たなくていい
            - けどコマンドの名前と働きは知っておかないと使えない
            - 最初は`clone`, `pull`, `branch`,  `checkout`, `commit`, `push`が使えたら充分
        - Linuxには対応していないので[GitKraken](https://www.gitkraken.com/)とかいいんじゃないでしょうか
            - 商用する場合はフリーじゃないので注意

1. 環境構築
    1. GitHubのリポジトリから自分のPCにクローンする
        - フォルダ/ディレクトリを作りたい場所へ移動してから下記をコピペ
            ```
            git clone https://github.com/GuitarBuilderClass/Teaching-Assistant.git
            ```
        Gitがややこしくて使うのが鬱陶しかったら[ファイルをダウンロード](https://github.com/GuitarBuilderClass/Teaching-Assistant/archive/master.zip)して解凍してもいいよ
        - Gitを使わないなら以降のGit関連の話すべて無視してね
        - でも仕事ではGitとかSVNとかで管理するのが普通だから覚えると便利
            - `企画書_2(最終版)(決定稿)(改訂版).xlsx.old.コピー(これで提出).xlsx`とかにならないようにしよう
    1. `pipenv` のインストールと有効化
        - クローンしたファイルにはPipfileという必要な設定が詰まったファイルが入っているのでpipenvで使えるようにする
            ```
            pip install pipenv
            pipenv install -e .
            pipenv shell
            pipenv install --dev .
            ```
            `pip`もしくは`pipenv`が正しく動かなかったら連絡ください  
            - `-e .` はこの後で出てくるpytestの環境を設定するのに必要  
            - `--dev .` オプションはdevelop(開発用)のパッケージをインストールするのに必要  
            - その他、何か必要なパッケージがあれば `pipenv install <PACAGE_NAME>`でインストール可能  
                - `pipenv install --dev <PACAGE_NAME>`で開発用環境にだけインストールできる
                - `<PACAGE_NAME>`を`.`と指定すると存在しているPipfileの設定でインストールする
    1. インストールの確認
        ```
        python -V
        ```
        Python 3.7.x
        と出力されたら成功