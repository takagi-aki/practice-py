#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""insertion_sort.py: 挿入ソート関数定義ファイル"""

__author__ = "Akinari Takagi"

from typing import Iterable

from numpy import insert
from double_linked_list import DoubleLinkedList


def insertion_sort(values: Iterable):
    """挿入ソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する

    多分O(n^2)

    Example:
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        insertion sort
        1 2 3 4 5 6
        >>> insertion_sort([1, 2, 3])
        insertion sort
        1 2 3
    """

    print('insertion sort')

    buffer = DoubleLinkedList()

    for x in values:
        it = iter(buffer)
        it2 = iter(buffer)

        while(True):
            try:
                val = next(it)
                if(not (val < x)):
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
