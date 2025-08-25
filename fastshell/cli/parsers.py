import ast
from typing import (
    Optional, Callable, Any,
    List, Dict, Tuple,
)


class BaseParser:

    @staticmethod
    def parse_params(args: List[str]) -> Dict[str, str]:
        if "/:" not in args or ":/" not in args:
            return {}, args

        start = args.index("/:") + 1
        end = args.index(":/", start)
        params = {
            k.strip(): v.strip('"').strip("'")
            for k, v in
            (arg.split("=", 1) for arg in args[start:end] if "=" in arg)
        }
        remaining_args = args[end + 1:]

        return params, remaining_args

    @staticmethod
    def parse_multitypes(
            multitypes: bool,
            params: Dict[str, str],
    ) -> dict:

        if multitypes:

            for param_key, param_value in params.items():
                try:
                    params[param_key] = ast.literal_eval(param_value)
                except ValueError:
                    params[param_key] = param_value

        return params

    @staticmethod
    def parse_func_info(
            cmd: str,
            commands: Dict[str, str],
    ) -> Dict[str, str]:
        func_info = commands.get(cmd)

        if func_info is None:
            for value in commands.values():
                if value["alias"] is None:
                    continue

                if cmd in value["alias"]:
                    func_info = value

        return func_info

    @staticmethod
    def parse_args(
            argv: List[str],
            fake_args: List[str],
            debugging: bool,
    ) -> List[str]:
        args = argv[0:]
        if debugging and fake_args:
            args = fake_args

        return args

    @staticmethod
    def parse_missing(
            parameters: Dict[str, str],
            params: List[str],
            inspect_parameter: Callable[[Any], Any],
    ) -> List[Optional[str]]:
        return [
            name for name, p in parameters
            if name not in params and p.default is inspect_parameter
        ]

    @staticmethod
    def parse_set_required_exception(
            sig_parameters: Dict[str, str],
            params: List[str],
            required: List[str],
    ) -> List[str]:
        req_parameters = [name for name, p in sig_parameters if name in params]

        res: List[str] = list()
        for param in required:
            if param not in req_parameters:
                res.append(param)

        return res

    @staticmethod
    def parse_expose(
            args: List[str],
            expose: str,
            expose_yes_tag: str,
            expose_no_tag: str,
            expose_prompt: str,
    ) -> List[str] | bool:
        argv = args.copy()

        if expose:
            if expose_yes_tag in argv:
                argv.remove(expose_yes_tag)
                return argv, True
            elif expose_no_tag in argv:
                argv.remove(expose_no_tag)
                print(f"Command '{cmd}' skipped by user.")
                return argv, False
            else:
                confirm: str = input(expose_prompt).strip().lower()
                if confirm not in ("y", "yes", expose_yes_tag):
                    print(f"Command '{cmd}' cancelled by user.")
            return argv, False
        return argv, False

    @staticmethod
    def parser_global_flags(
            args: List[str],
            flag_definitions: List[Tuple[Callable, str, bool]],
    ) -> List[str] | List[bool]:
        args_copy = args.copy()
        flags_using = []

        for validator_fn, option_name, cli_info in flag_definitions:
            flag = validator_fn(args=args_copy)
            if flag:
                flags_using.append(flag)
                self.__global_commands_help(cli_info=cli_info)

                args_copy.remove(option_name)

        return args_copy, flags_using
