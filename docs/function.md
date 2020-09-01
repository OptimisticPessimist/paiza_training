## 関数
- 関数は再利用できるコードのかたまり
- テストコードからも利用するが、下記の流れが進めやすい
    - 一度にすべての処理をしようとせず、段階的にデータを変換する
    - 変換したデータをテストで確認する
    - 最後にまとめて変換して、入力と結果が期待通りか確認する

### def
Pythonの関数は`def`キーワードで定義する
下ではint型の`a`, `b`を足してint型の値を返す`add()`関数を作る

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `def`: 関数を定義するキーワード  
- `add()`:　関数名  
- `a: int`, `b: int`: int型の引数だという型ヒント
    - 引数を2つ指定しているので、`add()`は2つの引数を指定しないといけない
    - 引数が1つ（不足）や3つ以上（超過）では動作しない
- `-> int:` : 戻り値がint型の関数だという型ヒント
- `return`: 関数を利用した場所に渡す値

Paizaでも型ヒントが使えるようになったが、型のあるコードは保守性が高くなりやすい（メンテナンスしやすい）ので、**型ヒントは書かなくてもいいけど、書いた方がエンジニア（未来の同僚）からのウケは良い**という実感がある  
型のある言語（JavaとかTypeScriptとか）にも移行しやすくなると思うし

関数は外の変数の変化から影響を受けないし、中の変数の変化で外へ影響を与えることもできない  
引数で外から値を受け取り、`return`で戻り値を元のコードへ渡すことができる  

実際に`add()`を使ってみる

```python
def add(a: int, b: int) -> int:
    return a + b


a = 2
b = 3
c = 5

d = add(a, b)
e = add(c, d)

print(e)

```

出力
> 10

`add(a, b)`で`c`には`2 + 3 = 5`が代入される  
`add(c, d)`で`d`には`5 + 5 = 10`が代入される

#### 応用
先述の`add()`は2変数でしか使えないが、int型のListに対応できるようにしてみよう  
型ヒントで`List`や`Dict`などを使うときは`from typing import `で呼び出しが必要

```python
from typing import List


def add(int_list: List[int]) -> int:
    result: int = 0
    for n in int_list:
        result += n
    return result
    

i_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(add(i_list))

```

出力
> 55


関数は同じ処理が複数箇所にあるとき、処理をまとめるために使うことも多い  
スキルチェックでは時間制限があるのでそこまで考える時間はないかもしれないが、実務では是非似た処理はひとつの関数にまとめていってほしい

---
### スコープ
関数の中と外では同じ変数名でも別々の値としてデータを扱っている  
たとえば、次のコードでは関数内の変数を関数外から直接使おうとしているが、関数内の処理を関数外から直接参照できないので、変数が未定義(`NameError`)だというエラーが出る

```python
def dummy_function() -> None:
    cant_callable_variable = 810
    
 
print(cant_callable_variable)

```

出力
> Traceback (most recent call last):  
>   File "<input>", line 5, in <module>  
> NameError: name 'cant_callable_variable' is not defined
    
関数内の処理を関数外で使いたいときは`return`を使うか、後述予定のクラス(`class`）で属性として扱う

```python
def dummy_function() -> int:
    return 33 - 4
    
print(dummy_function())

```

出力
> 29


---
#### 消費税を計算しよう
今は令和元年9月30日  
たろう君はコンビニで110円（税抜）のおにぎりを買いました。
次にたろう君はスーパーでワンカップ大関を198円（税別）で買います。  
たろう君はそれぞれのお店でいくら支払うでしょうか

関数を使わないコード

```python
from math import floor

print(f"たろう君はコンビニで{floor(110 * 1.08)}円つかいました")
print(f"たろう君はスーパーで{floor(198 * 1.08)}円つかいました")

```

出力
> たろう君はコンビニで118円つかいました  
> たろう君はスーパーで213円つかいました

消費税計算は同じ処理をしていますね  
関数にまとめてみましょう

```python
from math import floor


def calc_tax(price: int) -> int:
    return floor(price * 1.08)
    

print(f"たろう君はコンビニで{calc_tax(110)}円つかいました")
print(f"たろう君はスーパーで{calc_tax(198)}円つかいました")

```

出力省略

さて、令和元年10月1日になりました  
消費税が8%から10％になり、軽減税率も導入されました

最初のコードではすべてを手で直さなくてはいけませんが、関数化している場合は関数を手直しするだけで大丈夫です

たろう君はコンビニで110円（税抜）のおにぎりを持ち帰りで買います  
帰りにたろう君は中華屋でチューハイ大ジョッキ298円（税抜）と餃子348円（税抜）とラーメン640円（税抜）を店内で食べようと注文します

`calc_tax()`関数を軽減税率の対象かどうかも含めて対応できるように変更してみましょう

```python
from math import floor


def calc_tax(price: int, is_reduced_tax: bool) -> int:  # 関数のデフォルト値
    if is_reduced_tax:
        return floor(price * 1.08)
    else:
        return floor(price * 1.1)


print(f"たろう君はコンビニで{calc_tax(110, True):,d}円つかいました")
print(f"たろう君は中華屋で{calc_tax(298 + 348 + 648, False):,d}円つかいました")  # {<数値>:,d}は3桁区切りでカンマを入れる記号

```

出力
> たろう君はコンビニで118円つかいました  
> たろう君は中華屋で1,423円つかいました

`calc_tax()`の引数 `is_reduced_tax`によって税率計算が切り替わっている  
この他にも、`1.08`や`1.1`が一見して何を表す数字か分からないため、変数（定数）として扱ってコメントがなくてもわかるようにする方法もある

```python
from math import floor

NORMAL_TAX_RATE = 1.1
REDUCED_TAX_RATE = 1.08

def calc_tax(price: int, is_reduced_tax: bool) -> int:  # 関数のデフォルト値
    if is_reduced_tax:
        return floor(price * REDUCED_TAX_RATE)
    else:
        return floor(price * NORMAL_TAX_RATE)
        
```

定数は大文字をアンダースコアで繋げて命名するのがPython流  
`price`に掛けているのが`REDUCED_TAX_RATE`なのか`NORMAL_TAX_RATE`なのか、コードから何の計算をしているか分かりやすい  
また~~考えたくないけど~~税率が変わったときもそれぞれの定数の数値を変えるだけで基本的には改修が終わるはずなので楽になる