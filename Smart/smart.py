from Smart.color import Color
from Smart.markdown import Markdown
from Smart.panel import Panel
from Smart.emoji import Emoji


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
