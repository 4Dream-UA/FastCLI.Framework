from .color import Color
from .markdown import Markdown
from .panel import Panel
from .emoji import Emoji
from .progress_bar import ProgressBar
from .table import Table


class Smart:

    @property
    def color(self) -> Color:
        return Color()

    @property
    def panel(self) -> Panel:
        return Panel()

    @property
    def emoji(self) -> Emoji:
        return Emoji()

    @property
    def markdown(self) -> Markdown:
        return Markdown()

    @property
    def table(self) -> Table:
        return Table()

    @property
    def progress_bar(self) -> ProgressBar:
        return ProgressBar()

    @staticmethod
    def legacy_shell_init() -> None:
        import os
        import sys
        import ctypes

        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

