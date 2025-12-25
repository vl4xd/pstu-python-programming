from .plugin import Plugin


class ReversePlugin(Plugin, name="reverse"):


    def execute(self, text: str) -> str:
        return text[::-1]
