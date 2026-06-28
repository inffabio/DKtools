from pathlib import Path

from dktools.core.filesystem import FileSystem
from dktools.core.logger import Logger
from dktools.models.folder import Folder
from dktools.models.project import Project


class BootstrapService:

    def __init__(self, project: Project):

        self.project = project

    def create(self, workspace: Path):

        root = workspace / self.project.name

        self._create_folder(root)

        for folder in self.project.folders:

            self._walk(root, folder)

    def _walk(self, current: Path, folder: Folder):

        path = current / folder.name

        self._create_folder(path)

        for child in folder.children:

            self._walk(path, child)

    def _create_folder(self, folder: Path):

        if FileSystem.ensure_directory(folder):

            Logger.success(f"Created {folder}")

        else:

            Logger.info(f"Exists {folder}")