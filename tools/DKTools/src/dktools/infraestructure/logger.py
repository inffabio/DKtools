"""
Simple console logger.
"""

from __future__ import annotations

from datetime import datetime


class Logger:

    @staticmethod
    def _timestamp() -> str:
        return datetime.now().strftime("%H:%M:%S")

    @classmethod
    def info(cls, message: str) -> None:
        print(f"[{cls._timestamp()}] [INFO] {message}")

    @classmethod
    def success(cls, message: str) -> None:
        print(f"[{cls._timestamp()}] [ OK ] {message}")

    @classmethod
    def warning(cls, message: str) -> None:
        print(f"[{cls._timestamp()}] [WARN] {message}")

    @classmethod
    def error(cls, message: str) -> None:
        print(f"[{cls._timestamp()}] [FAIL] {message}")