# coding: utf-8


def solution(number: int) -> int:
    """
    回答に必要な関数を書く
    必要なら複数作る（分かりやすい名前に書き換えると良い）
    """
    # <角度numberはN角形になる、という計算式を書く>
    return number // 180 + 2


if __name__ == "__main__":
    """
    Pythonが実行されるとき、自分が最初に呼ばれると`__name__`属性が`__main__`になります
    Paizaでも実行時には `if __name__ == "__main__"以下が実行されます
    他のファイルから呼び出された場合はこの部分の処理は無視されます
    """
    number = int(input())
    print(solution(number))
