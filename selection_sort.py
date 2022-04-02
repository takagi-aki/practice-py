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
        >>> selection_sort([5, 2, 4, 6, 1, 3])
        selection sort
        1 2 3 4 5 6
    """

    print('selection sort')

    buffer = list(values)

    for i in range(len(buffer)):
        min_val = buffer[i]
        min_index = i
        for j in range(i, len(buffer)):
            if(buffer[j] < min_val):
                min_val = buffer[j]
                min_index = j
        buffer[min_index] = buffer[i]
        buffer[i] = min_val

    print(' '.join(map(str, buffer)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
