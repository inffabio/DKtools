from __future__ import annotations

from dataclasses import dataclass, field

from dktools.domain.folder import Folder
from dktools.domain.file import File


@dataclass(slots=True)
class Project:

    name: str

    version: str = "0.1.0"

    items: list[Folder | File] = field(default_factory=list)

    def add(self, item: Folder | File) -> None:
        self.items.append(item)