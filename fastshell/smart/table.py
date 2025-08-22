from .color import Color


class Table:
    def __init__(self):
        self.base_border_char: str = "-"
        self.base_color: Color = Color.white
        self.color_stop: Color = Color.stop
        self.column_separator: str = "|"
        self.missing_value: str = "None"

    def new(
            self,
            columns: list[dict],
            padding: int = 0,
            border_char: str = None,
            border_color: str = None,
            header_color: str = None,
            content_color: str = None,
    ) -> str:
        sample = str()

        border_char = border_char or self.base_border_char
        border_color = border_color or self.base_color
        header_color = header_color or self.base_color
        content_color = content_color or self.base_color

        max_rows = max(len(col["content"]) for col in columns)

        padded_columns = []
        for col in columns:
            padded_content = list(col["content"])
            while len(padded_content) < max_rows:
                padded_content.append(None)
            padded_columns.append({
                "header": col["header"],
                "content": padded_content
            })

        headers = [col["header"] for col in padded_columns]
        rows = list(zip(*[col["content"] for col in padded_columns]))

        col_widths = []
        for header, col in zip(headers, padded_columns):
            max_content_width = max(len(str(item)) if item is not None else
                                    len(self.missing_value)
                                    for item in col["content"])
            col_widths.append(max(len(header), max_content_width))

        def format_row(row_items, color):
            colored_items = []
            for item, width in zip(row_items, col_widths):
                display_value = (self.missing_value
                                 if item is None else str(item))
                colored_item = (f"{color}{display_value:<{width}}"
                                f"{self.color_stop}")
                colored_items.append(colored_item)
            return f" {self.column_separator} ".join(colored_items)

        separator_items = [border_char * width for width in col_widths]
        separator = (
            f"{border_color}"
            f"{f' {border_char * 3} '.join(separator_items)}{self.color_stop}"
        )

        sample += "\n" * padding
        sample += "\n" + format_row(headers, header_color)
        sample += "\n" + separator

        for row in rows:
            sample += "\n" + format_row(row, content_color)

        return sample
