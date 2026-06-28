from __future__ import annotations

from dataclasses import dataclass

from pathlib import Path

import yaml


@dataclass(slots=True)
class Configuration:

    project_name: str

    folders: list[str]

    @classmethod
    def load(cls) -> "Configuration":

        file = (
            Path(__file__)
            .parent.parent
            / "config"
            / "project.yaml"
        )

        data = yaml.safe_load(
            file.read_text(
                encoding="utf8"
            )
        )

        return cls(
            project_name=data["project"]["name"],
            folders=data["folders"],
        )