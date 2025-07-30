class BaseValidater:

    @staticmethod
    def validate_not_args(args: list) -> bool:
        """
        This validater used for raise NoRegisteredCommandsInArguments ...
        Exception if return True

        :param args:
        :return:
        """
        if not args:
            return True
        return False

    @staticmethod
    def validate_not_func(func: callable) -> bool:
        """
        This validator used for raise UnexpectedCommandInArguments ...
        Exception if return True
        :param func:
        :return:
        """
        if not func:
            return True
        return False

    @staticmethod
    def validate_missing(missing: list) -> bool:
        """
        This validator used for raise CommandWithoutRegisteredMissing ...
        Exception if return True
        :param missing:
        :return:
        """
        if missing:
            return True
        return False
