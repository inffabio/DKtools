"""
Filesystem abstraction.

All filesystem operations must go through this class.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


class FileSystem:
    """Utility class for filesystem operations."""

    @staticmethod
    def ensure_directory(path: Path) -> bool:

        if path.exists():
            return False

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return True

    @staticmethod
    def ensure_file(
        path: Path,
        content: str = "",
        encoding: str = "utf-8",
    ) -> bool:

        if path.exists():
            return False

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            content,
            encoding=encoding,
        )

        return True

    @staticmethod
    def exists(path: Path) -> bool:
        return path.exists()

    @staticmethod
    def read(path: Path) -> str:
        return path.read_text(encoding="utf-8")

    @staticmethod
    def write(
        path: Path,
        content: str,
        encoding: str = "utf-8",
    ) -> None:

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            content,
            encoding=encoding,
        )

    @staticmethod
    def directories(path: Path) -> Iterable[Path]:
        return sorted(
            [
                item
                for item in path.iterdir()
                if item.is_dir()
            ]
        )

    @staticmethod
    def files(path: Path) -> Iterable[Path]:
        return sorted(
            [
                item
                for item in path.iterdir()
                if item.is_file()
            ]
        )