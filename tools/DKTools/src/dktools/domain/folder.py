from __future__ import annotations

from dataclasses import dataclass, field

from dktools.domain.file import File


@dataclass(slots=True)
class Folder:

    name: str

    items: list["Folder | File"] = field(default_factory=list)

    def add(self, item: "Folder | File") -> None:
        self.items.append(item)