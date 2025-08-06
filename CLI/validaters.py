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

    @staticmethod
    def validate_help_calling(args: list) -> bool:

        """
        This validator used for call self.command_help ...
        if statement is True

        :param args:
        :return:
        """

        if len(args) > 1 and args[1] == "--help":
            return True
        return False

    @staticmethod
    def validate_g_help(args: list) -> bool:

        """
        This validator used for call self.global_commands_help ...
        with none attributes if statement is True

        :param args:
        :return:
        """

        if "--g-help" in args:
            return True
        return False

    @staticmethod
    def validate_g_help_with_cli(args: list) -> bool:

        """
        This validator used for call self.global_commands_help ...
        with cli_info=True if statement is True

        :param args:
        :return:
        """

        if "--g-help-with-cli" in args:
            return True
        return False

    @staticmethod
    def validate_set_required_params(sig_parameters: dict, params: list, required: list) -> bool:
        if [name for name, p in sig_parameters if name in params] != required and required:
            return True
        return False
