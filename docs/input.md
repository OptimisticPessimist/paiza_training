## 標準入力から文字列を受け取る

### 目次
1. 入力が1行の場合
1. 入力が複数行の場合

#### 1. 入力が1行の場合
標準入力から文字列を受け取るには`input()`関数を使う   
これは数字だろうがなんだろうがstr型で変数に格納される  

|入力|コード|結果|
|:---:|:---|:---|
|abcde|`s = input()`|s = "abcde"|
|abcde|`lst=list(input())`|lst = ["a", "b", "c", "d", "e"]| 
|5|`n = int(input())`|n = 5|
|1 2|`a, b = [int(x) for x in input().split()]`|a = 1, b = 2|
|a b c d e|`lst = input().split()`|lst = ["a", "b", "c", "d", "e"]|
|1 2 3 4 5|`lst = [int(x) for x in input().split()`|lst = [1, 2, 3, 4, 5]|
|abc,def,ghi|`lst = input().split(',')`|lst = ["abc", "def", "ghi"]|

#### 2. 入力が複数行の場合