from CLI.errors import (
    NoRegisteredCommandsInArguments
)


class BaseValidater:

    @staticmethod
    def validate_not_args(args: list) -> bool:
        if not args:
            return True
        return False

