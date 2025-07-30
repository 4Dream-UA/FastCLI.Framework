class NoRegisteredCommandsInArguments(Exception):

    def __init__(self) -> None:
        super().__init__("""
        You do not use any registration commands!
        If this exception is mistake - just use try-expect...
        to ignore it.
        """)


class UnexpectedCommandInArguments(Exception):

    def __init__(self, cmd) -> None:
        super().__init__(f"""
        You use an unexpected command!
        Please, just delete {cmd} command and try it again.
        """)
