## 条件分岐(if-elif-else)
条件式とは、その式が正しい（`True`）か誤り（`False`)を判定する式のことである  
最初に`True`になった条件式のブロック（同じインデントで行頭が揃っている部分）が実行される
```python=
if True:  # ここに条件式を書く
    print("このブロックが実行される")
    print("ここも実行される")
else:
    print("このブロックは実行されない")
```

- `else`は他の条件が`True`にならなかったときに実行される<br>
    - `else`はなくてもプログラムとしては正しく動作する
- `if`の条件をチェックするのと同時に別の条件もチェックしたい場合、Pythonでは`elif`を使う
    - `elif`は`if`と`else`の間に何個でも使える

### 条件分岐に使う記号
|記号（演算子）|意味|`True`となる例|
|:---:|:---:|:---:|
|==|左右の辺が等しい|3.0 == 3<br>"a" == "a"|
|!=|左右の辺が等しくない|"B" != "b"|
|<|左辺が右辺より小さい|-2 < 10_000|
|<=|左辺が右辺以下|5 <= 5|
|>|左辺が右辺より大きい|3.141 > 2.436|
|>=|左辺が右辺以上|5_000_000_000_000_000 >= 3_000_000|
|in|左辺が右辺に含まれる|"Green" in ["Red", "Green", "Blue"]<br>7 in range(10)|

|その他|意味|x = 7のときに`True`となる例|
|:---:|:---|:---|
|A and B|AとBの両方が`True`なら`True`|(5 < x) and (x <10)|
|A or B|AまたはBのどちらかが`True`なら`True`|(x > 10) or (x < 8)|
|not A|Aではない|not x == 3|
|A not in B|Bの中にAが含まれていない|x not in [1, 2, 3, 4, 5]|


#### 例題1
次のコードの出力結果はどうなるか
```python
num = 3

if num > 5:
    print("A")
elif num < -2:
    print("B")
elif -2 <= num < 4:
    pass
else:
    print("C")
print("D")
```

> 【答え】  
> D  
> 
> 【解説】  
> numが3だから、条件に当てはまるのは`-2 <= num < 4`の部分  
> 範囲が連続している場合は`and`は不要  
> 
> `pass`は何もしない命令なので、`if-elif-else`の外側にある  
> `print("D")`だけが実行される
> 
> `pass`がないと`IndentationError: expected an indented block`となる  
> 本来なら式や命令文が存在するはずのインデントブロックが存在しないためエラーが起きる

#### 例題2
上記のコードで`num = 10`のときは出力結果はどうなるか

> 【答え】  
> A  
> D  

## 繰り返し（ループ処理）
コードは基本的に上から下へ処理されていく  
しかしループを使えばコードの一部・または全部を指定された条件で繰り返すことができる  

### `while`: 条件が`True`の間は処理を続ける
コード例
```python=
count = 0
while count < 6:
    print(count)
    count += 1
print("end")
    
```
出力
> 0  
> 1  
> 2  
> 3  
> 4  
> 5  
> end  

#### 動作の解説
- 1行目で`count`に0が代入される
- 2行目で`while` ループに入る<br>　条件から`count < 6`が`True`の間は同じコードブロックの処理を繰り返す
1. `count`は0なので`while`ループは実行される
    1. `print(count)`で0が出力される
    2. `count += 1`で`count`は1になる
1. `count`は1なので`while`ループは実行される
    1. `print(count)`で1が出力される
    2. `count += 1`で`count`は2になる
1. `count`は2なので`while`ループは実行される
    1. `print(count)`で2が出力される
    2. `count += 1`で`count`は3になる
1. `count`は3ので`while`ループは実行される
    1. `print(count)`で3が出力される
    2. `count += 1`で`count`は4になる
1. `count`は4なので`while`ループは実行される
    1. `print(count)`で4が出力される
    2. `count += 1`で`count`は5になる
1. `count`は5なので`while`ループは実行される
    1. `print(count)`で5が出力される
    2. `count += 1`で`count`は6になる
1. `count`は6なので`count < 6`が`False`になるため、ここで`while`ループは終了する
- `print("end")`でendが出力される

##### 注意
もしも`count += 1`を忘れるとどうなるか  
`while`の終了条件`count < 6`を満たすことが永遠にできないため、永久ループになる  
そのときは`ctrl + C`キーの同時押しでプログラムを強制終了できる

---
### `for`: リストとかの中身がなくなるまで繰り返す
コード例
```python=
animals = ["elephant", "giraffe", "goat", "sheep"]

for animal in animals:
    print(animal)
    
```
出力
> elephant  
> giraffe  
> goat  
> sheep  

上記の例では`list`である`animals`の中身を順に取り出している

指定回数繰り返すときは`range()`を使うのが便利
`range()`はリストではない（ジェネレータと呼ばれるもの）だが、似たように使える

コード例
```python=
# 3回同じことを繰り返す
for _ in range(3):
    print("Hello!")
```
出力
> Hello!  
> Hello!  
> Hello!  

```python=
# 1~5までの自乗数を表示する
for i in range(1, 6):
    print(f"{i}: {i ** i}")
    
```

出力
> 1: 1  
> 2: 4  
> 3: 27  
> 4: 256  
> 5: 3125  

---
#### `break`: ループを中止して抜け出す
`break`を使うとそのループから抜け出すことができる

下記は`while`の項目で書いたコードと同じ出力をするコード
```python=
count = 0
while True:
    if count >= 6:
        print("end")
        break
    print(count)
    count += 1
```
このコードでは`count`が6未満では`count`を出力してから+1する  
`count`が6以上になるとendを出力したあと`break`でループから抜け出す

#### `continue`: 次のループを開始する
`continue`は以降の処理を無視して次の処理を開始する  
1から20までの数で、3の倍数を無視して表示するコードだ
```python=
n = 0

while n <= 20:
    n += 1
    if n % 3 == 0:
        continue
    else:
        print(n)
    
```

出力
> 1  
> 2  
> 4  
> 5  
> 7  
> 8  
> 10  
> 11  
> 13  
> 14  
> 16  
> 17  
> 19  
> 20  