#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""card.py: カードクラス定義"""

__author__ = "Akinari Takagi"


class Card:
    """カードクラス.

    トランプのカードの記号文字列と数値を分けて保存し利用しやすくするクラス.

    Attributes:
        str (str): 数値と記号を含めたカード名文字列.
        value (int): カードの数値.
        suit (str): カードの記号文字列.
    """


    def __init__(self, card_str) -> None:
        """
        Args:
            card_str (str): カードの記号と数値を表す文字列(例'H1').

        Examples:    
            >>> a = Card('S4')
            >>> a.str
            'S4'
            >>> a.value
            4
            >>> a.suit
            'S'
        """

        self.str = card_str
        self.value = int(card_str[1:])
        self.suit = card_str[0]

    def __repr__(self) -> str:
        return self.str


if __name__ == '__main__':
    import doctest
    doctest.testmod()
