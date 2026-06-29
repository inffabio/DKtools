from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass(slots=True)
class Item(ABC):
    """
    Base class for every project item.
    """

    name: str