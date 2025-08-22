from typing import List


class Markdown:
    stop = "\033[0m"

    bold = "\033[1m"
    underline = "\033[4m"

    @classmethod
    def markdown_list(cls) -> dict:
        return {
            key: value
            for key, value in vars(cls).items()
            if isinstance(value, str) and not key.startswith("__")
        }

    @classmethod
    def markdown_it(cls, text: str, marker: List[str]) -> str:
        for mark in marker:
            if mark in cls.markdown_list():
                text = f"{cls.markdown_list()[mark]}{text}{cls.stop}"
        return text

    @classmethod
    def bold_it(cls, text: str) -> str:
        return f"{cls.bold}{text}{cls.stop}"

    @classmethod
    def underline_it(cls, text: str) -> str:
        return f"{cls.underline}{text}{cls.stop}"
