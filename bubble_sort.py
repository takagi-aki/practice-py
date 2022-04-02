#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""bubble_sort.py: バブルソート"""

__author__ = "Akinari Takagi"

from typing import Iterable


def bubble_sort(values: Iterable):
    """バブルソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する

    Example:
        >>> bubble_sort([5,4,3,2,1])
        bubble sort
        1 2 3 4 5
        >>> bubble_sort([5,2,4,6,1,3])
        bubble sort
        1 2 3 4 5 6
    """

    print('bubble sort')

    buffer = list(values)

    for i in range(len(buffer)):
        for j in range(len(buffer)-1, i, -1):
            if(buffer[j] < buffer[j - 1]):
                buffer[j - 1], buffer[j] = buffer[j], buffer[j - 1]

    print(' '.join(map(str, buffer)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
