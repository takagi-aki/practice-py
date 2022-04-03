#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""selection_sort.py: 選択ソート関数定義ファイル"""

__author__ = "Akinari Takagi"

from typing import Iterable


from double_linked_list import DoubleLinkedList


def selection_sort(values: Iterable):
    """選択ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する
    非破壊
    O(n^2)

    Example:
        >>> selection_sort([5, 6, 4, 2, 1, 3])
        selection sort
        1 2 3 4 5 6
        4
        >>> selection_sort([5, 2, 4, 6, 1, 3])
        selection sort
        1 2 3 4 5 6
        3
    """

    print('selection sort')

    swapcnt = 0
    buffer = list(values)

    for i in range(len(buffer)):
        min_index = i
        for j in range(i + 1, len(buffer)):
            if(buffer[j] < buffer[min_index]):
                min_index = j
        if(min_index != i):
            swapcnt += 1
            buffer[min_index], buffer[i] = buffer[i], buffer[min_index]

    print(' '.join(map(str, buffer)))
    print(str(swapcnt))


def doublelinkedlist_selection_sort(values: Iterable):
    """DoubleLinkedListを使った選択ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する
    非破壊
    O(n^2)

    Example:
        >>> doublelinkedlist_selection_sort([5, 6, 4, 2, 1, 3])
        doublelinkedlist selection sort
        1 2 3 4 5 6
        >>> doublelinkedlist_selection_sort([5, 2, 4, 6, 1, 3])
        doublelinkedlist selection sort
        1 2 3 4 5 6
    """

    print('doublelinkedlist selection sort')

    # 入力データで双方向リストを構成しソースとする
    # ソースが空になるまで以下ループ
    #   ソースから最小値をもつノード(min_it)をとくてい
    #   出力バッファに最小値を出力
    #   ソースから(min_it)を削除

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
                if(tmp_it.value < min_it.value):
                    min_it = tmp_it
        except StopIteration:
            buffer.append(min_it.value)
            source.erase(min_it)

    print(' '.join(map(str, buffer)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
