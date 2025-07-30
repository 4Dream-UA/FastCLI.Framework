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