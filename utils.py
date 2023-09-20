from typing import (
    TYPE_CHECKING,
    Any,
    Optional,
    Sequence,
    Tuple,
)

if TYPE_CHECKING:
    DispArgs = Sequence[Tuple[Optional[str]], Any]

class ObjectDisplayMixin:
    '''
    '''
    __slots__: Tuple[str, ...] = tuple()

    def __display_attributes__(self) -> 'DispArgs':
        attrs = ((s, getattr(self, s)) for s in self.__slots__)
        return [(a, v) for a, v in attrs if v is not None]

    def __repr_name__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return self.__repr_str__(' ')

    def __repr__(self) -> str:
        return f'{self.__repr_name__()}'