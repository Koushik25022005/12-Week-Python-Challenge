"""Shared typing helpers for Week 2."""
from __future__ import annotations

from typing import Any, Protocol, TypeVar


class SupportsLessThan(Protocol):
    """Anything that can be ordered with ``<``."""

    def __lt__(self, other: Any) -> bool:  # pragma: no cover
        ...


Comparable = TypeVar("Comparable", bound=SupportsLessThan)
Item = TypeVar("Item")
