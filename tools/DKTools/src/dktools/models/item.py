from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Item:
    """
    Base class for all project items.
    """

    name: str