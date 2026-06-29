"""
Configuration loader.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from dktools.domain.project import Project
from dktools.domain.folder import Folder
from dktools.domain.file import File


class Configuration:

    @classmethod
    def load(cls) -> Project:

        file = (
            Path(__file__)
            .parent.parent
            / "config"
            / "project.yaml"
        )

        if not file.exists():
            raise FileNotFoundError(file)

        data = yaml.safe_load(
            file.read_text(
                encoding="utf-8"
            )
        )

        project = Project(
            name=data["project"]["name"]
        )

        for item in data["tree"]:
            project.add(
                cls._create_item(item)
            )

        return project

    @classmethod
    def _create_item(cls, data):

        item_type = data["type"]

        if item_type == "folder":

            folder = Folder(
                name=data["name"]
            )

            for child in data.get(
                "children",
                []
            ):
                folder.add(
                    cls._create_item(child)
                )

            return folder

        if item_type == "file":

            return File(
                name=data["name"],
                template=data.get("template"),
                overwrite=data.get(
                    "overwrite",
                    False,
                ),
            )

        raise ValueError(
            f"Unknown item type: {item_type}"
        )