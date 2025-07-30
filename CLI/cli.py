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
