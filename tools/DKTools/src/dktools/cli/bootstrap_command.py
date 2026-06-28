from pathlib import Path

from dktools.core.configuration import Configuration

from dktools.services.bootstrap_service import BootstrapService


class BootstrapCommand:

    def run(self, workspace: Path):

        configuration = Configuration.load()

        BootstrapService(configuration).create(workspace)