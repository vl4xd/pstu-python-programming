class Plugin:


    PluginRegistry = {}


    def __init_subclass__(cls, /, name: str, **kwargs):
        super().__init_subclass__(**kwargs)

        if name in Plugin.PluginRegistry:
            raise ValueError(f"Плагин с именем '{name}' уже существует")

        Plugin.PluginRegistry[name] = cls
        cls.name = name


    def execute(self, text: str) -> str:
        raise NotImplementedError("Метод 'execute' должен быть реализован в подклассе")
