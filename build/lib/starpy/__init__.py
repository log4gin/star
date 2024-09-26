from .lexer import lexer
from .compile import parser
from .vm import vm
from .interface import VERSION


__version__ = VERSION

__all__ = [
    "lexer",
    "parser",
    "vm",
]
