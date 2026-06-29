class Logger:

    @staticmethod
    def created(text: str):

        print(f"[CREATE] {text}")

    @staticmethod
    def skipped(text: str):

        print(f"[SKIP]   {text}")

    @staticmethod
    def error(text: str):

        print(f"[ERROR]  {text}")