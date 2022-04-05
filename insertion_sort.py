#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""insertion_sort.py: 挿入ソート関数定義ファイル"""

__author__ = "Akinari Takagi"

from typing import Iterable


from double_linked_list import DoubleLinkedList


def insertion_sort(values: Iterable, comp_func=lambda a, b: a < b):
    """標準listを使用した挿入ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する

    n個の入力に対してO(n^2)
    非破壊

    Example:
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        insertion sort
        5 2 4 6 1 3
        2 5 4 6 1 3
        2 4 5 6 1 3
        2 4 5 6 1 3
        1 2 4 5 6 3
        1 2 3 4 5 6
        >>> insertion_sort([1, 2, 3])
        insertion sort
        1 2 3
        1 2 3
        1 2 3
    """

    print('insertion sort')

    buffer = list(values)

    for i in range(len(buffer)):
        v = buffer[i]
        j = i - 1
        while j >= 0 and comp_func(v, buffer[j]):
            buffer[j+1] = buffer[j]
            j -= 1
        buffer[j+1] = v

        print(' '.join(map(str, buffer)))


def doublelinkedlist_insertion_sort(values: Iterable, comp_func=lambda a, b: a < b):
    """DoubleLinkedListを使用した挿入ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する

    n個の入力に対してO(n^2)
    非破壊

    Example:
        >>> doublelinkedlist_insertion_sort([5, 2, 4, 6, 1, 3])
        doublelinkedlist insertion sort
        5
        2 5
        2 4 5
        2 4 5 6
        1 2 4 5 6
        1 2 3 4 5 6
        >>> doublelinkedlist_insertion_sort([1, 2, 3])
        doublelinkedlist insertion sort
        1
        1 2
        1 2 3
    """

    print('doublelinkedlist insertion sort')

    buffer = DoubleLinkedList()

    for x in values:
        it = iter(buffer)
        it2 = iter(buffer)

        while(True):
            try:
                val = next(it)
                if(not comp_func(val, x)):
                    buffer.insert(it2, x)
                    break
                _ = next(it2)
            except StopIteration:
                buffer.insert(it, x)
                break

        print(' '.join(map(str, buffer)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
