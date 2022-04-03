#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""bubble_sort.py: バブルソート"""

__author__ = "Akinari Takagi"

from typing import Iterable


from double_linked_list import DoubleLinkedList


def bubble_sort(values: Iterable):
    """Listを利用したバブルソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する

    Example:
        >>> bubble_sort([5,3,2,4,1])
        bubble sort
        1 2 3 4 5
        8
        >>> bubble_sort([5,2,4,6,1,3])
        bubble sort
        1 2 3 4 5 6
        9
    """

    print('bubble sort')

    swapcnt = 0
    is_not_sorted = True
    buffer = list(values)

    while(is_not_sorted):
        is_not_sorted = False
        for j in range(len(buffer)-1, 0, -1):
            if(buffer[j] < buffer[j - 1]):
                swapcnt += 1
                is_not_sorted = True
                buffer[j - 1], buffer[j] = buffer[j], buffer[j - 1]

    print(' '.join(map(str, buffer)))
    print(str(swapcnt))


def doublelinkedlist_bubble_sort(values: Iterable):
    """DoubleLinkedListを利用したバブルソート

    Iterableなオブジェクト内の要素をソートし
    結果を標準出力に表示する

    Example:
        >>> doublelinkedlist_bubble_sort([5,3,2,4,1])
        doublelinkedlist bubble sort
        1 2 3 4 5
        8
        >>> doublelinkedlist_bubble_sort([5,2,4,6,1,3])
        doublelinkedlist bubble sort
        1 2 3 4 5 6
        9
    """

    print('doublelinkedlist bubble sort')

    swapcnt = 0
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
                if(it_right.value < it_left.value):
                    swapcnt += 1
                    is_not_sorted = True
                    it_right.value, it_left.value = it_left.value, it_right.value
                it_left.prev()
                it_right.prev()
        except StopIteration:
            pass

    print(' '.join(map(str, buffer)))
    print(str(swapcnt))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
