## やること

1. [準備](./docs/1_install.md)
    1. Python本体のインストール
    1. GitとGitHubアカウントの作成
    1. Visual Studio Codeのインストールと設定
    1. (Option) Gitの使い方を練習
    1. (Option) SourceTree便利
    1. 環境構築

1. [テスト駆動開発(TDD: Test Driven Development)を使ってみよう](./docs/2_tdd.md)
    1. テストを先に書いて、コードは後で書く: なんで？
    1. pytestの使い方： テストコードを使いまわそう
    1. テストケースの作り方: 境界値や大きすぎるデータへの対応
    
1. [標準入力から文字列を受け取る](/docs/3_input.md)
    1. 入力が1行の場合
    1. 入力が複数行の場合

1. テクニック
   1. [よく使う組み込み関数の紹介](docs/built-in_functions.md)
   2. [文字列の処理方法(文字列メソッド)](docs/string_method.md)

1. 問題演習  
    まずは各グループの最後の問題を流し読みして、解けそうか判断してください。  
    解答に詰まったら各グループの問題を最初から順に解くことでヒントになります。  
    時間無制限・調べ放題(できれば公式ドキュメントで)で解答してください。  
    解答コードは`src/`ディレクトリ内、テストコードは`tests/`ディレクトリ内に作成してください

    1. **5以上の整数の合計**  
      if文とループの使い方の復習にちょうど良い問題です。
       1. (<font color="gray">Dランク</font>)[インクリメント](exercise/1_5以上の整数/11D_インクリメント.md)
       2. (<font color="gray">Dランク</font>)[複数行の入力と出力](exercise/1_5以上の整数/12D_複数行の入力と出力.md)
       3. (<font color="gray">Dランク</font>)[配列(リスト)要素の合計](exercise/1_5以上の整数/13D_配列(リスト)要素の合計.md)
       4. (<font color="gray">Dランク</font>)[5以上か4以下か](exercise/1_5以上の整数/14D_5以上か4以下か.md)
       5. (<font color="gray">Dランク</font>)[配列(リスト)データの足し合わせ](exercise/1_5以上の整数/15D_配列(リスト)データの足し合わせ.md)
       6. (<font color="blue">Cランク</font>)[5以上の整数の合計](exercise/1_5以上の整数/16C_5以上の整数の合計.md)
   2. **足すか掛けるか**  
       条件分岐について理解を深める問題です。
       1. (<font color="gray">Dランク</font>)[インクリメント](exercise/2_足すか掛けるか/21D_インクリメント.md) 1-1と同じ問題
       2. (<font color="gray">Dランク</font>)[文字列の出力](exercise/2_足すか掛けるか/22D_文字列の出力.md)
       3. (<font color="gray">Dランク</font>)[文字列の分割](exercise/2_足すか掛けるか/23D_文字列の分割.md)
       4. (<font color="gray">Dランク</font>)[整数の足し算](exercise/2_足すか掛けるか/24D_整数の足し算.md)
       5. (<font color="blue">Cランク</font>)[足すか掛けるか](exercise/2_足すか掛けるか/25C_足すか掛けるか.md)
    3. **文字列を切り取る**  
       文字列操作についての理解を深める問題です。
        1. (<font color="gray">Dランク</font>)[文字列の分割](exercise/3_文字列を切り取る/31D_文字列の分割.md) 2-3と同じ問題
        2. (<font color="gray">Dランク</font>)[整数の足し算](exercise/3_文字列を切り取る/32D_整数の足し算.md) 2-4と同じ問題
        3. (<font color="gray">Dランク</font>)[文字列の長さ](exercise/3_文字列を切り取る/33D_文字列の長さ.md)
        4. (<font color="gray">Dランク</font>)[文字列の1文字目](exercise/3_文字列を切り取る/34D_文字列の1列目.md)
        5. (<font color="gray">Dランク</font>)[あいだの整数](exercise/3_文字列を切り取る/35D_あいだの整数.md)
        6. (<font color="gray">Dランク</font>)[文字列を切り取る](exercise/3_文字列を切り取る/36D_文字列を切り取る.md)
    4. **指定範囲だけ大文字**  
       文字列操作についての理解を深める問題です。
        1. (<font color="gray">Dランク</font>)[文字列の分割](exercise/4_指定範囲だけ大文字/41D_文字列の分割.md) 3-1と同じ問題
        2. (<font color="gray">Dランク</font>)[整数の足し算](exercise/4_指定範囲だけ大文字/42D_整数の足し算.md) 3-2と同じ問題
        3. (<font color="gray">Dランク</font>)[文字列の長さ](exercise/4_指定範囲だけ大文字/43D_文字列の長さ.md) 3-3と同じ問題
        4. (<font color="gray">Dランク</font>)[文字列の1文字目](exercise/4_指定範囲だけ大文字/44D_文字列の1文字目.md) 3-4と同じ問題
        5. (<font color="gray">Dランク</font>)[大文字にする](exercise/4_指定範囲だけ大文字/45D_大文字にする.md)
        6. (<font color="gray">Dランク</font>)[あいだの整数](exercise/4_指定範囲だけ大文字/46D_あいだの整数.md) 3-5と同じ問題
        7. (<font color="blue">Cランク</font>)[指定範囲だけ大文字](exercise/4_指定範囲だけ大文字/47C_指定範囲だけ大文字.md)
    5. **文字の重複カウント**  
       文字列操作についての理解を深める問題です。
        1. (<font color="gray">Dランク</font>)[文字列の長さ](exercise/5_文字の重複カウント/51D_文字列の長さ.md) 4-3と同じ問題
        2. (<font color="gray">Dランク</font>)[文字列の1文字目](exercise/5_文字の重複カウント/52D_文字列の1列目.md) 4-4と同じ問題
        3. (<font color="gray">Dランク</font>)[配列（リスト）の要素の出力](exercise/5_文字の重複カウント/53D_配列（リスト）の要素の出力.md)
        4. (<font color="gray">Dランク</font>)[1文字ずつ出力](exercise/5_文字の重複カウント/54D_1文字ずつ出力.md)
        5. (<font color="gray">Dランク</font>)[文字の重複カウント](exercise/5_文字の重複カウント/55D_文字の重複カウント.md)
    6. **文字列の重複カウント**  
       文字列操作についての理解を深める問題です。
        1. (<font color="gray">Dランク</font>)[文字列の長さ](exercise/6_文字列の重複カウント/61D_文字列の長さ.md)
        2. (<font color="gray">Dランク</font>)[文字列の1文字目](exercise/6_文字列の重複カウント/62D_文字列の1文字目.md)
        3. (<font color="gray">Dランク</font>)[1文字ずつ出力](exercise/6_文字列の重複カウント/63D_1文字ずつ出力.md)
        4. (<font color="gray">Dランク</font>)[文字列の1、2文字目](exercise/6_文字列の重複カウント/64D_文字列の1、2文字目.md)
        5. (<font color="gray">Dランク</font>)[文字列のn文字目とn+1文字目](exercise/6_文字列の重複カウント/65D_文字列のn文字目とn+1文字目.md)
        6. (<font color="blue">Cランク</font>)[文字列の重複カウント](exercise/6_文字列の重複カウント/66C_文字列の重複カウント.md)
    7. **文字と整数の組のソート**  
       配列(リスト)、連想配列(辞書)、ソートなどについて理解を深める問題です。
    8. **文字と整数の組のソート2**  
       配列(リスト)、連想配列(辞書)、ソートなどについて理解を深める問題です。
    9. **アルファベット探し**  
       条件分岐、文字処理について理解を深める問題です。
    10. **五目並べ**  
        2次元配列や文字列の扱いについての腕試し問題です。
    11. **占い**  
        この問題で連想配列(辞書)についての学習成果を確かめましょう。