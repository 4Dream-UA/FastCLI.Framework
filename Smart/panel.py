from .color import Color


class Panel:
    def __init__(self):
        self.base_border_char = "_"
        self.base_color = Color.white
        self.color_stop = Color.stop

    def new_panel(
        self,
        title: str,
        content: list,
        padding: int = 0,
        width: int = 30,
        border_char: str = None,
        border_color: str = None,
    ) -> str:
        panel = str()

        border_char = border_char or self.base_border_char
        border_color = border_color or self.base_color

        horizontal_border = border_char * width
        panel += "\n" * padding
        top_line = f"{border_color}{horizontal_border} {title} {horizontal_border}{self.color_stop}"

        panel += "\n" + top_line

        for item in content:

            item_title = item.get("title", "")
            item_text = item.get("text", "")
            item_color = item.get("color", self.base_color)
            item_padding = item.get("padding", 0)

            line = f"{item_color}{item_title}: {item_text}{self.color_stop}"
            padded_line = (" " * item_padding) + line if content[0] is item else "\n" + (" " * item_padding) + line

            panel += "\n" + padded_line

        bottom_line = f"{border_color}{border_char * (len(top_line) - len(self.color_stop) - 5)}{self.color_stop}"
        panel += "\n" + bottom_line

        return panel
