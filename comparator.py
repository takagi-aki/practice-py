#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""comparator.py: ソートに利用する比較関数の定義ファイル."""

__author__ = "Akinari Takagi"

__is_even = lambda a: (a % 2) == 0
__is_odd = lambda a: (a % 2) == 1

less_than = lambda a, b: a < b
greater_than = lambda a, b: b < a
less_than_but_even_less_than_odd = lambda a, b: (__is_even(a) and __is_odd(b))\
                                                or (not(__is_odd(a) and __is_even(b))\
                                                and (a < b))

if __name__ == '__main__':

    def test():
        """
        >>> from insertion_sort import insertion_sort, doublelinkedlist_insertion_sort
        >>> from bubble_sort import bubble_sort, doublelinkedlist_bubble_sort
        >>> from selection_sort import selection_sort, doublelinkedlist_selection_sort
        >>> from stable_sort import stable_sort, doublelinkedlist_stable_sort, Card
        >>> data = [1,3,5,4,2,6]
        >>> insertion_sort(data, less_than)
        insertion sort
        1 3 5 4 2 6
        1 3 5 4 2 6
        1 3 5 4 2 6
        1 3 4 5 2 6
        1 2 3 4 5 6
        1 2 3 4 5 6
        >>> insertion_sort(data, greater_than)
        insertion sort
        1 3 5 4 2 6
        3 1 5 4 2 6
        5 3 1 4 2 6
        5 4 3 1 2 6
        5 4 3 2 1 6
        6 5 4 3 2 1
        >>> insertion_sort(data, less_than_but_even_less_than_odd)
        insertion sort
        1 3 5 4 2 6
        1 3 5 4 2 6
        1 3 5 4 2 6
        4 1 3 5 2 6
        2 4 1 3 5 6
        2 4 6 1 3 5
        >>> doublelinkedlist_insertion_sort(data, less_than)
        doublelinkedlist insertion sort
        1
        1 3
        1 3 5
        1 3 4 5
        1 2 3 4 5
        1 2 3 4 5 6
        >>> doublelinkedlist_insertion_sort(data, greater_than)
        doublelinkedlist insertion sort
        1
        3 1
        5 3 1
        5 4 3 1
        5 4 3 2 1
        6 5 4 3 2 1
        >>> doublelinkedlist_insertion_sort(data, less_than_but_even_less_than_odd)
        doublelinkedlist insertion sort
        1
        1 3
        1 3 5
        4 1 3 5
        2 4 1 3 5
        2 4 6 1 3 5
        >>> bubble_sort(data, less_than)
        bubble sort
        1 2 3 4 5 6
        4
        >>> bubble_sort(data, greater_than)
        bubble sort
        6 5 4 3 2 1
        11
        >>> bubble_sort(data, less_than_but_even_less_than_odd)
        bubble sort
        2 4 6 1 3 5
        10
        >>> doublelinkedlist_bubble_sort(data, less_than)
        doublelinkedlist bubble sort
        1 2 3 4 5 6
        4
        >>> doublelinkedlist_bubble_sort(data, greater_than)
        doublelinkedlist bubble sort
        6 5 4 3 2 1
        11
        >>> doublelinkedlist_bubble_sort(data, less_than_but_even_less_than_odd)
        doublelinkedlist bubble sort
        2 4 6 1 3 5
        10
        >>> selection_sort(data, less_than)
        selection sort
        1 2 3 4 5 6
        2
        >>> selection_sort(data, greater_than)
        selection sort
        6 5 4 3 2 1
        3
        >>> selection_sort(data, less_than_but_even_less_than_odd)
        selection sort
        2 4 6 1 3 5
        4
        >>> doublelinkedlist_selection_sort(data, less_than)
        doublelinkedlist selection sort
        1 2 3 4 5 6
        >>> doublelinkedlist_selection_sort(data, greater_than)
        doublelinkedlist selection sort
        6 5 4 3 2 1
        >>> doublelinkedlist_selection_sort(data, less_than_but_even_less_than_odd)
        doublelinkedlist selection sort
        2 4 6 1 3 5
        >>> data = list(map(Card,['H4', 'C9', 'S4', 'D2', 'C3']))
        >>> stable_sort(data, less_than)
        stable sort
        D2 C3 H4 S4 C9
        Stable
        D2 C3 S4 H4 C9
        Not stable
        >>> stable_sort(data, greater_than)
        stable sort
        C9 H4 S4 C3 D2
        Stable
        C9 H4 S4 C3 D2
        Stable
        >>> stable_sort(data, less_than_but_even_less_than_odd)
        stable sort
        D2 H4 S4 C3 C9
        Stable
        D2 S4 H4 C3 C9
        Not stable
        >>> doublelinkedlist_stable_sort(data, less_than)
        doublelinkedlist stable sort
        D2 C3 H4 S4 C9
        Stable
        D2 C3 H4 S4 C9
        Stable
        >>> doublelinkedlist_stable_sort(data, greater_than)
        doublelinkedlist stable sort
        C9 H4 S4 C3 D2
        Stable
        C9 H4 S4 C3 D2
        Stable
        >>> doublelinkedlist_stable_sort(data, less_than_but_even_less_than_odd)
        doublelinkedlist stable sort
        D2 H4 S4 C3 C9
        Stable
        D2 H4 S4 C3 C9
        Stable
    """
        pass

    import doctest
    doctest.testmod()