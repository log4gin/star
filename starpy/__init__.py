from .lexer import lexer, token_type, token
from .compile import parser
from .vm import vm
from .interface import VERSION
from .star import main as interpreter

__doc__ = """
Star is a programming language based on Python.
"""

__version__ = VERSION

__all__ = ["lexer", "parser", "vm", "token_type", "token", "__version__", "interpreter"]
