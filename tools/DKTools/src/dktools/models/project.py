from __future__ import annotations

from dataclasses import dataclass, field

from pathlib import Path

from dktools.models.item import Item


@dataclass(slots=True)
class Project:

    name: str

    version: str = "0.1.0"

    root: Path | None = None

    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:

        self.items.append(item)