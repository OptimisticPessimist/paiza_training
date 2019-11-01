# coding: utf-8


def judge_hands(card):
    poker = len(set(card))
    if poker == 1:
        return "Four Card"
    elif poker == 2:
        counts = list()
        for c in set(card):
            counts.append(card.count(c))
        if max(counts) == 3:
            return "Three Card"
        else:
            return "Two Pair"
    elif poker == 3:
        return "One Pair"
    else:
        return "No Pair"


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(judge_hands(input()))
