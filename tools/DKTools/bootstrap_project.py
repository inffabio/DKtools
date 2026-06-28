from pathlib import Path

from dktools.application import Application


def main() -> None:
    app = Application()
    app.bootstrap(Path.cwd())


if __name__ == "__main__":
    main()