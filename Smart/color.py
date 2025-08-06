class Color:
    stop = "\033[0m"

    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    cyan = "\033[36m"
    magenta = "\033[35m"
    white = "\033[37m"

    # move it in own file in future
    bold = "\033[1m"
    underline = "\033[4m"

    @classmethod
    @property
    def color_dict(cls):
        return {
            key: value
            for key, value in vars(cls).items()
            if not key.startswith("__") and not callable(value)
        }

    @classmethod
    def colorize(cls, color: str, text: str) -> str:
        return f"{cls.color_dict.get(color)}{text}{cls.stop}"
