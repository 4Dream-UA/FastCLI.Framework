class NoRegisteredCommandsInArguments(Exception):
    def __init__(self) -> None:
        super().__init__(
            """
            You do not use any registration commands!
            If this exception is mistake - just use try-expect...
            to ignore it.
            """
        )


class UnexpectedCommandInArguments(Exception):

    def __init__(self, cmd: str) -> None:
        super().__init__(
            f"""
            You use an unexpected command!
            Please, just delete {cmd} command and try it again.
            """
        )


class CommandWithoutRegisteredMissing(Exception):

    def __init__(self, missing: str) -> None:
        super().__init__(
            f"""
            You do not use all missing of commands!
            Anyway, just add {missing} missing to your command ...
            like `python file.py foo /: parm1=val1 parm2=val2 :/`.
            """
        )


class CommandWithoutRequiredArgument(Exception):
    def __init__(self, required) -> None:
        super().__init__(
            f"""
            You do not use all required arguments!
            Anyway, just add {required} required arguments to your command.
            """
        )
