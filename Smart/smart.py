from Smart.color import Color
from Smart.panel import Panel
from Smart.emoji import Emoji


class Smart:

    @property
    def color(self):
        return Color()

    @property
    def panel(self):
        return Panel()

    @property
    def emoji(self):
        return Emoji()
