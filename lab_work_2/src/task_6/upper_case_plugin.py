from .plugin import Plugin


class UpperCasePlugin(Plugin, name="upper"):


    def execute(self, text: str) -> str:
        return text.upper()
