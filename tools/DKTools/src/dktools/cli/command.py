from pathlib import Path

from dktools.core.configuration import Configuration
from dktools.services.bootstrap_service import BootstrapService


class BootstrapCommand:

    def run(self, workspace: Path) -> None:

        configuration = Configuration.load()

        service = BootstrapService(configuration)

        service.create_project(workspace)