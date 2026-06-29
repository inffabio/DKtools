from pathlib import Path

from dktools.models.folder import Folder
from dktools.models.file import File
from dktools.models.item import Item

from dktools.models.project import Project

from dktools.core.filesystem import FileSystem
from dktools.core.logger import Logger


class BootstrapService:

    def create(
        self,
        workspace: Path,
        project: Project,
    ) -> None:

        root = workspace / project.name

        FileSystem.ensure_directory(root)

        for item in project.items:

            self._create_item(
                root,
                item,
            )

    def _create_item(
        self,
        current: Path,
        item: Item,
    ) -> None:

        if isinstance(item, Folder):

            directory = current / item.name

            created = FileSystem.ensure_directory(
                directory
            )

            if created:
                Logger.created(directory)

            else:
                Logger.skipped(directory)

            for child in item.items:

                self._create_item(
                    directory,
                    child,
                )

            return

        if isinstance(item, File):

            file = current / item.name

            created = FileSystem.ensure_file(
                file
            )

            if created:
                Logger.created(file)

            else:
                Logger.skipped(file)