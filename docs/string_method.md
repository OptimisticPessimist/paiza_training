## 文字列の処理について  
公式ドキュメントの[4.7. テキストシーケンス型---str](https://docs.python.org/ja/3.6/library/stdtypes.html#text-sequence-type-str)内にある 4.7.1. 文字列メソッド を参照  
`str`型に対して使えるメソッドはここに書いてある  
以下によく使うものを使用例付きで紹介する

### よく使う文字列メソッド
1. 文字を変換するメソッド
    - str.**capitalize()**: 文字列strの最初の文字だけ大文字に、残りは小文字にして返す
    - str.**upper()**: 全ての変換可能な文字を大文字にした文字列を返す
    - str.**lower()**: 全ての変換可能な文字を小文字にした文字列を返す
    - str.**title()**: 文字列strの単語ごとに、変換可能なら大文字から始まって残りを小文字にした文字列を返す
    - str.**swapcase()**: 全ての変換可能な文字の大小を入れ替えた文字列を返す
      ```python
      s = "hello, world!"

      for word in s.split():
          # end=" " と半角スペースを入れないと続けて出力されてしまうので注意
          print(word.capitalize(), end=" ")

      print()
      # -> Hello, World!
      # 各単語の最初の文字だけ大文字にしたいだけならtitle()メソッドを使う

      print(s.upper())  # -> HELLO, WORLD!
      print(s.lower())  # -> hello, world!
      print(s.title())  # -> Hello, World!
      print(s.title().swapcase())  # -> hELLO, wORLD! 

      ```

1. 文字列を変換するメソッド
    - str.**join()**: 文字列strと引数内の文字列または文字列のリスト・タプルなどを結合する
      ```python
      era = ["明治", "大正", "昭和", "平成", "令和"]
      print("→".join(era))

      # -> 明治→大正→昭和→平成→令和
      # ", "で区切られた文字列を作ることができた
      ```
    - str.**split()**: 引数が指定されていなければ空文字（スペースなど）で、指定されていればその文字で文字列strを分割したリストを返す
      ```python
      a, b = "A B".split()
      print(a)  # -> A
      print(b)  # -> B

      print("1-2-3-4-5".split("-"))  # -> [1, 2, 3, 4, 5]

      ``` 
    - str.**strip()**: 文字列strの先頭および末尾部分から引数の文字列を除去したコピーを返す  
      引数が指定されていない場合、空白文字が除去される  
      引数が指定されている場合、その文字の組み合わせすべてが除去される
    - str.**rstrip()**: 文字列strの末尾部分から引数の文字列を除去したコピーを返す  
      引数が指定されていない場合、空白文字が除去される  
      引数が指定されている場合、その文字の組み合わせすべてが除去される
      ```python
      blank_string = "   body   "
      address = "www.example.com"

      print(blank_string.strip())  # -> body
      print(blank_string.rstrip())  # ->    body

      print(address.rstrip("wmco.")) # -> www.example
      print(address.strip("wmco.")) # -> example

      ```


2. 一致する文字列を取り扱うメソッド
    - str.**count()**: 文字列strの中で、引数に指定した文字列と一致する回数を返す
      ```python
      s = "I Say You Say I ♥ You"

      print(s.count("Say"))  # 指定文字列は大文字小文字の区別あり
    
      # -> 2

      # 文字列をlower()で全て小文字に変換すると大小文字の区別なくカウントできる
      print(s.lower().count("y"))  # -> 4 

      ```
    - str.**startswith()**: 文字列strが引数で指定した文字列から始まるなら`True`を、そうでないなら`False`を返す
    - str.**endswith()**: 文字列strが引数で指定した文字列で終わるなら`True`を、そうでないなら`False`を返す
      ```python
      def is_elephant(s: str) -> bool:
          return s.startswith("パオ")

      french = "我々はフランスのJCJKですわ。"
      elephant = "パオはフランスの象パオ。"

      if not is_elephant(french):
          print(f"「{french}」はクラウド女学院生の発言です。")

      if is_elephant(elephant):
          print("象が逃げたぞ射札しろ！！")
      
      ``` 
    - str.**find()**: 文字列strの中に含まれる引数の文字列が出現する最小のインデックスを返す  
      見つからなければ`-1`を返す。 
        ```python
        s = "I hate you."

        index = s.find("love")

        if index == -1:
            print("You are hated.")
        else:
            print(f"love is {index}.")
        
        ```
    - str.**rfind()**: r(右)から`find()`する。つまり文字列strの中に含まれる引数の文字列が出現する最大のインデックスを返す  
      見つからなければ`-1`を返す
    - str.**index()**: `str.find()`と似ているが、一致する文字列が見つからなければ `ValueError` を送出する
    - str.**rindex()**: `str.rfind()`と似ているが、一致する文字列が見つからなければ `ValueError` を送出する
  