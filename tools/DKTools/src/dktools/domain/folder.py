from __future__ import annotations

from dataclasses import dataclass, field

from dktools.domain.item import Item


@dataclass(slots=True)
class Folder(Item):
    """
    Represents a directory.
    """

    children: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:
        self.children.append(item)