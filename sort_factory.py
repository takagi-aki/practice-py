#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""sort_factory.py: ソートクラスオブジェクト生成器"""

__author__ = "Akinari Takagi"

from typing import Union


from isort import ISort, ICardSort
from sort import InsertionSort, DoubleLinkedListInsertionSort, BubbleSort, DoubleLinkedListBubbleSort, SelectionSort, DoubleLinkedListSelectionSort, StableSort, DoubleLinkedListStableSort


__sort_algorithm_dict = {
    'insertion': InsertionSort, 'doublelinkedlist_insertion': DoubleLinkedListInsertionSort,
    'bubble': BubbleSort, 'doublelinkedlist_bubble': DoubleLinkedListBubbleSort,
    'selection': SelectionSort, 'doublelinkedlist_selection': DoubleLinkedListSelectionSort,
    'stable': StableSort, 'doublelinkedlist_stable': DoubleLinkedListStableSort}


def get_sort_instance(algorithm_name) -> Union[ISort, ICardSort]:
    """名前にあったソートアルゴリズムを取得

    Example:
        >>> a = get_sort_instance('insertion')
        >>> isinstance(a, InsertionSort)
        True
        >>> a = get_sort_instance('doublelinkedlist_insertion')
        >>> isinstance(a, DoubleLinkedListInsertionSort)
        True
    """
    C = __sort_algorithm_dict.get(algorithm_name)
    C()

    return C()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
