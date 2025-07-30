from CLI.errors import (
    NoRegisteredCommandsInArguments
)


class BaseValidater:

    @staticmethod
    def validate_not_args(args: list) -> Exception | None:
        if not args:
            raise NoRegisteredCommandsInArguments()

        return None