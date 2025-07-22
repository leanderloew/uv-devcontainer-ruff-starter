from collections import defaultdict
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass as _unvalidated_dataclass
from typing import Any, TypeVar, cast, dataclass_transform, overload

from pydantic import ConfigDict
from pydantic.dataclasses import dataclass as _dataclass

T = TypeVar("T")
U = TypeVar("U")


@dataclass_transform()
@overload
def validated_dataclass[T](_cls: type[T]) -> type[T]: ...
@overload
def validated_dataclass[T](_cls: None = None, **kwargs: Any) -> Callable[[type[T]], type[T]]: ...


def validated_dataclass[T](_cls: type[T] | None = None, **kwargs: Any) -> Callable[[type[T]], type[T]] | type[T]:
    if "frozen" in kwargs:
        raise ValueError("Cannot override 'frozen'.")
    if "config" in kwargs:
        raise ValueError("Cannot override 'config'.")

    def wrapper(cls: type[T]) -> type[T]:
        return cast(type[T], _dataclass(cls, frozen=True, config=ConfigDict(extra="forbid"), **kwargs))

    return wrapper if _cls is None else wrapper(_cls)


@dataclass_transform()
@overload
def unvalidated_dataclass[T](_cls: type[T]) -> type[T]: ...
@overload
def unvalidated_dataclass[T](_cls: None = None, **kwargs: Any) -> Callable[[type[T]], type[T]]: ...


def unvalidated_dataclass[T](_cls: type[T] | None = None, **kwargs: Any) -> Callable[[type[T]], type[T]] | type[T]:
    if "frozen" in kwargs:
        raise ValueError("Cannot override 'frozen'.")

    def wrapper(cls: type[T]) -> type[T]:
        return cast(type[T], _unvalidated_dataclass(cls, frozen=True, **kwargs))  # type: ignore

    return wrapper if _cls is None else wrapper(_cls)


class FrozenDict(dict[T, U]):
    def __setitem__(self, key: T, value: U) -> None:
        raise TypeError("Attempted assignment on a frozen dict")


def batch[T](iterable: Sequence[T], n: int = 1) -> Iterable[Sequence[T]]:
    """Batches a Sequence of size x to int(x/n) Sequences of size n and one with the rest."""
    length_of_iter = len(iterable)
    for ndx in range(0, length_of_iter, n):
        yield iterable[ndx : min(ndx + n, length_of_iter)]  # noqa: E203


def groupby(iterable: Iterable[T], key_fn: Callable[[T], U]) -> dict[U, list[T]]:
    d: defaultdict[U, list[T]] = defaultdict(list)
    for i in iterable:
        d[key_fn(i)].append(i)
    return dict(d)
