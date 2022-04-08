#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""isort.py: ソートクラスインターフェース定義"""

__author__ = "Akinari Takagi"


from abc import ABCMeta, abstractmethod
from typing import Iterable


from card import Card
from comparator import less_than


class ISort(metaclass=ABCMeta):

    @abstractmethod
    def sort(values: Iterable, cmp_func=less_than):
        pass

class ICardSort(metaclass=ABCMeta):

    @abstractmethod
    def sort(values: Iterable[Card], cmp_func=less_than):
        pass
