from __future__ import annotations

from dataclasses import dataclass, field

from dktools.models.item import Item


@dataclass(slots=True)
class Folder(Item):

    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:

        self.items.append(item)