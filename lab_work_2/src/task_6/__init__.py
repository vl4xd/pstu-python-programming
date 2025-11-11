from .plugin import Plugin
from .upper_case_plugin import UpperCasePlugin
from .reverse_plugin import ReversePlugin


# При имопрте модуля через * будут импортированы только следующие имена...
__all__ = ['Plugin', 'UpperCasePlugin', 'ReversePlugin']
