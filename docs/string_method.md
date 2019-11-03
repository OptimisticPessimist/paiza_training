## 文字列の処理について  
公式ドキュメントの[4.7. テキストシーケンス型---str](https://docs.python.org/ja/3.6/library/stdtypes.html#text-sequence-type-str)内にある 4.7.1. 文字列メソッド を参照  
`str`型に対して使えるメソッドはここに書いてある  
以下によく使うものを使用例付きで紹介する

1. よく使う文字列メソッド
    - str.**capitalize**(): 文字列strの最初の文字だけ大文字に、残りは小文字にして返す
        ```python
        s = "hello, world!"

        for word in s.split(" "):
            # end=" " と半角スペースを入れないと続けて出力されてしまうので注意
            print(word.capitalize(), end=" ")

        print()

        # -> Hello, World!
        # 各単語の最初の文字だけ大文字にしたいだけなら別に便利なメソッドがある

        ```
    - str.**count**(): 文字列strの中で、引数に指定した文字列と一致する回数を返す
        ```python
        s = "I Say You Say I ♥ You"

        print(s.count("Say"))  # 指定文字列は大文字小文字の区別あり
     
        # -> 2

        ```
    - str.**startswith**(): 文字列strが引数で指定した文字列から始まるなら`True`を、そうでないなら`False`を返す
    - str.**endswith**(): 文字列strが引数で指定した文字列で終わるなら`True`を、そうでないなら`False`を返す
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
    - str.**find**(): 文字列strの中に含まれる引数の文字列が出現する最小のインデックスを返す  
    見つからなければ`-1`を返す。 
        ```
        s = "I hate you."

        if s.find("love") == -1:
            print("You are hated s/he.")
        else:
            print()
        ```