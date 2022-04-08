#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""double_linked_list.py: 双方向連結リスト"""

__author__ = "Akinari Takagi"


from typing import Iterable


class _DoubleLinkNode:

    def __init__(self, data) -> None:
        self.prev: _DoubleLinkNode = None
        self.next: _DoubleLinkNode = None
        self.data = data


class DoubleLinkedListItarator:
    """双方向連結リストのイテレータ.

    双方向連結リストDoubleLinkedListのイテレータ.
    元のリストでイテレータが指定するデータをeraseやpopしたあとのイテレータの動作は未定なので、利用しないでください.
    insertやappendするときは問題ありません.
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

    def next(self):
        """イテレーターを一つ先に進める

        Examples:
            >>> a = DoubleLinkedList([1, 2, 3])
            >>> it = iter(a)
            >>> it.next()
            1
            >>> it.next()
            2
        """
        return next(self)

    def prev(self):
        """イテレーターを一つ前に戻す

        Examples:
            >>> a = DoubleLinkedList([1, 2, 3])
            >>> it = iter(a)
            >>> it.next()
            1
            >>> it.prev()
            2
            >>> it.prev()
            1
        """
        if(self.__node is None):
            raise StopIteration
        else:
            node = self.__node
            self.__node = self.__node.prev
            return node.data

    def copy(self):
        """イテレーターをコピーする

        内部の値についてはコピーされない

        Examples:
            >>> a = DoubleLinkedList([1, 2, 3])
            >>> it = iter(a)
            >>> it.next()
            1
            >>> it2 = it.copy()
            >>> it.next()
            2
            >>> it2.next()
            2
        """
        return DoubleLinkedListItarator(self.__parent, self.__node)

    def __eq__(self, other):
        """イテレータがさすノードが等しいか返す.

        Examples:
            >>> a = DoubleLinkedList([1, 2, 3])
            >>> it = iter(a)
            >>> _ = it.next()
            >>> it2 = a.iterator(1)
            >>> it == it2
            True
            >>> _ = it2.next()
            >>> it == it2
            False
        """
        return self.node == other.node

    def __ne__(self, other):
        """イテレータがさすノードが等しくないか返す.

        Examples:
            >>> a = DoubleLinkedList([1, 2, 3])
            >>> it = iter(a)
            >>> _ = it.next()
            >>> it2 = a.iterator(1)
            >>> it != it2
            False
            >>> _ = it2.next()
            >>> it != it2
            True
        """
        return not (self == other)


class DoubleLinkedList(Iterable):
    """双方向連結リスト.

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

    def __find_node_from_index(self, i: int) -> _DoubleLinkNode:
        """先頭(末尾)からi番目のノードを取得する.

        Args:
            i: 取得するノードのインデックス.

        Returns:
            i >= 0 先頭からi番目のノード.
            i < 0 末尾から1-i番目のノード.

        Raises:
            IndexError: 指定するノードがデータ列の範囲外の時.
        """

        if i >= 0:
            node = self._first
            for n in range(i):
                if(node is None):
                    raise IndexError
                node = node.next
            return node
        else:
            node = self._last
            for n in range(i, -1, 1):
                if(node is None):
                    raise IndexError
                node = node.prev
            return node

    def __insert_node(self, node, x):
        """ノードを挿入する.

        Args:
            node : 新たなノードを追加する位置の次のノード.
                   必ずリスト内に含まれることを確認すること.
                   リスト内にない場合リストが壊れる.
                   ただし、末尾に追加する場合はNone.
            x    : 追加する値.
        """

        # 挿入する新たなノードを作成
        new_node = _DoubleLinkNode(x)

        if(node is None):
            if(self._last is None):
                # リストが空のときの処理
                self._first = new_node
                self._last = new_node
            else:
                # 末尾に挿入するときの処理
                new_node.prev = self._last
                self._last.next = new_node
                self._last = new_node
        elif(node.prev is None):
            # 先頭に挿入するときの処理
            new_node.next = self._first
            self._first.prev = new_node
            self._first = new_node
        else:
            # 2個のノードの間に挿入するときの処理
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node

        # 要素のカウントをインクリメント
        self._length += 1

    def __erase_node(self, node):
        """ノードを削除する.

        Args:
            node : 削除するノード。必ずリスト内に含まれることを確認すること。リスト内にない場合リストが壊れる.
        """

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

        # ノードの総数をデクリメント
        self._length -= 1

    def index(self, i: int):
        """インデクスから要素の値を返す.

        Args:
            i: 取得したい値のインデックス.

        Returns:
            i >= 0 先頭からi番目のノードの値.
            i < 0 末尾から1-i番目のノードの値.

        Raises:
            IndexError: 指定するノードがデータ列の範囲外の時.

        Examples:
            >>> a = DoubleLinkedList([1,2,3,4])
            >>> a.index(0)
            1
            >>> a.index(2)
            3
            >>> a.index(-1)
            4
        """
        node = self.__find_node_from_index(i)
        return node.data

    def iterator(self, i: int):
        """インデクスからイテレータを返す.

        Args:
            i: 取得したいイテレータの示す値のインデックス.

        Returns:
            i >= 0 先頭からi番目のイテレータ.
            i < 0 末尾から1-i番目のイテレータ.
            iが範囲のとき、ノードのデータを持たないイテレータ.

        Examples:
            >>> a = DoubleLinkedList([1,2,3,4])
            >>> it = a.iterator(0)
            >>> it.value
            1
            >>> it = a.iterator(2)
            >>> it.value
            3
            >>> it = a.iterator(-1)
            >>> it.value
            4
        """
            node = self.__find_node_from_index(i)
        return DoubleLinkedListItarator(self, node)

    def append(self, x):
        """末尾に要素を追加.

        Args:
            x: 追加したい値.

        Examples:
            >>> a = DoubleLinkedList()
            >>> a.append(1)
            >>> a.append(2)
            >>> a.append(3)
            >>> a
            [1, 2, 3]
        """

        self.__insert_node(None, x)

    def pop(self):
        """末尾の要素を削除.

        Examples:
            >>> a = DoubleLinkedList()
            >>> a.append(1)
            >>> a.append(2)
            >>> a.append(3)
            >>> a.pop()
            >>> a
            [1, 2]
        """

        self.__erase_node(self._last)

    def appendleft(self, x):
        """先頭の要素を追加.

        Args:
            x: 追加したい値.

        Examples:
            >>> a = DoubleLinkedList()
            >>> a.appendleft(1)
            >>> a.appendleft(2)
            >>> a.appendleft(3)
            >>> a
            [3, 2, 1]
        """

        self.__insert_node(self._first, x)

    def popleft(self):
        """先頭の要素を削除.

        Examples:
            >>> a = DoubleLinkedList()
            >>> a.appendleft(1)
            >>> a.appendleft(2)
            >>> a.appendleft(3)
            >>> a.popleft()
            >>> a
            [2, 1]
        """

        self.__erase_node(self._first)

    def delete(self, x):
        """指定した値と等価な要素をすべて削除.

        Args:
            x: 削除したい値.

        Examples:
            >>> a = DoubleLinkedList([1,2,3,2,1])
            >>> a.delete(1)
            >>> a
            [2, 3, 2]
        """

        node = self._first
        while(node is not None):
            next_node = node.next

            # ノードのデータと一致したらノードを削除する
            if node.data == x:
                self.__erase_node(node)

            node = next_node

    def insert(self, i, x):
        """指定した場所に要素を追加.

        Args:
            i: 削除したい場所のインデックスまたはイテレータ.
            x: 追加したい値.

        Raises:
            ValueError: iの型が無効であるか、イテレータが無効である.

        Examples:
            >>> a = DoubleLinkedList([1,2,3,4,5])
            >>> a.insert(2, 6)
            >>> a
            [1, 2, 6, 3, 4, 5]
            >>> it = a.iterator(3)
            >>> a.insert(it, 7)
            >>> a
            [1, 2, 6, 7, 3, 4, 5]
        """

        # 挿入位置の一つ次のノードを特定
        if(isinstance(i, DoubleLinkedListItarator)):
            if(i.parent is not self):
                raise ValueError
            node = i.node
        elif(isinstance(i, int)):
            node = self.__find_node_from_index(min(i, len(self)))
        else:
            raise ValueError

        self.__insert_node(node, x)

    def erase(self, i):
        """指定した場所の要素を削除.

        Args:
            i: 削除したい場所のインデックスまたはイテレータ.

        Raises:
            ValueError: iの型が無効であるか、イテレータが無効である.

        Examples:
            >>> a = DoubleLinkedList([1,2,3,4,5])
            >>> a.erase(2)
            >>> a
            [1, 2, 4, 5]
            >>> it = a.iterator(3)
            >>> a.erase(it)
            >>> a
            [1, 2, 4]
        """

        # 挿入位置の一つ次のノードを特定
        if(isinstance(i, DoubleLinkedListItarator)):
            if(i.parent is not self):
                raise ValueError
            node = i.node
        elif(isinstance(i, int)):
            node = self.__find_node_from_index(i)
        else:
            raise ValueError

        self.__erase_node(node)

    def __len__(self) -> int:
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

    def __iter__(self) -> DoubleLinkedListItarator:
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
