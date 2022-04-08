#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""isort.py: ソートクラスインターフェース定義"""

__author__ = "Akinari Takagi"


from typing import Iterable

from isort import ICardSort, ISort
from comparator import less_than
from insertion_sort import insertion_sort, doublelinkedlist_insertion_sort
from bubble_sort import bubble_sort, doublelinkedlist_bubble_sort
from selection_sort import selection_sort, doublelinkedlist_selection_sort
from stable_sort import stable_sort, doublelinkedlist_stable_sort

class InsertionSort(ISort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        insertion_sort(values, cmp_func)


class DoubleLinkedListInsertionSort(ISort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        bubble_sort(values, cmp_func)


class BubbleSort(ISort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        doublelinkedlist_bubble_sort(values, cmp_func)


class DoubleLinkedListBubbleSort(ISort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        doublelinkedlist_insertion_sort(values, cmp_func)


class SelectionSort(ISort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        selection_sort(values, cmp_func)


class DoubleLinkedListSelectionSort(ISort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        doublelinkedlist_selection_sort(values, cmp_func)


class StableSort(ICardSort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        stable_sort(values, cmp_func)


class DoubleLinkedListStableSort(ICardSort):

    def __init__(self) -> None:
        super().__init__()

    def sort(values: Iterable, cmp_func=less_than):
        doublelinkedlist_stable_sort(values, cmp_func)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
