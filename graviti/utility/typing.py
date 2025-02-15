#!/usr/bin/env python3
#
# Copyright 2022 Graviti. Licensed under MIT License.
#

"""Graviti customized types."""

from typing import AbstractSet, Tuple, TypeVar, Union

from typing_extensions import Protocol

_K = TypeVar("_K")
_V = TypeVar("_V")


class NestedDict(Protocol[_K, _V]):
    """Typehint for nested dict."""

    def __getitem__(self, key: _K) -> Union["NestedDict[_K, _V]", _V]:
        ...

    def __setitem__(self, key: _K, value: Union["NestedDict[_K, _V]", _V]) -> None:
        ...

    def items(self) -> AbstractSet[Tuple[_K, Union["NestedDict[_K, _V]", _V]]]:
        """Return (key, value) pairs of the dict."""
        ...
