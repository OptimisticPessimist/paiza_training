# 組み込み関数
   
`import`なしで使える関数を[組み込み関数](https://docs.python.org/ja/3.6/library/functions.html)と呼ぶ

## よく使う組み込み関数 16選（全部で68個ある内の**16個だけ**！）
- [abs()](https://docs.python.org/ja/3.6/library/functions.html#abs): 絶対値を返す
- [dict()](https://docs.python.org/ja/3.6/library/functions.html#func-dict): 辞書を作って返す
- [input()](https://docs.python.org/ja/3.6/library/functions.html#input): 標準入力から1行を読み込み、受け取った文字列を返す
- [len()](https://docs.python.org/ja/3.6/library/functions.html#len): 要素の数やオブジェクトの長さを返す
- [list()](https://docs.python.org/ja/3.6/library/functions.html#func-list): リストを作って返す
    - `empty_list = list()` と `empty_list = []` は同じ
- [max()](https://docs.python.org/ja/3.6/library/functions.html#max): リストやタプルなどから最大値を返す
- [min()](https://docs.python.org/ja/3.6/library/functions.html#min): リストやタプルなどから最小値を返す
- [pow()](https://docs.python.org/ja/3.6/library/functions.html#pow): `pow(x, y)`で $x^y$ を返す
    - `x ** y` と結果は同じ
- [print()](https://docs.python.org/ja/3.6/library/functions.html#print): 引数の値を出力する
    - キーワード引数`end=`を利用すると改行しない出力ができる<br>
    
    ソースコード
    ```python
    print("a", end="")
    print("b", end="")
    print("c", end="")
    print()
    ```
    出力
    ```
    abc
    ```
    そのままでは行末に改行コードがないので、最後に`print()`で改行コードを足さないと動作確認テストが通らない可能性がある
- [range()](https://docs.python.org/ja/3.6/library/functions.html#func-range): [詳細はここ](https://docs.python.org/ja/3.6/library/stdtypes.html#range)
    - 下記の形で使い分ける(*`range`型は評価されるまで値を出さないので、`list()`でリストに変換している)
    - `range(stop: int)`
        - list(range(3)) -> [0, 1, 2]
    - `range(start, stop)`
        - list(range(1, 3)) -> [1, 2]
    - `range(start, stop, step)`
        - list(range(0, 20, 5)) -> [0, 5, 10, 15]
        - list(range(5, 0, -1)) -> [5, 4, 3, 2, 1]
- [reversed()](): リストやタプル、rangeなどを逆順にする
    - `list(range(5, 0, -1))` と `list(reversed(ranged(1, 6)))` は同じ
    - `reversed_list = original_list[::-1]` でも元のリストを逆順にできる
    ```
    for i in processing_list[::-1]:
        # 処理を書く
    ```
    と書くと`for文`でリストの最後の要素から順に処理することができる
- [set()](https://docs.python.org/ja/3.6/library/functions.html#func-set): 集合型を作って返す
    - **要素の順番を保持しない**ので注意が必要だが、重複を消すことができるので便利
- [sorted()](https://docs.python.org/ja/3.6/library/functions.html#sorted): ソート（並べ替え）をして返す
    - キーワード引数`reverse=`が`False`(デフォルト)なら昇順、`True`なら降順にソートする
- [str()](https://docs.python.org/ja/3.6/library/functions.html#func-str): 文字列に変換して返す
- [sum()](https://docs.python.org/ja/3.6/library/functions.html#sum): リストやタプルなどを左から右へ合計して総和を返す
- [tuple()]: タプル型を作って返す
    - タプルはイミュータブル（変更不可能）なので、あとで変更したい場合はリストを使うこと
    - `sample_tuple = (1, 2)` と `sample_tuple = tuple([1, 2])` は同じ
    - タプルの要素が1つのときは `one_element_tuple = (1, )` と書く必要があるので注意
    - これは `(1, 2)` が `1, 2` とも書けるため
    - 1要素のタプルは `one_element_tuple = 1,` とカンマをつけることでも書ける
- [zip()](https://docs.python.org/ja/3.6/library/functions.html#zip): リストやタプルなどを複数用意して、どれかの要素がなくなるまで要素の最初から順に取り出していく
    
    ソースコード
    ```
    a = [1, 2, 3]
    b = [4, 5, 6, 7]

    result = 0
    for x, y in zip(a, b):
        result += x * y

    print(result)
    ```
    出力
    ```
    32
    ```
    $1 \times 4 + 2 \times 5 + 3 \times 6 = 32$  
    `b`は`a`よりも要素が多いため、`7`は処理されない