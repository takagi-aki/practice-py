#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""double_linked_list.py: 双方向連結リスト"""

__author__ = "Akinari Takagi"


from typing import Iterable
from attr import attr, attributes


class _DoubleLinkNode:

    def __init__(self, data) -> None:
        self.prev: _DoubleLinkNode = None
        self.next: _DoubleLinkNode = None
        self.data = data


class DoubleLinkedListItarator:
    """双方向連結リストのイテレータ
    """

    def __init__(self, parent, node: _DoubleLinkNode) -> None:
        self.__parent = parent
        self.__node = node

    @property
    def parent(self):
        return self.__parent

    @property
    def node(self):
        return self.__node

    @property
    def value(self):
        return self.__node.data

    @value.setter
    def value(self, x):
        """
        Example:
            >>> x = DoubleLinkedList([1,2,3])
            >>> it = iter(x)
            >>> _ = next(it)
            >>> it.value
            2
            >>> it.value = 4
            >>> x
            [1, 4, 3]
        """
        self.__node.data = x

    def __next__(self):
        if(self.__node is None):
            raise StopIteration
        else:
            node = self.__node
            self.__node = self.__node.next
            return node.data


class DoubleLinkedList(Iterable):
    """双方向連結リスト

    Examples:
        >>> a = DoubleLinkedList()
        >>> a.appendleft(5)
        >>> a.appendleft(2)
        >>> a.appendleft(3)
        >>> a.appendleft(1)
        >>> a.delete(3)
        >>> a.appendleft(6)
        >>> a.delete(5)
        >>> a
        [6, 1, 2]
        >>> b = DoubleLinkedList()
        >>> b.appendleft(5)
        >>> b.appendleft(2)
        >>> b.appendleft(3)
        >>> b.appendleft(1)
        >>> b.delete(3)
        >>> b.appendleft(6)
        >>> b.delete(5)
        >>> b.popleft()
        >>> b.pop()
        >>> b
        [1]
        >>> c = DoubleLinkedList()
        >>> c.insert(0,1)
        >>> c.insert(1,2)
        >>> c.insert(100,3)
        >>> c.insert(0,4)
        >>> c
        [4, 1, 2, 3]
    """

    def __init__(self, iterable: Iterable = None) -> None:
        self._first: _DoubleLinkNode = None  # 開始ノード
        self._last: _DoubleLinkNode = None  # 末端ノード
        self._length = 0       # リストの要素数

        if(iterable is not None):
            for x in iterable:
                self.append(x)

    def index(self, i:int):
        if i >= 0:
            node = self._first
            for n in range(i):
                if(node is None):
                    raise IndexError
                node = node.next
            return node.data
        else:
            node = self._last
            for n in range(i, 0):
                if(node is None):
                    raise IndexError
                node = node.prev
            return node.data


    def append(self, x):
        # 挿入する新たなノードを作成
        new_node = _DoubleLinkNode(x)

        # リストの開始ノードや末尾がないの時、あらたなノードをすれらにする
        # そうでなければ末端に追加
        if(self._first is None):
            self._first = new_node
        if(self._last is None):
            self._last = new_node
        else:
            self._last.next = new_node
            new_node.prev = self._last
            self._last = new_node

        # 要素のカウントをインクリメント
        self._length += 1

    def pop(self):
        # リストの開始ノードや末尾がないの時、そのまま
        # リストの末端=先端ならば末端と先端はNone
        # そうでなければ末端の一つ前のノードを末端にする
        if(self._last is None):
            return
        if(self._last.prev is None):
            self._last = None
            self._first = None
        else:
            self._last.prev.next = None
            self._last = self._last.prev

        # 要素のカウントをデクリメント
        self._length -= 1

    def appendleft(self, x):
        # 挿入する新たなノードを作成
        new_node = _DoubleLinkNode(x)

        # リストの開始ノードや末尾がないの時、あらたなノードをすれらにする
        # そうでなければ開始に追加
        if(self._first is None):
            self._first = new_node
        if(self._last is None):
            self._last = new_node
        else:
            self._first.prev = new_node
            new_node.next = self._first
            self._first = new_node

        # 要素のカウントをインクリメント
        self._length += 1

    def popleft(self):
        # リストの開始ノードがないの時、そのまま
        # リストの末端=先端ならば末端と先端はNone
        # そうでなければ開始の一つ先のノードを開始ノードにする
        if(self._first is None):
            return
        if(self._first.next is None):
            self._last = None
            self._first = None
        else:
            self._first.next.prev = None
            self._first = self._first.next

        # 要素のカウントをデクリメント
        self._length -= 1

    def delete(self, x):
        node = self._first
        while(node is not None):
            next_node = node.next

            # ノードのデータと一致したらノードを削除する
            if node.data == x:

                # 一つ前のノードの一つ先のノードを指定する
                # 一つ前のノードがない場合は現在の次のノードがリストの開始ノードとなる
                # 一つ前のノードがある場合は現在の次のノードとなる
                if(node.prev is None):
                    self._first = node.next
                else:
                    node.prev.next = node.next

                # 一つ先のノードの一つ前のノードを指定する
                # 一つ先のノードがない場合は現在の一つ前のノードがリストの終端ノードとなる
                # 一つ先のノードがある場合は現在の一つ前のノードとなる
                if(node.next is None):
                    self._last = node.prev
                else:
                    node.next.prev = node.prev

                # 要素のカウントをデクリメント
                self._length -= 1

            node = next_node

    def insert(self, i, x):
        # 挿入する新たなノードを作成
        new_node = _DoubleLinkNode(x)

        # 挿入位置の一つ次のノードを特定
        if(isinstance(i, DoubleLinkedListItarator)):
            if(i.parent is not self):
                raise ValueError
            node = i.node
        elif(isinstance(i, int)):
            node = self._first
            for n in range(min(i, len(self))):
                node = node.next
        else:
            raise ValueError

        # 挿入するノードの前後のノードを特定する
        node_new_prev: _DoubleLinkNode = None
        node_new_next: _DoubleLinkNode = None

        if(node is None):
            node_new_prev = self._last
            node_new_next = None
        elif(node.prev is None):
            node_new_prev = None
            node_new_next = node
        else:
            node_new_prev = node.prev
            node_new_next = node

        # 一つ前のノードと新たなノードをつなぐ
        # ない場合はリストの開始ノードが新たなノードとなる
        if(node_new_prev is None):
            self._first = new_node
        else:
            new_node.prev = node_new_prev
            node_new_prev.next = new_node

        # 一つ後のノードと新たなノードをつなぐ
        # ない場合はリストの末端ノードが新たなノードとなる
        if(node_new_next is None):
            self._last = new_node
        else:
            new_node.next = node_new_next
            node_new_next.prev = new_node

        # 要素のカウントをインクリメント
        self._length += 1

    def __len__(self):
        """リスト内の要素数を返す

        Examples:
            >>> a = DoubleLinkedList()
            >>> a.append(5)
            >>> a.append(2)
            >>> a.append(3)
            >>> a
            [5, 2, 3]
            >>> len(a)
            3
        """
        return self._length

    def __iter__(self):
        return DoubleLinkedListItarator(self, self._first)

    def __contains__(self, x) -> bool:
        """リスト内の要素にxと等価なものがあるか返す

        Examples:
            >>> a = DoubleLinkedList()
            >>> a.append(5)
            >>> a.append(2)
            >>> a.append(3)
            >>> 2 in a
            True
            >>> 1 in a
            False
        """

        for y in self:
            if x == y:
                return True
        return False

    def __repr__(self) -> str:
        return str([i for i in self])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
