import sys
import inspect
from typing import (
    Optional, Callable, Any,
    Dict, List,
)
from .errors import (
    NoRegisteredCommandsInArguments,
    UnexpectedCommandInArguments,
    CommandWithoutRegisteredMissing,
    CommandWithoutRequiredArgument,
)
from .parsers import BaseParser
from .validaters import BaseValidater


class CLI:
    def __init__(self):
        self._commands: Dict[str, Dict[str, Any]] = dict()
        self._parser: BaseParser = BaseParser()
        self._validator: BaseValidater = BaseValidater()

    def command(
            self,
            name: str,
            multitypes: bool = False,
            expose: bool = False,
            expose_prompt: str = "Do you sure? [y/N]: ",
            expose_yes_tag: str = "--yes",
            expose_no_tag: str = "--no",
            _help: Optional[str] = None,
            params_help: Optional[Dict[str, str]] = None,
            alias: Optional[List[str]] = None,
            required: Optional[List[Any]] = None,
            _return: bool = True,
    ) -> Callable[[Any], Any]:
        def wrapper(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
            self._commands[name] = {
                "func": func,
                "multitypes": multitypes,
                "expose": expose,
                "expose_prompt": expose_prompt,
                "expose_yes_tag": expose_yes_tag,
                "expose_no_tag": expose_no_tag,
                "_help": _help,
                "params_help": params_help,
                "alias": alias,
                "required": required,
                "_return": _return,
            }
            return func
        return wrapper

    def main(
            self,
            cli_app: bool = True,
            debugging: bool = False,
            fake_args: Optional[List[str]] = None
    ) -> None:
        args = self._parser.parse_args(
            argv=sys.argv[1:],
            debugging=debugging,
            fake_args=fake_args,
        )

        flags_using: List[str] = []

        if self._validator.validate_g_help(args=args):
            args.remove("--g-help")
            flags_using.append(
                self._validator.validate_g_help(args=args)
            )
            self.global_commands_help()

        if self._validator.validate_g_help_with_cli(args=args):
            args.remove("--g-help-with-cli")
            flags_using.append(
                self._validator.validate_g_help_with_cli(args=args)
            )
            self.global_commands_help(cli_info=True)

        if (
                self._validator.validate_not_args(args=args)
                and cli_app and any(flags_using)
        ):
            raise NoRegisteredCommandsInArguments()

        while args:
            cmd = args[0]
            func_info = self._parser.parse_func_info(cmd, self._commands)

            if self._validator.validate_help_calling(args=args):
                self.command_help(cmd=cmd, func_info=func_info)
                args = args[2:]
                continue

            if self._validator.validate_not_func(func=func_info):
                raise UnexpectedCommandInArguments(cmd=cmd)

            func: Callable[[Any], Any] = func_info.get("func")
            multitypes = func_info.get("multitypes")
            expose = func_info.get("expose")
            expose_prompt = func_info.get("expose_prompt")
            expose_yes_tag = func_info.get("expose_yes_tag")
            expose_no_tag = func_info.get("expose_no_tag")
            required = func_info.get("required")
            _return = func_info.get("_return")

            args = args[1:]
            params, args = self._parser.parse_params(args)

            sig = inspect.signature(func)
            if self._validator.validate_set_required_params(
                    sig_parameters=sig.parameters.items(),
                    params=params, required=required
            ):
                raise CommandWithoutRequiredArgument(
                    required=self._parser.parse_set_required_exception(
                        sig_parameters=sig.parameters.items(),
                        params=params, required=required
                    )
                )

            missing = self._parser.parse_missing(
                parameters=sig.parameters.items(), params=params,
                inspect_parameter=inspect.Parameter.empty
            )

            if self._validator.validate_missing(missing=missing):
                raise CommandWithoutRegisteredMissing(
                    missing=", ".join(missing)
                )

            params = self._parser.parse_multitypes(
                multitypes=multitypes,
                params=params
            )

            if expose:
                if expose_yes_tag in args:
                    args.remove(expose_yes_tag)
                elif expose_no_tag in args:
                    args.remove(expose_no_tag)
                    print(f"Command '{cmd}' skipped by user.")
                    continue
                else:
                    confirm: str = input(expose_prompt).strip().lower()
                    if confirm not in ("y", "yes", expose_yes_tag):
                        print(f"Command '{cmd}' cancelled by user.")
                        continue
            if _return:
                print(func(**params))
                return
            func(**params)

    def global_commands_help(
            self,
            cli_info: bool = False
    ) -> None:

        if not self._commands:
            print("No commands defined.")
            return

        for name, func_info in self._commands.items():
            func = func_info.get("func")
            help_text = func_info.get("help", "No help info available.")
            params_help = func_info.get("params_help", {})

            print(f"Command: {name}")
            print(f"  Description: {help_text}")

            sig = inspect.signature(func)
            if params_help:
                for param in sig.parameters.values():
                    desc = params_help.get(param.name, f"{param.annotation}")
                    print(f"    {param.name}: {desc}")
            else:
                for param in sig.parameters.values():
                    print(f"    {param.name}: {param.annotation}")

            if cli_info:
                print("  [FastCLI] Additional flags:")
                print(f"    multitypes: {func_info.get('multitypes')}")
                print(f"    expose: {func_info.get('expose')}")
                print(f"    expose_prompt: {func_info.get('expose_prompt')}")
                print(f"    expose_yes_tag: {func_info.get('expose_yes_tag')}")
                print(f"    expose_no_tag: {func_info.get('expose_no_tag')}")

            print()

    @staticmethod
    def command_help(
            cmd: str,
            func_info: Dict[str, Any]
    ) -> None:

        if not func_info:
            print(f"{cmd}: Unknown command.")
            return

        func = func_info.get("func")
        print(f"\nDescription: {cmd}")
        print(func_info.get("_help", "No help available."))

        if func_info["params_help"] is None:
            sig = inspect.signature(func)
            for param in sig.parameters.values():
                print(f"  {param.name}: {param.annotation}")
            return

        for param, value in func_info["params_help"].items():
            print(f"  {param}: {value}")


__all__ = ["CLI"]
