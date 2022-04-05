#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""comparator.py: ソートに利用する比較関数の定義ファイル"""

__author__ = "Akinari Takagi"


def less_than_but_even_less_than_odd_func_generator(is_odd, is_even):

    return lambda a, b: (is_even(a) and is_odd(b)) or (not(is_odd(a) and is_even(b)) and (a < b))


less_than = lambda a, b: a < b
greater_than = lambda a, b: b < a
less_than_but_even_less_than_odd = less_than_but_even_less_than_odd_func_generator(
    lambda a: (a % 2) == 1, 
    lambda a: (a % 2) == 0
)

if __name__ == '__main__':
    from insertion_sort import insertion_sort, doublelinkedlist_insertion_sort
    from bubble_sort import bubble_sort, doublelinkedlist_bubble_sort
    from selection_sort import selection_sort, doublelinkedlist_selection_sort
    from stable_sort import stable_sort, doublelinkedlist_stable_sort, Card

    less_than_but_even_less_than_odd_as_card = less_than_but_even_less_than_odd_func_generator(
        lambda c: (c.value % 2) == 1,
        lambda c: (c.value % 2) == 0
    )

    data = [1,3,5,4,2,6]
    insertion_sort(data, less_than)
    insertion_sort(data, greater_than)
    insertion_sort(data, less_than_but_even_less_than_odd)
    doublelinkedlist_insertion_sort(data, less_than)
    doublelinkedlist_insertion_sort(data, greater_than)
    doublelinkedlist_insertion_sort(data, less_than_but_even_less_than_odd)
    bubble_sort(data, less_than)
    bubble_sort(data, greater_than)
    bubble_sort(data, less_than_but_even_less_than_odd)
    doublelinkedlist_bubble_sort(data, less_than)
    doublelinkedlist_bubble_sort(data, greater_than)
    doublelinkedlist_bubble_sort(data, less_than_but_even_less_than_odd)
    selection_sort(data, less_than)
    selection_sort(data, greater_than)
    selection_sort(data, less_than_but_even_less_than_odd)
    doublelinkedlist_selection_sort(data, less_than)
    doublelinkedlist_selection_sort(data, greater_than)
    doublelinkedlist_selection_sort(data, less_than_but_even_less_than_odd)
    data = list(map(Card,['H4', 'C9', 'S4', 'D2', 'C3']))
    stable_sort(data, less_than)
    stable_sort(data, greater_than)
    stable_sort(data, less_than_but_even_less_than_odd)
    doublelinkedlist_stable_sort(data, less_than)
    doublelinkedlist_stable_sort(data, greater_than)
    doublelinkedlist_stable_sort(data, less_than_but_even_less_than_odd)

    import doctest
    doctest.testmod()