from __future__ import annotations

from dataclasses import dataclass

from dktools.models.item import Item


@dataclass(slots=True)
class File(Item):

    template: str | None = None

    overwrite: bool = False