from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class File:

    name: str

    template: str | None = None

    overwrite: bool = False