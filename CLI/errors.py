class NoRegisteredCommandsInArguments(Exception):

    def __init__(self) -> None:
        super().__init__("""
        You do not use any registration commands!
        If this exception is mistake - just use try-expect...
        to ignore it.
        """)