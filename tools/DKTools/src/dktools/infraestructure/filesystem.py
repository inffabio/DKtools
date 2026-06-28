    @staticmethod
    def create_text_file(
        file: Path,
        content: str
    ) -> bool:

        if file.exists():
            return False

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        return True


    @staticmethod
    def create_empty_file(
        file: Path
    ) -> bool:

        if file.exists():
            return False

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.touch()

        return True