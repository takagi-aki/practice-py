#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""stable_sort.py: 安定ソート確認"""

__author__ = "Akinari Takagi"

from typing import Iterable
from double_linked_list import DoubleLinkedList


class Card:

    def __init__(self, card_str) -> None:
        self.str = card_str
        self.value = int(card_str[1:])
        self.suit = card_str[0]

    def __repr__(self) -> str:
        return self.str

    def __lt__(self, other):
        return self.value < other.value


def is_stable(d1: Iterable[Card], d2: Iterable[Card]):

    # 数字ごとの記号の並びを保存する領域確保
    suit_order = [DoubleLinkedList() for i in range(10)]

    # 数字ごとの記号の並びを記録する
    for x in d1:
        suit_order[x.value].append(x.suit)

    # 数字ごとの記号の並びで最初のものを確認し
    # 異なっていたら安定ソートでない
    # 同じであったら記号の並びから一番最初を削除する
    # すべてのカードで問題がなければ安定ソート判定
    for y in d2:
        d1_suit = suit_order[y.value].index(0)
        if(d1_suit != y.suit):
            return False
        suit_order[y.value].popleft()

    return True


def stable_sort(values: Iterable[Card]):
    """標準listを利用した安定ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する
    安定ソートであるかどうかも出力する

    Example:
        >>> test1 = list(map(Card,['H4', 'C9', 'S4', 'D2', 'C3']))
        >>> stable_sort(test1)
        stable sort
        D2 C3 H4 S4 C9
        Stable
        D2 C3 S4 H4 C9
        Not stable
        >>> test2 = list(map(Card, ['S1', 'H1']))
        >>> stable_sort(test2)
        stable sort
        S1 H1
        Stable
        S1 H1
        Stable
    """

    print('stable sort')
    buffer = list(values)
    for i in range(len(buffer)):
        for j in range(len(buffer)-1, i, -1):
            if(buffer[j].value < buffer[j - 1].value):
                buffer[j - 1], buffer[j] = buffer[j], buffer[j - 1]

    print(' '.join(map(str, buffer)))
    if is_stable(values, buffer):
        print('Stable')
    else:
        print('Not stable')

    buffer = list(values)
    for i in range(len(buffer)):
        min_val = buffer[i]
        min_index = i
        for j in range(i, len(buffer)):
            if(buffer[j].value < min_val.value):
                min_val = buffer[j]
                min_index = j
        buffer[min_index], buffer[i] = buffer[i], buffer[min_index]

    print(' '.join(map(str, buffer)))
    if is_stable(values, buffer):
        print('Stable')
    else:
        print('Not stable')


def doublelinkedlist_stable_sort(values: Iterable[Card]):
    """DoubleLinkedListを利用した安定ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する
    安定ソートであるかどうかも出力する

    Example:
        >>> test1 = list(map(Card,['H4', 'C9', 'S4', 'D2', 'C3']))
        >>> doublelinkedlist_stable_sort(test1)
        doublelinkedlist stable sort
        D2 C3 H4 S4 C9
        Stable
        D2 C3 H4 S4 C9
        Stable
        >>> test2 = list(map(Card, ['S1', 'H1']))
        >>> doublelinkedlist_stable_sort(test2)
        doublelinkedlist stable sort
        S1 H1
        Stable
        S1 H1
        Stable
    """

    print('doublelinkedlist stable sort')

    is_not_sorted = True
    buffer = DoubleLinkedList(values)

    while(is_not_sorted):
        is_not_sorted = False
        try:
            # イテレータがリストの有効な範囲にあるか確認する用。ループの初めにprevする
            it_check = buffer.iterator(-1)
            it_left = buffer.iterator(-1)   # 隣接する値の左を示すイテレータ
            it_right = buffer.iterator(-1)  # 隣接する値の右を示すイテレータ
            it_check.prev()
            it_left.prev()
            while True:
                it_check.prev()
                if it_right.value.value < it_left.value.value:
                    is_not_sorted = True
                    it_right.value, it_left.value = it_left.value, it_right.value
                it_left.prev()
                it_right.prev()
        except StopIteration:
            pass

    print(' '.join(map(str, buffer)))
    if is_stable(values, buffer):
        print('Stable')
    else:
        print('Not stable')

    source = DoubleLinkedList(values)
    buffer = DoubleLinkedList()

    while len(source):
        it = iter(source)
        min_it = it.copy()
        try:
            it.next()
            while True:
                tmp_it = it.copy()
                it.next()
                if tmp_it.value.value < min_it.value.value:
                    min_it = tmp_it
        except StopIteration:
            buffer.append(min_it.value)
            source.erase(min_it)

    print(' '.join(map(str, buffer)))
    if is_stable(values, buffer):
        print('Stable')
    else:
        print('Not stable')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
