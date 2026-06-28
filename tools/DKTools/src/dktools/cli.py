"""
Command Line Interface for DKTools.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from dktools.commands.bootstrap_command import BootstrapCommand


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dktools",
        description="DK Engineering Toolkit"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    subparsers.add_parser(
        "bootstrap",
        help="Create a new DK project structure."
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    workspace = Path.cwd()

    match args.command:
        case "bootstrap":
            BootstrapCommand().run(workspace)

        case _:
            parser.print_help()