from typing import (
    Optional, Callable, Any,
    List, Dict,
)


class BaseValidater:

    @staticmethod
    def validate_not_args(args: List[Optional[str]]) -> bool:

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
    def validate_not_func(func: Callable[[Any], Any]) -> bool:

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
    def validate_missing(missing: List[Optional[str]]) -> bool:

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
    def validate_help_calling(args: List[str]) -> bool:

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
    def validate_g_help(args: List[str]) -> bool:

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
    def validate_g_help_with_cli(args: List[str]) -> bool:

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
    def validate_set_required_params(
            sig_parameters: Dict[str, str],
            params: List[str],
            required: List[str],
    ) -> bool:

        """
        This validator used for select from all ...
        parameters only required

        :param sig_parameters:
        :param params:
        :param required:
        :return:
        """
        if (
                [
                    name for name, p in sig_parameters if name in params
                ] != required and required
        ):
            return True
        return False
