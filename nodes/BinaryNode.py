from typing import Tuple, Sequence, TypeVar, List, overload, Union

T = TypeVar('T', covariant=True)


class BinaryNodeBase(object):
    '''A node with up to 2 children pointers.'''

    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(' + \
            f'value={self.value}' + ', ' + \
            f'left={self.left}' + ', ' + \
            f'right={self.right})'


class BinaryNode(BinaryNodeBase, Sequence[T]):

    '''Sequence version of a BinaryNode'''

    def _search(self, count: int, index: int) -> Tuple[BinaryNode, int]:
        if self.left:
            found, count = self.left._search(count, index)
            if found:
                return found, count
        if count is index:
            return self, count
        elif self.right:
            return self.right._search(count + 1, index)
        else:
            return None, count + 1

    @overload
    def __getitem__(self, idx: int) -> T: ...

    @overload
    def __getitem__(self, s: slice) -> Sequence[T]: ...

    def __getitem__(self, item):
        found, _ = self._search(0, item)
        if not found:
            raise IndexError('Index out of range')
        return found.value

    def __len__(self) -> int:
        found, count = self._search(0, None)
        return count
