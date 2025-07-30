import sys
import inspect

from CLI.errors import (
    NoRegisteredCommandsInArguments,
    UnexpectedCommandInArguments,
    CommandWithoutRegisteredMissing,
)
from CLI.parsers import BaseParser
from CLI.validaters import BaseValidater

class CLI:

    def __init__(self):
        self.commands = {}
        self.base_parser = BaseParser()
        self.base_validator = BaseValidater()


    def command(
        self,
        name: str,
        multitypes: bool = False,
        expose: bool = False,
        expose_prompt: str = "Do you sure? [y/n] ",
        expose_yes_tag: str = "--yes",
        expose_no_tag: str = "--no",
    ) -> callable:
        def decorator(func):
            self.commands[name] = {
                "func": func, "multitypes": multitypes,
                "expose": expose, "expose_prompt": expose_prompt,
                "expose_yes_tag": expose_yes_tag, "expose_no_tag": expose_no_tag,
            }
            return func
        return decorator

    def main(self, cli_app: bool = True):

        args = sys.argv[1:]

        if self.base_validator.validate_not_args(args=args) and cli_app:
            raise NoRegisteredCommandsInArguments()

        while args:
            cmd = args[0]
            func_info = self.commands.get(cmd)

            if self.base_validator.validate_not_func(func=func_info):
                raise UnexpectedCommandInArguments(cmd=cmd)

            func = func_info.get("func")
            multitypes = func_info.get("multitypes")
            expose = func_info.get("expose")
            expose_prompt = func_info.get("expose_prompt")
            expose_yes_tag = func_info.get("expose_yes_tag")
            expose_no_tag = func_info.get("expose_no_tag")

            args = args[1:]
            params, args = self.base_parser.parse_params(args)

            sig = inspect.signature(func)
            missing = [
                name for name, p in sig.parameters.items()
                if name not in params and p.default is inspect.Parameter.empty
            ]
            if self.base_validator.validate_missing(missing=missing):
                raise CommandWithoutRegisteredMissing(missing=", ".join(missing))

            params = self.base_parser.parse_multitypes(multitypes=multitypes, params=params)

            if expose:
                if expose_yes_tag in args:
                    args.remove(expose_yes_tag)
                elif expose_no_tag in args:
                    args.remove(expose_no_tag)
                    print(f"Command '{cmd}' skipped by user.")
                    continue
                else:
                    confirm = input(expose_prompt).strip().lower()
                    if confirm not in ("y", "yes", expose_yes_tag):
                        print(f"Command '{cmd}' cancelled by user.")
                        continue

            func(**params)
            print(func(**params))
